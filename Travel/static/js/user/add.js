$(function(){
    // 删除
    $(".item .dele").click(function(){
        var gId = $(this).parents('.item').find(".hid").html()
        var spanList = $("#paging span")
        for(var i=0;i<spanList.length;i++){
            tSpan = Number($(spanList[i]).html())
            if(!(!tSpan)){
                num = tSpan
            }
        } 
        var xhr = createXhr()
        var url = "/user/del/" + gId + '/' + num
        xhr.open('get',url,true)
        xhr.onreadystatechange = function(){
            if(xhr.readyState==4 && xhr.status==200){
                $("body").html(xhr.responseText)
            }
        }  
        xhr.send(null)
    })
    //数量-1
    $(".minus").click(function(){
        var gId = $(this).parents('.item').find(".hid").html()
        var xhr = createXhr()
        var url = "/user/reduce/" + gId 
        xhr.open("get",url,true);
        xhr.send(null);
    })
    //数量+1
    $(".add").click(function(){
        var gId = $(this).parents('.item').find(".hid").html()
        var xhr = createXhr()
        var url = "/user/add/" + gId 
        xhr.open("get",url,true);
        xhr.send(null);
    })
    //确认支付
    $("#box1 .btnYes").click(function(){
        var msg = {
            totalPrice: $(".result .total-price").html()
        }
        $.get("/user/balance",msg,function(data){
            if(data){
                $("#box3").show()
                $("#box3 .bal").html(data)
            }else{
                $(".checkItem[checked]").each(function(){
                    var gId = $(this).parents(".item").find(".hid").html()
                    var xhr = createXhr()
                    var url = "/user/modif/" + gId 
                    xhr.open("get",url,true);
                    xhr.onreadystatechange = function(){
                        if(xhr.readyState==4 && xhr.status==200){
                            window.location.href = xhr.responseText
                        }
                    }  
                    xhr.send(null);
                })
            }
            $("#box3 img").click(function(){
                $("#box3").hide()
            })
        },"json")
    })  
})