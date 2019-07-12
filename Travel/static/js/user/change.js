$(function(){
	// alert('fdsfsd')
	$('.fImg input:nth-child(2)').click(function(){
		styleStr =($('[type=file]').val().split('.')).pop()
		// console.log($('[type=file]').val())
		// console.log(($('[type=file]').val().split('.')))
		// console.log(styleStr)
		if (styleStr =='png' || styleStr=='jpg' ||styleStr=='jpeg'){
			return true
		}else {
			alert('请传入正确的图片格式')
			return false
		}
	})

})