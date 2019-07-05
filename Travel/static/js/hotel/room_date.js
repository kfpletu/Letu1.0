window.onload=function(){
	today=$('[name=from_date]').val();
	// console.log(today);
	$('.form').submit(function () {
		if ($(this).find('[name=from_date]').val()>=today && $(this).find('[name=from_date]').val()<$(this).find('[name=to_date]').val()) {
			return true
		}
		alert('时间输入有误,请检查');
		return false

	})
// 	$('#form').submit(function (){
// 		if($('#from_date').val()<$('#to_date').val()&&$('#from_date').val()>=today){
//
// 			return true
// 		}else {
// 			alert('日期有无误,请再检查一下');
// 			return false
// 		}
// })
};