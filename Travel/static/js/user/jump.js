$(function(){
    var xhr = createXhr()
    console.log($(".oNum").text())
    var url = '/user/jump?orderNum=' + $(".oNum").html() + '&&' + 'orderPrice=' + $(".oPrice").html()
    xhr.open("get",url,true);
    console.log(url)
    // xhr.onreadystatechange = function(){
    //     if(xhr.readyState==4 && xhr.status==200){
    //         $("#uname-show").html(xhr.responseText);
    //     }
    // }
    xhr.send(null);
})