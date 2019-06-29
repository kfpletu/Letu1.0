$(function(){
    $(".choice .other input").click(function () {
        $(this).parents($('.choice')).children($('.input1')).attr('checked', false)
    });

    $("#zhifubao").click(function(){
        $("#main form").css("margin-right","611px");
        $(".imger").attr("src","/static/images/pay/zhifubao.jpg").css("display","block");
        setTimeout(function(){
            $(".imger").attr("src","/static/images/pay/chenggong_zhifubao.png").css("display","block")
        },3000)
    });
    $("#weixin").click(function(){
        $("#main form").css("margin-right","611px");
        $(".imger").attr("src","/static/images/pay/weixin.jpg").css("display","block");
        setTimeout(function(){
            $(".imger").attr("src","/static/images/pay/chenggong_weixin.png").css("display","block")
        },3000)
    });
    $("#yinlian").click(function(){
        $("#main form").css("margin-right","611px");
        $(".imger").attr("src","/static/images/pay/yinlian.jpg").css("display","block");
        setTimeout(function(){
            $(".imger").attr("src","/static/images/pay/chenggong_yinlian.png").css("display","block")
        },3000)
    })



});