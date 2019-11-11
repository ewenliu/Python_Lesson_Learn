$(function () {
    var ue = UE.getEditor('editor',{
        'serverUrl': '/ueditor/upload/'
    });

   $("#submit-btn").click(function (event) {
    event.preventDefault();
    var titleE = $("input[name=title]");
    var boardSelet = $("select[name=board]");

    var title = titleE.val();
    var board_id = boardSelet.val();
    var content = ue.getContent();

    blogajax.post({
        'url': '/apost/',
        'data': {
            'title': title,
            'content': content,
            'board_id': board_id
        },
        'success': function (data) {
            if(data['code'] == 200){
                xtalert.alertConfirm({
                    'msg': 'Post created!',
                    'cancelText': 'Return to Home page',
                    'confirmText': 'Post again',
                    'cancelCallback': function () {
                        window.location = '/';
                    },
                    'confirmCallback':function () {
                        titleE.val('');
                        ue.setContent('');
                    }
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