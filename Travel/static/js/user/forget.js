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
                        location.href = '/user/getpwd/'
                    }
                }
            });
        }
    });

    
})