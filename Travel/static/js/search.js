$(function () {
    $("#search2 img").mouseover(function(){
        $(this).attr('src',"/static/images/home/search2.png")
    });
    $("#search2 img").mouseout(function(){
        $(this).attr('src',"/static/images/home/search1.png");
        $(this).prev().css('outline','none')
    })
});