$(function () {
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