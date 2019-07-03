$(function () {
    $('.login').click(function () { 
        var jsObj = {
            uname: $('#uname').val(),
            upwd: $('#upwd').val(),
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        }
        $.ajax({
            type: "post",
            url: "/user/login/",
            data: jsObj,
            success: function (response) {
                alert(response)
                if (response == '登录成功') {
                    location.href='/'
                } else {
                    location.href='/user/login'
                }
            }
        });
    });
})