$(function () {
    $('#phone').blur(function () {
        var phone = $('#phone').val()
        var re = /^[1][3,4,5,7,8,9][0-9]{9}$/
        if (phone) {
            if (!re.exec(phone)) {
                $('#uphone').html('请输入正确的手机号码!')
            } else {
                var jsonObj = {
                    phone: $('#phone').val(),
                    csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
                }
                $.ajax({
                    type: "post",
                    url: "/user/check_phone_login/",
                    data: jsonObj,
                    dataType: "json",
                    success: function (response) {
                        if (response.mes) {
                            $('#uphone').html(response.mes);
                            $('#btnPhone').attr('disabled', true);
                        } else {
                            $('#uphone').html(response.mes);
                            $('#btnPhone').attr('disabled', false);
                        }
                    }
                });
            }
        } else {
            $('#uphone').html('手机号码不能为空!')
        }
    })


    $('#btnPhone').click(function () {
        if ($('#phone').val()) {
            if ($('#uphone').html()) {
            } else {
                var i = 60
                var timer = setInterval(function () {
                    $('#btnPhone').html(i + 's后可再获取')
                    i--
                    if (i < 0) {
                        clearInterval(timer)
                        $('#btnPhone').html('点击获取');
                        $('#btnPhone').attr('disabled', false);
                    }
                }, 1000)
                var jsObj = {
                    phone: $('#phone').val(),
                }
                $.ajax({
                    type: "get",
                    url: "/user/getMes/",
                    data: jsObj,
                    dataType: "json",
                    success: function (response) {
                        $('#uphone').html('验证码已发送至您的手机,请查看')
                        $('#showMes').html(response.num);
                    }
                });
                $('#btnPhone').attr('disabled', true);
            }
        } else {
            $('#uphone').html('手机号码不能为空!')
        }
    });

    $('#mes').blur(function () {
        if ($('#mes').val()) {
            if (String($('#mes').val()) == String($('#showMes').html())) {
                $('#uphone').html('')
                $('#umes').html('')
            } else {
                $('#umes').html('验证码输入错误')
            }
        } else {
            $('#umes').html('验证码不能为空');
        }
    });
    
    $('#btn').click(function () {
        if (!$('#phone').val() && !$('#mes').val()) {
            alert('请输入正确信息')
        } else {
            if (!$('#phone').val() || !$('#mes').val()) {
                alert('登录失败')
            } else {
                if ($('#uphone').html() || $('#umes').html()) {
                    alert('登录失败')
                } else {
                    var jsObj = {
                        phone: $('#phone').val(),
                        csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
                    }
                    $.ajax({
                        type: "post",
                        url: "/user/phoneLogin/",
                        data: jsObj,
                        success: function (response) {
                            if (response) {
                                alert('登录失败,请重新登录')
                                location.href = '/user/phoneLogin'
                            } else {
                                alert('登录成功')
                                if (document.referrer=='http://127.0.0.1:7890/user/register' ||
                                    document.referrer=='http://127.0.0.1:7890/user/forget' ||
                                    document=='http://127.0.0.1:7890/user/getpwd/'){
                                    location.href='/'
                                }else{
                                    window.location=document.referrer
                                }
                            }
                        }
                    });
                }
            }
        }
        
    });
})