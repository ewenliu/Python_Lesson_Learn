# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 15:29
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : views.py
# @Documents:
from flask import (
    Blueprint,
    views,
    render_template,
    request,
    session,
    redirect,
    url_for,
    g)
from .forms import (
    LoginForm,
    ResetpwdForm,
    ResetEmailForm,
    AddBannerForm,
    UpdateBannerForm,
    AddBoardForm,
    UpdateBoardForm,
    DeleteBoardForm)
from .models import CMSUser, CMSPermission
from ..models import BannerModel, BoardModel, PostModel, HighlightPostModel
from .decorators import login_required, permission_required
import config
from exts import db, mail
from utils import restful
from flask_mail import Message

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')


@bp.route('/logout/')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))


@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')


@bp.route('/posts/')
@login_required
@permission_required(CMSPermission.POSTER)
def posts():
    context = {
        'posts': PostModel.query.all()
    }
    return render_template('cms/cms_posts.html', **context)


# h = highlight
@bp.route('/hpost/', methods=['POST'])
@login_required
@permission_required(CMSPermission.POSTER)
def hpost():
    post_id = request.form.get('post_id')
    if not post_id:
        return restful.params_error('Please fill post id')
    post = PostModel.query.get(post_id)
    if not post:
        return restful.params_error('No such post!')

    highlight = HighlightPostModel()
    highlight.post = post
    db.session.add(highlight)
    db.session.commit()
    return restful.success()


@bp.route('/uhpost/', methods=['POST'])
@login_required
@permission_required(CMSPermission.POSTER)
def uhpost():
    post_id = request.form.get('post_id')
    if not post_id:
        return restful.params_error('Please fill post id')
    post = PostModel.query.get(post_id)
    if not post:
        return restful.params_error('No such post!')

    highlight = HighlightPostModel.query.filter_by(post_id=post_id).first()
    db.session.delete(highlight)
    db.session.commit()
    return restful.success()


@bp.route('/dpost/', methods=['POST'])
@login_required
@permission_required(CMSPermission.POSTER)
def dpost():
    post_id = request.form.get('post_id')
    if not post_id:
        return restful.params_error('Please fill post id')
    post = PostModel.query.get(post_id)
    # print(post_id, post)
    if not post:
        return restful.params_error('No such post!')

    db.session.delete(post)
    db.session.commit()
    return restful.success()


@bp.route('/comments/')
@login_required
@permission_required(CMSPermission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')


@bp.route('/boards/')
@login_required
@permission_required(CMSPermission.BOARDER)
def boards():
    board_models = BoardModel.query.all()
    context = {
        'boards': board_models
    }
    return render_template('cms/cms_boards.html', **context)


@bp.route('/aboard/', methods=['POST'])
@login_required
@permission_required(CMSPermission.BOARDER)
def aboard():
    form = AddBoardForm(request.form)
    if form.validate():
        name = form.name.data
        board = BoardModel(name=name)
        db.session.add(board)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(form.get_error())


@bp.route('/uboard/', methods=['POST'])
@login_required
@permission_required(CMSPermission.BOARDER)
def uboard():
    form = UpdateBoardForm(request.form)
    if form.validate():
        board_id = form.board_id.data
        name = form.name.data
        if not board_id:
            return restful.params_error('Please type in board id!')
        board = BoardModel.query.get(board_id)
        if not board:
            return restful.params_error('No such board!')
        board.name = name
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(form.get_error())


@bp.route('/dboard/', methods=['POST'])
@login_required
@permission_required(CMSPermission.BOARDER)
def dboard():
    form = DeleteBoardForm(request.form)
    if form.validate():
        board_id = form.board_id.data
        if not board_id:
            return restful.params_error('Please type in board id!')
        board = BoardModel.query.get(board_id)
        if not board:
            return restful.params_error('No such board!')
        db.session.delete(board)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(form.get_error())



@bp.route('/fusers/')
@login_required
@permission_required(CMSPermission.FRONTUSER)
def fusers():
    return render_template('cms/cms_fusers.html')


@bp.route('/cusers/')
@login_required
@permission_required(CMSPermission.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')


@bp.route('/cgroups/')
@login_required
@permission_required(CMSPermission.ALL_PERMISSION)
def cgroups():
    return render_template('cms/cms_cgroups.html')


# 测试邮件接口用
@bp.route('/email/')
def send_email():
    message = Message(subject='ewen blog mail send system', recipients=['kevin.2.liu@nokia-sbell.com'],
                      body='Email captcha test')
    mail.send(message)
    return 'Success'


@bp.route('/banners/')
@login_required
@permission_required(CMSPermission.POSTER)
def banners():
    banners = BannerModel.query.order_by(BannerModel.priority).all()
    return render_template('cms/cms_banners.html', banners=banners)


# a = add
@bp.route('/abanner/', methods=['POST'])
@login_required
@permission_required(CMSPermission.POSTER)
def abanner():
    form = AddBannerForm(request.form)
    if form.validate():
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner = BannerModel(name=name, image_url=image_url, link_url=link_url, priority=priority)
        db.session.add(banner)
        db.session.commit()
        return restful.success()
    else:
        return restful.success(message=form.get_error())


# u = update
@bp.route('/ubanner/', methods=['POST'])
@login_required
@permission_required(CMSPermission.POSTER)
def ubanner():
    form = UpdateBannerForm(request.form)
    if form.validate():
        banner_id = form.banner_id.data
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner = BannerModel.query.get(banner_id)
        if banner:
            banner.name = name
            banner.image_url = image_url
            banner.link_url = link_url
            banner.priority = priority
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error('No such banner!')
    else:
        return restful.params_error(form.get_error())


# d = delete
@bp.route('/dbanner/', methods=['POST'])
@login_required
@permission_required(CMSPermission.POSTER)
def dbanner():
    banner_id = request.form.get('banner_id')
    if not banner_id:
        return restful.params_error(message='Please type in banner id!')
    banner = BannerModel.query.get(banner_id)
    if not banner:
        return restful.params_error(message='No such banner, check id!')
    db.session.delete(banner)
    db.session.commit()
    return restful.success()


@bp.route('/qiniu_test/')
def qiniu_test():
    return render_template('cms/qiniu_upload.html')


class LoginView(views.MethodView):

    def get(self, message=None):
        return render_template('cms/cms_login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    # permanent = True 过期时间是31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='Wrong email address or password')
        else:
            message = form.get_error()
            return self.get(message=message)


class ResetPwdView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                return restful.success()
            else:
                return restful.params_error('Wrong old password!')
        else:
            return restful.params_error(form.get_error())


class ResetEmailView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetmail.html')

    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            email = form.email.data
            g.cms_user.email = email
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message=form.get_error())


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))
bp.add_url_rule('/resetemail/', view_func=ResetEmailView.as_view('resetemail'))
