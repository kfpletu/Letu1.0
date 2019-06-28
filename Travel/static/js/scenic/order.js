$(function (){

//	1.数量增减
	$(".add").click(function (){
		//获取前一个兄弟元素（输入框）的值
		var value = $(this).prev().val();
		value++;
		$(this).prev().val(value);
		countPrice($(this),value);
		sum();
	
	})
	$(".minus").click(function (){
		var value = $(this).next().val();
		if(value > 1){
			value--;
		}
		$(this).next().val(value);
		countPrice($(this),value)
		sum()

	})
	//价格联动
	function countPrice(that,value){
		//价格联动 单价*数量，修改总金额
		var str = that.parents(".item").find(".gprice p").html();
		var price = str.substring(2);//"299.00"
		var sum = price * value;
		sum = sum.toFixed(2);
		that.parent().next().html("￥ "+sum);
	
	}

})