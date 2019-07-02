$(function(){
    $(".minus").click(function(){
        var xhr = createXhr()
        var url = 
        xhr.open("get",url,true);
        console.log(url)
        // xhr.onreadystatechange = function(){
        //     if(xhr.readyState==4 && xhr.status==200){
        //         $("#uname-show").html(xhr.responseText);
        //     }
        // }
        xhr.send(null);
    })
    
})