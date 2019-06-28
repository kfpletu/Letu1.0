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
        $('#from_city').val(cc);
    });

});