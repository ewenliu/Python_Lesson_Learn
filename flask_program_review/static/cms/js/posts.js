$(function () {
    $(".highlight-btn").click(function () {
        var self = $(this);
        var tr = self.parent().parent();
        var post_id = tr.attr("data-id");
        var highlight = parseInt(tr.attr("data-highlight"));
        var url = "";

        if (highlight){
            url = '/cms/uhpost/';
        }else {
            url = '/cms/hpost/';
        }
        console.log(url, highlight, post_id);
        blogajax.post({
            'url': url,
            'data': {
                'post_id':post_id
            },
            'success':function (data) {
                if (data['code']==200){
                    xtalert.alertSuccessToast('Successful!')
                    setTimeout(function () {
                        window.location.reload();
                    }, 500);
                } else {
                    xtalert.alertInfo(data['message']);
                }
            },
            'fail': function () {
                xtalert.alertNetworkError();
            }
        });
    });
});

$(function () {
    $(".remove-post-btn").click(function () {
        var self = $(this);
        var tr = self.parent().parent();
        var post_id = tr.attr("data-id");
        var url = "/cms/dpost/";

        console.log(post_id, url);
        blogajax.post({
            'url': url,
            'data': {
                'post_id':post_id
            },
            'success':function (data) {
                if (data['code']==200){
                    xtalert.alertSuccessToast('Successful!')
                    setTimeout(function () {
                        window.location.reload();
                    }, 500);
                } else {
                    xtalert.alertInfo(data['message']);
                }
            },
            'fail': function () {
                xtalert.alertNetworkError();
            }
        });
    });
});