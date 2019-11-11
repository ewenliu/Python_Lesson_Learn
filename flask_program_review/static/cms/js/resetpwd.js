$(function () {
    $("#submit").click(function (event) {
        event.preventDefault();
        var oldpwdE = $("input[name=oldpwd]");
        var newpwdE = $("input[name=newpwd]");
        var newpwd2E = $("input[name=newpwd2]");

        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var newpwd2 = newpwd2E.val();

        blogajax.post({
            'url': '/cms/resetpwd/',
            'data': {
                'oldpwd': oldpwd,
                'newpwd': newpwd,
                'newpwd2': newpwd2
            },
            'success': function (data) {
                if(data['code'] == 200){
                    oldpwdE.val('');
                    newpwdE.val('');
                    newpwd2E.val('');
                    xtalert.alertSuccess('Password change successfully! Redirect to login page',
                    function () {
                        window.location = '/cms/logout/';
                    });
                }else {
                    var message = data['message'];
                    xtalert.alertInfo(message);
                }
            },
            'fail': function (error) {
                xtalert.alertNetworkError();
            }
        });
    });
});
