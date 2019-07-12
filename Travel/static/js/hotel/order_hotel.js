$(function(){
	//搜索框住宿类型
	$('#container .form ul li a').click(function(){
		$('#hotel-level option').removeAttr('selected')
		
		for(var i =0 ;i<$('#hotel-level option').length;i++){
			if($(this).html()==$('#hotel-level option').eq(i).html()){
				// console.log($('#hotel-level option').eq(i).html())
				$('#hotel-level option').eq(i).prop('selected',true)
			}
		}

	})

	//天气预报栏
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


	//底部酒店品牌
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
	
	//酒店列表
	$.get(
		'/hotel/hotel-list',
		function(hotels){
			var html=''
			html+='<li>热门品牌：</li>'
			for (var i = 0; i < hotels.length; i++) {			
				html+=' <li><a href='+hotels[i].pk +'>'
				html+=hotels[i].fields.hotel_name
				html+='</a></li>'			
				if(i==5){			
					break;
				}			
			}
			$('#all_hotel_name').html(html)
			html=''
			var hotel_level_list=['','快速便捷','民宿公寓','星级酒店','主题酒店']
			$(hotels).each(function(i,hotel){
				hotel_index=Number(hotel.fields.hotel_p.charAt())
				html+=	'<figure class="hotel_figure">'
				html+=	'<img src="/static/images/hotel/'
				html+=  hotel.fields.hotel_p
				html+='/11.png" alt="The Pulpit Rock" class="hotel_img"> '
                html+=  '<span class="hotel_name">'  
                html+=hotel.fields.hotel_name
                html+='</span> '    
                html+= hotel_level_list[hotel_index] 
                html+=  '<a href=" '+hotel.pk +'">点击进入</a> '
				html+=  '</figure>'

			})
			$('.hotel_imfor').html(html)	
		},'json'
	);
	$('#all_hotel_name').mouseover(function(){
		console.log('111111')
		$(this).next().find().css('display','block')
	})



	// $('#all_hotel_name:first-child').mouseover(function(){
	// 	console.log('1111')
	// 	$('.hotel_figure').css('display','block')
	// });

	// $('#container .new li a:gt(0)').click(function(){
	// 	console.log('1111')
	// 	$('.hotel_figure').css('display','none')
	// 	var elems =$(".hotel_figure .hotel_name")
	// 	for(var i =0;i<elems.length;i++){
	// 		if($(this).html()==elems.eq(i).html()){
	// 			elems.eq(i).parent().css('display','block')
	// 		}
	// 	}
	// });

})