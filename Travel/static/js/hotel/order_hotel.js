$(function(){
	$('#container .form ul li a').click(function(){
		$('.form-third select option').removeAttr('selected')
		for(var i =0 ;i<$('.form-third select option').length;i++){
			if($(this).html()==$('.form-third select option').eq(i).html()){
				$('.form-third select option').eq(i).prop('selected','selected')
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
		$('.brandListBox:first').css('margin-left',(listBoxMarginH+'px'))
		if (listBoxMarginH<-1400) {
			listBoxMarginH=0;
		}
	},100)

	$('.brandListBox:first').mouseover(function(){
		clearInterval(timerH)
	})
	$('.brandListBox:first').mouseout(function(){
		timerH=setInterval(function(){
		listBoxMarginH-=2;	
		$('.brandListBox:first').css('margin-left',(listBoxMarginH+'px'))
		if (listBoxMarginH<-4400){
			listBoxMarginH=0;
		}
	},50)
	})

	var listBoxMarginF=0;
	var timerF=setInterval(function(){
		listBoxMarginF-=2;
		// console.log(listBoxMargin+'px')
		$('.brandListBox:last').css('margin-left',(listBoxMarginF+'px'))
		if (listBoxMarginF<-1400) {
			listBoxMarginF=0;
		}
	},100)

	$('.brandListBox:last').mouseover(function(){
		cursor = 'vertical-text'
		clearInterval(timerF)
	})

	$('.brandListBox:last').mouseout(function(){
		timerF=setInterval(function(){
		listBoxMarginF-=2;	
		$('.brandListBox:last').css('margin-left',(listBoxMarginF+'px'))
		if (listBoxMarginF<-1400) {
			listBoxMarginF=0;
		}
	},100)
	})
	

})