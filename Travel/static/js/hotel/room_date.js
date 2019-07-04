window.onload=function(){

	today=$('[id=from_date1]').val();
	// console.log(today);
	$('.form').submit(function () {
		if ($(this).find('[name=from_data]').val()>=today && $(this).find('[name=from_data]').val()<$(this).find('[name=to_data]').val()) {
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