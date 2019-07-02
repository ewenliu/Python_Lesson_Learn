
$(function () {
    $('#save-banner-btn').click(function (event) {
        event.preventDefault();
        var dialog = $('#banner-dialog');
        var nameInput = $("input[name='name']");
        var imageInput = $("input[name='image_url']");
        var linkInput = $("input[name='link_url']");
        var priorityInput = $("input[name='priority']");

        var name = nameInput.val();
        var image_url = imageInput.val();
        var link_url = linkInput.val();
        var priority = priorityInput.val();

        if(!name || !image_url || !link_url || !priority){
            xtalert.alertInfoToast('请输入完整的信息');
            return;
        }

        blogajax.post({
            "url": '/cms/abanner/',
            "data": {
                'name': name,
                'image_url': image_url,
                'link_url': link_url,
                'priority': priority
            },
            'success': function (data) {
                dialog.modal("hide");
                if(data['code']==200){
                    window.location.reload()
                }else {
                    xtalert.alertInfo(data['message']);
                }
            },
            'fail':function () {
                xtalert.alertNetworkError();
            }
        });

    });
});