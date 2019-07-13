$(function() {
    $('.login').click(function() {
        if ($('#show').html() ||!$('#validateCode').val()){
            alert('请输入验证码')
        }else{
            var jsObj = {
                uname: $('#uname').val(),
                upwd: $('#upwd').val(),
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
            }
            $.ajax({
                type: "post",
                url: "/user/login/",
                data: jsObj,
                success: function(response) {
                    alert(response)
                    if (response == '登录成功') {
                        if (document.referrer=='http://127.0.0.1:7890/user/register' ||
                            document.referrer=='http://127.0.0.1:7890/user/forget' ||
                            document=='http://127.0.0.1:7890/user/getpwd/'){
                            location.href='/'
                        }else{
                            window.location=document.referrer
                        }
                    } else {
                        location.href = '/user/login'
                    }
                }
            });
        }
    });
})