$(function() {

    
    $('.login').click(function() {
        if ($('#show').html() ||!$('#validateCode').val()){
            alert('请输入验证码')
        }else{
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
        }
    });

    $('#yanzma').click(function() {
        $.ajax({
            type: "get",
            url: "/user/yanzma",
            dataType:'json',
            success: function(response) {
                $('#showImg').html(response.code)
                $('#yanzma').attr('src',response.url+"?t="+Math.random())
            },
            error: function(){
                alert('验证码加载失败')
                location.href='/user/login'
            }
            
        });
    })

    $('#validateCode').blur(function(){
        code = $('#showImg').html()
        inputCode = $('#validateCode').val()
        console.log(code,inputCode)
        if(inputCode){
            if(code == inputCode){
                $('#show').html('')
            }else{
                $('#show').html('验证码错误,请重新输入')
                $.ajax({
                    type: "get",
                    url: "/user/yanzma",
                    dataType:'json',
                    success: function(response) {
                        $('#showImg').html(response.code)
                        $('#yanzma').attr('src',response.url+"?t="+Math.random())
                    },
                    error: function(){
                        alert('验证码加载失败')
                        location.href='/user/login'
                    }
                    
                });
            }
        }else{
            if($('#yanzma').attr('src')){
                $('#show').html('请输入验证码')
            }
        }
    })
    
})