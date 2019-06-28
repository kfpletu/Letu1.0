$(function(){
    //1.全选和取消全选
    $(".checkAll").click(function(){
        if($(this).attr("checked")){
            //修改为取消选中
            $(this).removeAttr("checked")
            .attr("src","/static/images/user/product_normal.png");
            $(".checkItem").removeAttr("checked")
            .attr("src","/static/images/user/product_normal.png");
        }else{
        $(this).attr("checked","true")
        .attr("src","/static/images/user/product_true.png");
        $(".checkItem").attr("checked","true")
        .attr("src","/static/images/user/product_true.png");
        }
       //调用总价格和总数量的联动函数
       sum();
    });
    //2.反选
    $(".checkItem").click(function(){
        if($(this).attr("checked")){
            $(this).removeAttr("checked").attr("src","/static/images/user/product_normal.png")
        }else{
            $(this).attr("checked","true").attr("src","/static/images/user/product_true.png")
        }
        //被选中的商品数量等于商品元素的个数，视为全选
        if($(".checkItem[checked]").length==$(".checkItem").length){
            //视为全选
            $(".checkAll").attr("src","/static/images/user/product_true.png")
        }else{
            //取消全选
            $(".checkAll").removeAttr("checked")
            .attr("src","/static/images/user/product_normal.png");
        }
        sum();
    });
    //3.数量增减
    $(".add").click(function(){
        //获取前一个兄弟元素输入框的值
        var value = $(this).prev().val();
        value++;
        $(this).prev().val(value);
        countPrice($(this),value);
        sum();  
    });
    $(".minus").click(function(){
        //获取后一个兄弟元素输入框的值
        var value = $(this).next().val();
        if(value>1){
            value--;
        }
        $(this).next().val(value);
        countPrice($(this),value);
        sum();
    });
    //结算确认框
    $("#main .result input").click(function(){
        if($("#main .result .total-price").html()!=0.00){
            $("#box1").css("display","block");
        }else{
            $("#box2").css("display","block");
            setTimeout(function(){
                $("#box2").css("display","none");
            },2000)
        }
    });
    $("#box1 button").click(function(){
        $("#box1").css("display","none");
        $("#content .wait").css("display","block");
        setTimeout(function(){
            $("#content .wait").css("display","none")//删除
        }, 2000)
    
    });
function countPrice(that,value){
    //价格联动 单价*数量 ，修改总金额
    var str = that.parents(".item").find(".gprice p").html();//￥ 299.00
    var price = str.substring(2);
    var sum = price * value;
    sum = sum.toFixed(2);
    //设置总金额
    that.parent().next().html("￥ "+sum);
}
//移除操作
$(".item .action").click(function(){
    //移除整个商品记录
    $(this).parents(".item").remove();
    sum()
});
//总价格和总数量的联动
function sum(){
    //获取被选中的商品，累加商品数量和总价
    var num = 0; //保存总数量
    var price = 0; //保存总价格
    //数据遍历,each(function(){})
    $(".checkItem[checked]").each(function(){
        //每取到一个元素就调用当前函数,this指代函数的调用者
        var n = $(this).parents(".item").find(".gcount input").val();
        var p = $(this).parents(".item").find(".gsum").html();
        //转number
        n = Number(n);
        p = Number(p.substring(2));
        num += n;
        price += p; 
    });
    $(".total-num").html(num);
    $(".total-price").html(price);
    if($(".checkItem[checked]").length){
        $(".result input").css("background","red");
    }else{
        $(".result input").css("background","gray");
    }
    //显示空空如也
    if($("#content .item").length==0){
        $("#empty").css("display","block");
    }

}
//历史订单移除
$(".item .oaction").click(function(){
    //移除整个商品记录
    $(this).parents(".item").remove();
});
});



