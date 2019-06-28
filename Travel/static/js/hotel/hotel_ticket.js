$(function(){
	var i=0
	function eq(i){
		return "#pics-thumbs img:eq("+i+')'
	}
	var margin_left_value=0
	var timer
	$(eq(0)).mouseover(function(){
		if (timer) {
			clearInterval(timer)
		}
		if (margin_left_value>0) {
			
			timer=setInterval(function(){
			if(margin_left_value<=0){
				clearInterval(timer)
				return
			}	
			margin_left_value-=10
			$('#pics-thumbs img').parents('#pics-thumbs').prev().css('margin-left',margin_left_value+'px')
			// console.log(margin_left_value+'px')	
		},10)			
		}else {
			timer=setInterval(function(){
			if(margin_left_value>=0){
				clearInterval(timer)
				return
			}	
			margin_left_value+=10
			$('#pics-thumbs img').parents('#pics-thumbs').prev().css('margin-left',margin_left_value+'px')
			// console.log(margin_left_value+'px')	
		},10)			
		}
		
	})
	$(eq(1)).mouseover(function(){
		if (timer) {
			clearInterval(timer)
		}
		if (margin_left_value>-670) {
			
			timer=setInterval(function(){
			if(margin_left_value<=-670){
				clearInterval(timer)
				return
			}	
			margin_left_value-=10
			$('#pics-thumbs img').parents('#pics-thumbs').prev().css('margin-left',margin_left_value+'px')
			// console.log(margin_left_value+'px')	
		},10)			
		}else {
			timer=setInterval(function(){
			if(margin_left_value>=-670){
				clearInterval(timer)
				return
			}	
			margin_left_value+=10
			$('#pics-thumbs img').parents('#pics-thumbs').prev().css('margin-left',margin_left_value+'px')
			// console.log(margin_left_value+'px')	
		},10)			
		}
		
	})
	$(eq(2)).mouseover(function(){
		if (timer) {
			clearInterval(timer)
		}
		if (margin_left_value>-670*2) {
			
			timer=setInterval(function(){
			if(margin_left_value<=-670*2){
				clearInterval(timer)
				return
			}	
			margin_left_value-=10
			$('#pics-thumbs img').parents('#pics-thumbs').prev().css('margin-left',margin_left_value+'px')
			// console.log(margin_left_value+'px')	
		},10)			
		}else {
			timer=setInterval(function(){
			if(margin_left_value>=-670*2){
				clearInterval(timer)
				return
			}	
			margin_left_value+=10
			$('#pics-thumbs img').parents('#pics-thumbs').prev().css('margin-left',margin_left_value+'px')
			// console.log(margin_left_value+'px')	
		},10)			
		}
		
	})
	$(eq(3)).mouseover(function(){
		if (timer) {
			clearInterval(timer)
		}
		if (margin_left_value>-670*3) {
			
			timer=setInterval(function(){
			if(margin_left_value<=-670*3){
				clearInterval(timer)
				return
			}	
			margin_left_value-=10
			$('#pics-thumbs img').parents('#pics-thumbs').prev().css('margin-left',margin_left_value+'px')
			// console.log(margin_left_value+'px')	
		},10)			
		}else {
			timer=setInterval(function(){
			if(margin_left_value>=-670*3){
				clearInterval(timer)
				return
			}	
			margin_left_value+=10
			$('#pics-thumbs img').parents('#pics-thumbs').prev().css('margin-left',margin_left_value+'px')
			// console.log(margin_left_value+'px')	
		},10)			
		}
		
	})
	$(eq(4)).mouseover(function(){
		if (timer) {
			clearInterval(timer)
		
		}
		if (margin_left_value>-670*4) {
			
			timer=setInterval(function(){
			if(margin_left_value<=-670*4){
				clearInterval(timer)
				return
			}	
			margin_left_value-=10
			$('#pics-thumbs img').parents('#pics-thumbs').prev().css('margin-left',margin_left_value+'px')
			// console.log(margin_left_value+'px')	
		},10)			
		}else {
			timer=setInterval(function(){
			if(margin_left_value>=-670*4){
				clearInterval(timer)
				return
			}	
			margin_left_value+=10
			$('#pics-thumbs img').parents('#pics-thumbs').prev().css('margin-left',margin_left_value+'px')
			// console.log(margin_left_value+'px')	
		},10)			
		}
		
	})
	lay('#version').html('-v' + laydate.v);

        //执行一个laydate实例
        laydate.render({
            elem: '#from_date1'
        });
        laydate.render({
            elem: '#to_date1' //指定元素,即你要输入的框的id号即可
        });
    lay('#version').html('-v' + laydate.v);

        //执行一个laydate实例
        laydate.render({
            elem: '#from_date2'
        });
        laydate.render({
            elem: '#to_date2' //指定元素,即你要输入的框的id号即可
        });
    lay('#version').html('-v' + laydate.v);

        //执行一个laydate实例
        laydate.render({
            elem: '#from_date3'
        });
        laydate.render({
            elem: '#to_date3' //指定元素,即你要输入的框的id号即可
        });
	
})