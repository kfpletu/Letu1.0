window.onload=function(){
	today=$('#from_date').val();
	$('#form').submit(function (){
		if($('#from_date').val()<$('#to_date').val()&&$('#from_date').val()>=today){

			return true
		}else {
			alert('日期有无误,请再检查一下');
			return false
		}
})
};


