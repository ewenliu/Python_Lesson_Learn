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
    $("#submit").click(function (event) {
        event.preventDefault();
        var emailE = $("input[name=email]");
        var captchaE = $("input[name=captcha]");

        var email = emailE.val();
        var captcha = captchaE.val();

        blogajax.post({
            'url': '/cms/resetemail/',
            'data':{
                'email':email,
                'captcha': captcha
            },
            'success': function (data) {
                if(data['code']==200){
                    emailE.val('');
                    captchaE.val('');
                    xtalert.alertSuccess('Mail address changed!',function () {
                        window.location = '/cms/logout/';
                    });
                }else {
                    xtalert.alertInfo(data['message']);
                }
            },
            'fail': function () {
                xtalert.alertNetworkError();
            }
        });
    });
});