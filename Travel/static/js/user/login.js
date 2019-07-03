$(function() {
    $('.login').click(function() {
        var jsObj = {
            uname: $('#uname').val(),
            upwd: $('#upwd').val(),
            validateCode: $('#validateCode').val(),
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        }
        $.ajax({
            type: "post",
            url: "/user/login/",
            data: jsObj,
            success: function(response) {
                alert(response)
                if (response == '登录成功') {
                    location.href = '/'
                } else {
                    location.href = '/user/login'
                }
            }
        });
    });

    $('#yanzma').click(function() {
        $.ajax({
            type: "get",
            url: "/user/yanzma",
            dataType:'json',
            success: function(response) {
                console.log(response.code)
                $('#yanzma').attr('src',response.url+"?t="+Math.random())
            },
            error: function(){
                alert('验证码加载失败')
                location.href='/user/login'
            }
            
        });
    })
})