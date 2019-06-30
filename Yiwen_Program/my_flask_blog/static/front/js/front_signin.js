
$(function () {
    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var telephone_input = $("input[name='telephone']");
        var password_input = $("input[name='password']");
        var remember_input = $("input[name='remember']");

        var telephone = telephone_input.val();
        var password = password_input.val();
        //如果点了记住我，返回1，否则返回0
        var remember = remember_input.checked?1:0;


        blogajax.post({
            'url': '/signin/',
            'data': {
                'telephone': telephone,
                'password': password,
                'remember': remember
            },
            'success': function (data) {
                if(data['code'] == 200){
                    var return_to = $("#return-to-span").text();
                    if(return_to){
                        window.location = return_to;
                    }else{
                        window.location = '/';
                    }
                }else{
                    xtalert.alertInfo(data['message']);
                }
            },
        });

    });
});