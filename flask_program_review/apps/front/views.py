# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 15:29
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : views.py
# @Documents:
from flask import Blueprint, views, render_template, request, session, url_for, g, abort, redirect
from .forms import SignupForm, SigninForm, AddPostForm, AddCommentForm
from utils import restful, safeutils
from exts import db
from .models import FrontUser
from ..models import BannerModel, BoardModel, PostModel, CommentModel, HighlightPostModel
import config
from .decorators import login_required
from flask_paginate import Pagination, get_page_parameter
from sqlalchemy.sql import func


bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    board_id = request.args.get('board_id', type=int, default=None)
    # 定制page参数
    page = request.args.get(get_page_parameter(), type=int, default=1)
    # 默认按照发布时间进行排序， 1=时间排序，2=精华排序，3=点赞个数排序， 4=评论数排序
    sort = request.args.get('sort_method', type=int, default=1)
    banners = BannerModel.query.order_by(BannerModel.priority).limit(3)
    boards = BoardModel.query.all()
    # posts = PostModel.query.all()
    # 获取当前page第一篇帖子id在数据库中起始位置
    start = (page-1)*config.PER_PAGE
    # PER_PAGE当前=10，即一页最多10篇帖子
    end = start+config.PER_PAGE
    # 如果按板块进行渲染
    total_page = 0

    query_obj = None
    if sort == 1:
        query_obj = PostModel.query.order_by(PostModel.create_time.desc())
    elif sort == 2:
        # 通过两张表进行查询要用db.session， 如果一张表则用Model就行
        # 按照加精的时间倒序排序
        # 如果没被加精，则按照帖子本身发布的时间进行倒序排序
        query_obj = db.session.query(PostModel).outerjoin(HighlightPostModel).order_by(
            HighlightPostModel.create_time.desc(), PostModel.create_time.desc())
    # 点赞的个数排序
    # elif sort == 3:
    #     query_obj = PostModel.query.order_by(PostModel.create_time.desc())
    # 按照评论数排序
    elif sort == 3:
        # 对应的sql：
        # SELECT post.id AS post_id, post.title AS post_title, post.content AS post_content, post.create_time AS post_create_time, post.board_id AS post_board_id, post.author_id AS post_author_id
        # FROM post LEFT OUTER JOIN comment ON post.id = comment.post_id GROUP BY post.id ORDER BY count(comment.id) DESC, post.create_time DESC
        query_obj = db.session.query(PostModel).outerjoin(CommentModel).group_by(PostModel.id).order_by(
            func.count(CommentModel.id).desc(), PostModel.create_time.desc())
    else:
        abort(404)

    if board_id:
        query_obj = query_obj.filter(PostModel.board_id==board_id)
        posts = query_obj.slice(start, end)
        total_page = query_obj.count()
        post_count = PostModel.query.filter(PostModel.board_id==board_id).count()
    else:
        posts = query_obj.slice(start, end)
        total_page = query_obj.count()
        post_count = PostModel.query.count()


    # outer_window, inner_window用来限制翻页div的左右的动态个数
    pagination = Pagination(bs_version=3, page=page, total=total_page, outer_window=0, inner_window=2)
    context = {
        'banners': banners,
        'boards': boards,
        'posts': posts,
        'pagination': pagination,
        'current_board_id': board_id,
        'current_sort_method': sort,
        'post_count': post_count
    }
    return render_template('front/front_index.html', **context)


@bp.route('/p/<post_id>/')
def post_detail(post_id):
    post = PostModel.query.get(post_id)
    if post:
        return render_template('front/front_pdetail.html', post=post)
    else:
        abort(500)


@bp.route('/acomment/', methods=['POST'])
@login_required
def acomment():
    form = AddCommentForm(request.form)
    if form.validate():
        content = form.content.data
        post_id = form.post_id.data
        post = PostModel.query.get(post_id)
        post.num_comment += 1
        if post:
            comment = CommentModel(content=content)
            comment.post = post
            comment.author = g.front_user
            db.session.add(comment)
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='No such post!')
    else:
        return restful.params_error(form.get_error())


# a = add
@bp.route('/apost/', methods=['GET', 'POST'])
@login_required
def apost():
    if request.method == 'GET':
        boards = BoardModel.query.all()
        context = {
            'boards': boards
        }
        return render_template('front/front_apost.html', **context)
    else:
        form = AddPostForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            board_id = form.board_id.data
            board = BoardModel.query.get(board_id)
            if not board:
                return restful.params_error(message='No such board!')
            post = PostModel(title=title, content=content)
            post.board = board
            post.author = g.front_user
            db.session.add(post)
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(form.get_error())


@bp.route('/logout/')
@login_required
def logout():
    del session[config.FRONT_USER_ID]
    return redirect(url_for('front.index'))


class SignupView(views.MethodView):

    def get(self):
        # 网页跳转功能
        # 后台判断是否是跳转过来的而非直接方位，如果是，则在模板页面加一个id="return-to-span" 的span
        return_to = request.referrer
        # 判断return to 是否为安全
        if return_to and return_to != request.url and safeutils.is_safe_url(return_to):
            return render_template('front/front_signup.html', return_to=return_to)
        else:
            return render_template('front/front_signup.html')

    def post(self):
        form = SignupForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = FrontUser(email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message=form.get_error())


class SigninView(views.MethodView):

    def get(self):
        return_to = request.referrer
        # 如果从注册页面来的，登陆完就不要返回回去了
        if return_to and return_to != request.url and return_to != url_for('front.signup') and safeutils.is_safe_url(return_to):
            return render_template('front/front_signin.html', return_to=return_to)
        else:
            return render_template('front/front_signin.html')

    def post(self):
        form = SigninForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = FrontUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.FRONT_USER_ID] = user.id
                if remember:
                    session.permanent = True
                return restful.success()
            else:
                return restful.params_error(message='Wrong email or password!')
        else:
            return restful.params_error(message=form.get_error())


bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))
bp.add_url_rule('/signin/', view_func=SigninView.as_view('signin'))
