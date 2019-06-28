//等待页面加载完毕
$(function(){
    var imgList = $("#imgd img");
    var liList = $("#imgd li");
    var index = 0;
    var timer = setInterval(autoPlay,2000);
    function autoPlay(){
        //当前图片隐藏
        imgList.eq(index).css("display","none");
        liList.eq(index).css("background","rgba(0,0,0,0)");
        index ++;
        if(index == imgList.length){
            index = 0;
        }
        //元素显示
        imgList.eq(index).css("display","block");
        liList.eq(index).css("background","#fff");
    }
    $("#imgd").mouseover(function (){
        clearInterval(timer);
    });
    $("#imgd").mouseout(function (){
        timer = setInterval(autoPlay,2000);
    });
    //向左翻动
    $("#imgd .left").click(function(){
        //当前元素隐藏
		$("#imgd img").eq(index).css("display","none");
		$("#imgd li").eq(index).css("background","rgba(0,0,0,0)");
		//更新下标
		index = --index == -1 ? $("#imgd img").length-1 : index;
		//设置显示
		$("#imgd img").eq(index).css("display","block");
		$("#imgd li").eq(index).css("background","#fff");
    });
    //向右翻动
    $("#imgd .right").click(function(){
        //当前元素隐藏
		$("#imgd img").eq(index).css("display","none");
		$("#imgd li").eq(index).css("background","rgba(0,0,0,0)");
		//更新下标
		index = ++index == $("#imgd img").length ? 0 : index;
		//设置显示
		$("#imgd img").eq(index).css("display","block");
		$("#imgd li").eq(index).css("background","#fff");
    });
    //点击圆点实现翻页
    for(var i=0;i<imgList.length;i++){
        $(liList.eq(i)).click(function(){
            liList.eq(index).css("background","rgba(0,0,0,0)");
            $(this).css("background","#fff");
            imgList.eq(index).css("display","none");
            for(var j=0;j<liList.length;j++){
                //点击后同步更改下标
                if(liList.eq(j).css("background-color")=="rgb(255, 255, 255)"){
                    index = j;
                }
            }
            imgList.eq(index).css("display","block");  
        })
    }

    $("#tour #search2 img").mouseover(function(){
        $(this).attr('src',"/static/images/home/search2.png")
    })
    $("#tour #search2 img").mouseout(function(){
        $(this).attr('src',"/static/images/home/search1.png")
        $(this).prev().css('outline','none')
    })
})



