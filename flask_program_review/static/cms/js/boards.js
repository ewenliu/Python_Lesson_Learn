$(function () {
    $('#add-board-btn').click(function (event) {
        event.preventDefault();
        xtalert.alertOneInput({
            'text': 'Please type in board name!',
            'placeholder': 'Board name',
            'confirmCallback': function (inputValue) {
                blogajax.post({
                    'url': '/cms/aboard/',
                    'data': {
                        'name': inputValue
                    },
                    'success': function (data) {
                        if(data['code']==200){
                            window.location.reload();
                        }else{
                            xtalert.alertInfo(data['message']);
                        }
                    },
                    'fail':function () {
                        xtalert.alertNetworkError();
                    }
                });
            }
        });
    });
});

$(function () {
    $(".edit-board-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var tr = self.parent().parent();

        var name = tr.attr("data-name");
        var board_id = tr.attr("data-id");

        xtalert.alertOneInput({
            'text': 'Please type in board name!',
            'placeholder': 'Board name',
            'confirmCallback': function (inputValue) {
                blogajax.post({
                    'url': '/cms/uboard/',
                    'data': {
                        'name': inputValue,
                        'board_id': board_id
                    },
                    'success': function (data) {
                        if(data['code']==200){
                            window.location.reload();
                        }else{
                            xtalert.alertInfo(data['message']);
                        }
                    },
                    'fail':function () {
                        xtalert.alertNetworkError();
                    }
                });
            }
        });
    });
});

$(function () {
    $(".delete-board-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var tr = self.parent().parent();
        var boardId = tr.attr("data-id");

        xtalert.alertConfirm({
            'msg': 'Sure to delete this board?',
            'confirmCallback': function () {
                blogajax.post({
                    'url': '/cms/dboard/',
                    'data':{
                        'board_id': boardId
                    },
                    'success': function (data) {
                        if(data['code']==200){
                            window.location.reload();
                        }else {
                            xtalert.alertInfo(data['message']);
                        }
                    },
                    'fail': function () {
                        xtalert.alertNetworkError();
                    }
                })
            }
        })
    });
});
