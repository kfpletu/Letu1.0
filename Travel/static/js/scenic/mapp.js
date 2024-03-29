  $(function(){
    // 百度地图API功能
    jingdu=$('#jingdu').html()
    weidu=$('#weidu').html()
    var map = new BMap.Map("allmap");
    map.centerAndZoom(new BMap.Point(jingdu,weidu),12);
    map.enableScrollWheelZoom(true);
    window.map = map;

    //单击获取点击的经纬度
    map.addEventListener("click", function (e) {
        console.log(e.point.lng + "," + e.point.lat);
        var output = "";
        var searchComplete = function (results){
            if (transit.getStatus() != BMAP_STATUS_SUCCESS){
                return ;
            }
            var plan = results.getPlan(0);
                outtime = plan.getDuration(true);  //获取时间
                outs = plan.getDistance(true);  //获取距离
                output += '全程'+outs+' 大约需要'+outtime
        }
        var transit = new BMap.TransitRoute(map, {renderOptions: {map: map},
            onSearchComplete: searchComplete,
            onPolylinesSet: function(){
                setTimeout(function(){$('#map_td').html(output)},"1000");
            }}
        );

        var start=new BMap.Point(e.point.lng,e.point.lat);
        var end = new BMap.Point(jingdu,weidu);
        transit.search(start, end);
    });
}
)


