
$(function () {
    $('#add-board-btn').click(function (event) {
        event.preventDefault();
        xtalert.alertOneInput({
            'text': '请输入板块名称！',
            'placeholder': '板块名称',
            'confirmCallback': function (inputValue) {
                blogajax.post({
                    'url': '/cms/aboard/',
                    'data':{
                        'name': inputValue
                    },
                    'success': function (data) {
                        if(data['code']==200){
                            window.location.reload();
                        }else {
                            xtalert.alertInfo(data['message']);
                        }
                    }
                });
            }
        });
    });
});