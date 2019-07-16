$(function () {
    $('#new_pwd_again').blur(function () { 
        var new_pwd = $('#new_pwd').val()
        var re = /^(\w){6,20}$/
        if (new_pwd) {
            if (!re.exec(new_pwd)) {
                $('#show').html('输入的密码格式有误')
            } else {
                var new_pwd_again = $('#new_pwd_again').val()
                if (new_pwd == new_pwd_again) {
                    $('#show').html('')
                } else {
                    $('#show').html('两次输入的密码不一致')
                }
            }
            
        }else{
            $('#show').html('第一次输入密码不能为空')
        }
    });

    $('.login').click(function () {
        if ($('#show').html()) {
            alert('请输入正确的密码')
        } else {
            var jsObj = {
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
                new_pwd : $('#new_pwd').val()
            }
            $.ajax({
                type: "post",
                url: "/user/getpwd",
                data: jsObj,
                success: function (response) {
                    if (response) {
                        alert('修改密码成功,请登录')
                        location.href='/user/login'
                    } else {
                        alert('修改密码失败,请重新输入')
                        location.href = '/user/getpwd'
                    }
                }
            });
        }
    });
})