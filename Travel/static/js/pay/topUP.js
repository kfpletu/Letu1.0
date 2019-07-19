$(function () {
    //金额选择的唯一性设定
    $(".choice .other input").click(function () {
        $(this).parents($('.choice')).children($('.input1')).attr('checked', false)

    });
    //支付二维码的显示
    $("#zhifubao").click(function () {
        $(".imger").attr("src", "/static/images/pay/zhifubao.jpg").css("display", "block");
        $(".payimg>.imger").css("opacity", "1");
    });

    $("#weixin").click(function () {
        $(".imger").attr("src", "/static/images/pay/weixin.jpg").css("display", "block");
        $(".payimg>.imger").css("opacity", "1");
    });

    $("#yinlian").click(function () {
        $(".imger").attr("src", "/static/images/pay/yinlian.jpg").css("display", "block");
        $(".payimg>.imger").css("opacity", "1");
    });

    //处理响应回来的状态
    // $.post("/user/topUp",function (data) {
    //     alert(data)
    // })
    //绑定点击事件button,触发事件
    $(".button").click(function () {
        if ($("#money1").prop('checked') || $("#money2").prop('checked') || $("#money3").prop('checked') || $("#money4").prop('checked')) {
            if ($("#zhifubao").prop('checked') || $("#weixin").prop('checked') || $("#yinlian").prop('checked')) {
                payment();
            } else {
                alert("请选择支付方式哦!");
            }
        } else {
            if ($("#money5").val() == 0||$("#money5").val()<0) {
                alert("请输入正确的金额哦!");
            }else {
                if ($("#zhifubao").prop('checked') || $("#weixin").prop('checked') || $("#yinlian").prop('checked')) {
                    payment();
                } else {
                    alert("请选择支付方式哦!");
                }
            }
        }
        // else if ($("#money5").val() != 0) {
        //     // if ($("#zhifubao").prop('checked') || $("#weixin").prop('checked') || $("#yinlian").prop('checked')) {
        //     //     payment();
        //     // } else {
        //     //     alert("请选择支付方式哦!");
        //     // }
        // }
        /* var money = choice();
         console.log(money);
         var csrf={
             money:money,
             csrfmiddlewaretoken:$("[name='csrfmiddlewaretoken']").val()
         };
         $.post("/user/top-top/",csrf,function (data) {
             if(data=="1"){
                 $("#success").css("display","block");
                 $(".payimg>.imger").css("opacity","0.0")
             }else {
                 alert("当前充值人数较多,请客官稍后再试哦!")
             }
         })*/

    });
    $(".closeimg>.clo").click(function () {
        $("#success").css("display", "none");
    })

});

//选择金额的函数
function choice() {
    if ($("#money1").prop('checked')) {
        return $("#money1").val();
    } else if ($("#money2").prop('checked')) {
        return $("#money2").val();
    } else if ($("#money3").prop('checked')) {
        return $("#money3").val();
    } else if ($("#money4").prop('checked')) {
        return $("#money4").val();
    } else {
        if($("#money5").val()<0||$("#money5").val()==0){
            alert("请输入正确的金额哦!")
        }else {
            return $("#money5").val();
        }

    }
}

//封装:异步提交数据,响应处理数据
function payment() {
    var money = choice();
    var csrf = {
        money: money,
        csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
    };
    $.post("/user/top-top/", csrf, function (data) {
        if (data == "1") {
            $("#success").css("display", "block");
            $(".payimg>.imger").css("opacity", "0.0")
        } else {
            alert("当前充值人数较多,请客官稍后再试哦!")
        }
    })
}
