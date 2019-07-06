$(function(){
	$('#container .form ul li a').click(function(){
		$('#hotel-level option').removeAttr('selected')
		
		for(var i =0 ;i<$('#hotel-level option').length;i++){
			if($(this).html()==$('#hotel-level option').eq(i).html()){
				// console.log($('#hotel-level option').eq(i).html())
				$('#hotel-level option').eq(i).prop('selected',true)
			}
		}

	})
	$('#container .new li a:first').mouseover(function(){
		$('.hotel_figure').css('display','block')
	})
	$('#container .new li a:gt(0)').click(function(){
		$('.hotel_figure').css('display','none')
		var elems =$(".hotel_figure .hotel_name")
		for(var i =0;i<elems.length;i++){
			if($(this).html()==elems.eq(i).html()){
				elems.eq(i).parent().css('display','block')
			}
		}
	})
	var listBoxMarginH=0;
	var timerH=setInterval(function(){
		listBoxMarginH-=2;
		// console.log(listBoxMargin+'px')
		$('#brandListFirst').css('margin-left',(listBoxMarginH+'px'))
		if (listBoxMarginH<-1400) {
			listBoxMarginH=0;
		}
	},100)

	$('#brandListFirst').mouseover(function(){
		clearInterval(timerH)
	})
	$('#brandListFirst').mouseout(function(){
		timerH=setInterval(function(){
		listBoxMarginH-=2;	
		$('#brandListFirst').css('margin-left',(listBoxMarginH+'px'))
		if (listBoxMarginH<-8400){
			listBoxMarginH=0;
		}
	},50)
	})

	var listBoxMarginF=0;
	var timerF=setInterval(function(){
		listBoxMarginF-=2;
		// console.log(listBoxMargin+'px')
		$('#last_brand').css('margin-left',(listBoxMarginF+'px'))
		if (listBoxMarginF<-1400) {
			listBoxMarginF=0;
		}
	},100)

	$('#last_brand').mouseover(function(){
		cursor = 'vertical-text'
		clearInterval(timerF)
	})

	$('#last_brand').mouseout(function(){
		timerF=setInterval(function(){
		listBoxMarginF-=2;	
		$('#last_brand').css('margin-left',(listBoxMarginF+'px'))
		if (listBoxMarginF<-1400) {
			listBoxMarginF=0;
		}
	},100)
	})	

	$('#brandListFirst').load('/hotel/weather/')
	// $.get('/hotel/weather/',function(data){
	// 	alert('new FileReaderSyn')
	// 	$('#brandListFirst').html(data)
	// })


})