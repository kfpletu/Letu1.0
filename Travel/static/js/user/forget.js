$(function () {

    $('.login').click(function () {
        if ($('#show').html() || !$('#validateCode').val()) {
            alert('请输入验证码')
        } else {
            var jsObj = {
                uname: $('#uname').val(),
                phone: $('#phone').val(),
                email: $('#email').val(),
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
            }
            $.ajax({
                type: "post",
                url: "/user/forget",
                data: jsObj,
                success: function (response) {
                    if (response) {
                        alert(response)
                        location.href = '/user/forget'
                    } else {
                        location.href = '/user/getpwd'
                    }
                }
            });
        }
    });

    $('#yanzma').click(function () {
        $.ajax({
            type: "get",
            url: "/user/yanzma",
            dataType: 'json',
            success: function (response) {
                $('#showImg').html(response.code)
                $('#yanzma').attr('src', response.url + "?t=" + Math.random())
            },
            error: function () {
                alert('验证码加载失败')
                location.href = '/user/login'
            }

        });
    })


    $('#validateCode').blur(function () {
        code = $('#showImg').html()
        inputCode = $('#validateCode').val()
        if (inputCode) {
            if (code == inputCode) {
                $('#show').html('')
            } else {
                $('#show').html('验证码错误,请重新输入')
                $.ajax({
                    type: "get",
                    url: "/user/yanzma",
                    dataType: 'json',
                    success: function (response) {
                        $('#showImg').html(response.code)
                        $('#yanzma').attr('src', response.url + "?t=" + Math.random())
                    },
                    error: function () {
                        alert('验证码加载失败')
                        location.href = '/user/login'
                    }

                });
            }
        } else {
            if ($('#yanzma').attr('src')) {
                $('#show').html('请输入验证码')
            }
        }
    })
})