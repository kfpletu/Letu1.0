$(function() {
    // 删除
    $("#delect").click(function () {
        // var gId = $(this).parents('.item').find(".hid").html();
        var id=$(".hid").html();
        console.log(id);
        var xhr = createXhr();
        var url = "/user/delete?id="+id;

        console.log(url);
        xhr.open('get', url, true);
        xhr.send(null)
    });
});
