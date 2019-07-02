$(function(){
    // 删除
    $(".item .dele").click(function(){
        var gId = $(this).parents('.item').find(".hid").html()
        console.log(gId)
        var xhr = createXhr()
        var url = "/user/del/" + gId
        xhr.open('get',url,true)
        xhr.send(null)
    })
    //数量-1
    $(".minus").click(function(){
        var gId = $(this).parents('.item').find(".hid").html()
        console.log(gId)
        var xhr = createXhr()
        var url = "/user/reduce/" + gId 
        xhr.open("get",url,true);
        xhr.send(null);
    })
    //数量+1
    $(".add").click(function(){
        var gId = $(this).parents('.item').find(".hid").html()
        console.log(gId)
        var xhr = createXhr()
        var url = "/user/add/" + gId 
        xhr.open("get",url,true);
        xhr.send(null);
    })
    $("#box1 .btnYes").click(function(){
        console.log('1111')
        $("checkItem[checked]").each(function(){
            var gId = $(this).parents('#content').find(".hid").html()
            console.log(gId)
            var xhr = createXhr()
            var url = "/user/modif/" + gId 
            xhr.open("get",url,true);
            xhr.send(null);
        })
    })  
})