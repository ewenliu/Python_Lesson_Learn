$(function () {
    $('#captcha-img').click(function (event) {
        event.preventDefault();
        var self = $(this);
        var src = self.attr('src');
        var newsrc = blogparam.setParam(src, 'xx', Math.random());
        self.attr('src', newsrc);

    });
});

$(function () {
   $("#captcha-btn").click(function (event) {
       event.preventDefault();
       var email = $("input[name=email]").val();
       if(!email){
           xtalert.alertInfoToast('Please fill emall address');
           return;
       }
       var timestamp = (new Date).getTime();
       // 测试用，真正线上要加密和混淆js
       var sign = md5(email+timestamp+'ajsdoifjaoIFJOIWEF199#!');

       blogajax.post({
           'url': '/common/email_captcha/',
           'data': {
               'email': email,
               'timestamp': timestamp,
               'sign': sign
           },
           'success': function (data) {
               if(data['code']==200){
                   xtalert.alertSuccessToast('Mail sent successful, Notice your inbox!')
               }else {
                   xtalert.alertInfo(data['message'])
               }
           },
           'fail': function () {
               xtalert.alertNetworkError();
           }
       });
   });
});

$(function () {
    $('#submit-btn').click(function (event) {
        event.preventDefault();
        var emailE = $("input[name=email]");
        var email_captchaE = $("input[name=email_captcha]");
        var usernameE = $("input[name=username]");
        var passwordE = $("input[name=password]");
        var password_confirmE = $("input[name=password_confirm]");
        var graph_captchaE = $("input[name=graph_captcha]");

        var email = emailE.val();
        var email_captcha = email_captchaE.val();
        var username = usernameE.val();
        var password = passwordE.val();
        var password_confirm = password_confirmE.val();
        var graph_captcha = graph_captchaE.val();

        blogajax.post({
            'url': '/signup/',
            'data':{
                'email' : email,
                'email_captcha' : email_captcha,
                'username' : username,
                'password' : password,
                'password_confirm' : password_confirm,
                'graph_captcha' : graph_captcha
            },
            'success': function (data) {
                if(data['code']==200){
                    // xtalert.alertSuccess('Sign up successfully, redirect to login page',
                    //     function () {
                    //         window.location = '/';
                    //     });
                    var return_to =  $("#return-to-span").text();
                    if (return_to){
                        window.location = return_to;
                    } else {
                        window.location = '/';
                    }
                }else {
                    var message = data['message'];
                    xtalert.alertInfo(message);
                }
            },
            'fail':function () {
                xtalert.alertNetworkError();
            }
        });
    });
});