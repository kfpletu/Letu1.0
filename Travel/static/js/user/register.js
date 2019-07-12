$(function () {
    $('#uname').blur(function () {
        if ($('#uname')) {
            var uname = $('#uname').val()
            var re = /^[a-zA-Z]{1}([a-zA-Z0-9]|[._]){4,14}$/
            if (!re.exec(uname)) {
                $('#name').html('输入的用户名格式有误')
            } else {
                var xhr = createXhr()
                var url = '/user/checkuname?uname=' + uname
                xhr.open('get', url, true)
                xhr.onreadystatechange = function () {
                    if (xhr.readyState == 4 && xhr.status == 200) {
                        $('#name').html(xhr.responseText)
                    }
                }
                xhr.send(null)
            }
        } else {
            $('#name').html('用户名不能为空')
        }

    });

    
    $('#upwd').blur(function () { 
        var upwd = $('#upwd').val()
        var re = /^(\w){6,20}$/
        if (upwd) {
            if (!re.exec(upwd)) {
                $('#pwd').html('输入的密码格式有误')
            } else {
                $('#pwd').html('')
            }
        } else {
            $('#pwd').html('密码不能为空')
        }
        
    });

    $('#phone').blur(function () {
        var phone = $('#phone').val()
        var re = /^[1][3,4,5,7,8,9][0-9]{9}$/
        if (phone) {
            if (!re.exec(phone)) {
                $('#uphone').html('请输入正确的手机号码!')
            } else {
                var xhr = createXhr()
                var url = '/user/checkphone?phone=' + phone
                xhr.open('get', url, true)
                xhr.onreadystatechange = function () {
                    if (xhr.readyState == 4 && xhr.status == 200) {
                        if (xhr.responseText) {
                            $('#uphone').html(xhr.responseText)
                        } else {
                            $('#uphone').html('请获取手机验证码')
                        }
                    }
                }
                xhr.send(null)
            }
        } else {
            $('#uphone').html('请输入手机号码!')
        }
    })

    $('#btnPhone').click(function () { 
        if ($('#phone').val()) {
            if ($('#uphone').html() != '请获取手机验证码') {
                $('#uphone').html('请输入正确的手机号码')
            } else {
                $('#showMess').css('display', 'block');
                $('#subReg').attr('disabled', true);
                $('#subReg').css('background', 'gray');
            }
        } else {
            $('#uphone').html('请输入手机号码')
        }

    });

    $('#getMes').click(function () { 
        var i = 60
        var timer = setInterval(function () {
            $('#getMes').html(i+'s后可再获取')
            i--
            if (i < 0) {
                clearInterval(timer)
                $('#getMes').html('点击获取');
                $('#getMes').attr('disabled', false);
            }
        }, 1000)
        var jsObj = {
            phone: $('#phone').val(),
        }
        $.ajax({
            type: "get",
            url: "/user/message",
            data:jsObj,
            dataType: 'json',
            success: function (response) {
                $('#showMes').html(response.num);
            }
        });
        $('#getMes').attr('disabled', true);
    });

    $('#setMes').click(function () { 
        setmes = String($('#mes').val());
        getmes = String($('#showMes').html())
        if (getmes == setmes) {
            $('#uphone').html('')
            $('#showMess').css('display', 'none');
            $('#subReg').css('background', '#997679');
            $('#subReg').attr('disabled', false);
        } else {
            alert('验证码输入错误')
            $('#mes').val('');
            $('#subReg').attr('disabled', true);
        }
    });

    $('#email').blur(function () { 
        var email = $('#email').val()
        var re = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/
        if (email) {
            if (!re.exec(email)) {
                $('#uemail').html('请输入正确的邮箱!')
            } else {
                $('#uemail').html('')
            }
        } else {
            $('#uemail').html('请输入邮箱!')
        }
    });


    $('#subReg').click(function () { 
        if ($('#uname').val() && $('#upwd').val() && $('#phone').val() && $('#email').val()) {
            if ($('#name').html() || $('#pwd').html() || $('#uphone').html() || $('#uemail').html()) {
                alert('注册失败')
            } else {
                var xhr = createXhr()
                xhr.open('post', '/user/register', true)
                xhr.onreadystatechange = function () {
                    if (xhr.readyState == 4 && xhr.status == 200) {
                        if (xhr.responseText) {
                            alert(xhr.responseText)
                        } else {
                            alert('注册成功,请登录')
                            location.href = '/user/login'
                        }
                        
                    }
                }
                xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
                var res = 'uname=' + $('#uname').val() + '&upwd=' + $('#upwd').val() +
                    '&phone=' + $('#phone').val() + '&email=' + $('#email').val()
                    + '&csrfmiddlewaretoken=' + $('[name="csrfmiddlewaretoken"]').val()
                console.log(res);
                xhr.send(res)
            }
        } else {
            alert('注册失败')
        }
    });
})