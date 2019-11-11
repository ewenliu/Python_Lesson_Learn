$(function () {
    $("#submit-btn").click(function (event) {
        event.preventDefault();

        var emailE = $("input[name=email]");
        var passwordE = $("input[name=password]");
        var rememberE = $("input[name=remember]");

        var email=  emailE.val();
        var password =  passwordE.val();
        var remember =  rememberE.checked ? 1:0;

        blogajax.post({
            'url': '/signin/',
            'data':{
                'email': email,
                'password': password,
                'remember': remember
            },
            'success': function (data) {
                if(data['code']==200){
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