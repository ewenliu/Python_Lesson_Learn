
$(function () {
   $('#captcha-img').click(function (event) {
       var self = $(this);
       var src = self.attr('src');
       var newsrc = blogparam.setParam(src, 'xx', Math.random());
       self.attr('src', newsrc);
   });
});

$(function () {
    $('#sms-captcha-btn').click(function (event) {
        event.preventDefault();
        var self = $(this);
        var telephone = $('input[name="telephone"]').val();
        if(!(/^1[345879]\d{9}$/.test(telephone))){
            xtalert.alertInfoToast('请输入正确的手机号码');
            return;
        }
        blogajax.get({
           'url': '/c/sms_captcha/?telephone='+telephone,
            'success': function (data) {
                if(data['code']==200){
                    xtalert.alertSuccessToast('短信验证码发送成功');
                    self.attr('disabled', 'disabled');
                    var timeCount = 60;
                    var timer = setInterval(function () {
                        timeCount--;
                        self.text(timeCount);
                        if(timeCount <= 0){
                            self.removeAttr('disabled');
                            clearInterval(timer);
                            self.text('Send SMS Code');
                        }
                    }, 1000);
                }else{
                    xtalert.alertInfoToast(data['message']);
                }
            }
        });
    });
});
