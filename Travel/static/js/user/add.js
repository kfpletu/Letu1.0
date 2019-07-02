$(function(){
    $(".item .dele").click(function(){
        var gId = $("#content .hid").html()
        console.log(gId)
        var xhr = createXhr()
        var url = "/user/del/" + gId
        xhr.open('get',url,true)
        xhr.send(null)
    })

    // $(".minus").click(function(){
    //     var xhr = createXhr()
    //     var url = "/user/add/" + (num+1)
    //     xhr.open("get",url,true);
    //     console.log(url)
    //     // xhr.onreadystatechange = function(){
    //     //     if(xhr.readyState==4 && xhr.status==200){
    //     //         $("#uname-show").html(xhr.responseText);
    //     //     }
    //     // }
    //     xhr.send(null);
    // })
    
})