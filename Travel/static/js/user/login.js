$(function () {
    $('.login').click(function () { 
        var jsObj = {
            uname: $('#uname').val(),
            upwd: $('#upwd').val(),
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        }
        $.post("/user/login/", jsObj,
            function () {
                alert('登录成功')
                location.href = '/'
            },
            
        );
    });
})