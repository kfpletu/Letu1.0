$(function () {
    $('#d1').click(function () {
        var aa = $('#from_city').val();
        // $('#from_city').val($('#to_city').val())
        // $('#to_city').val(aa);
        var bb=$('#to_city').val();
        // console.log(aa,bb);
        $('#from_city').val(bb);
        $('#to_city').val(aa);
    });
    $('.aa').click(function () {
        // console.log("11");
        var cc=$(this).html();
        // console.log(cc);
        $('#to_city').val(cc);
    });

});
function func() {
    if ($("#from_city").val()==''){
        alert("请输入出发城市");
        return false;
    }
    if ($("#to_city").val()==''){
        alert("请输入到达城市");
        return false;
    }
    if ($("#from_date").val()==''){
        alert("请输入出发时间");
        return false;
    }
    if ($("#to_date").val()==''){
        alert("请输入返回时间");
        return false;
    }
}