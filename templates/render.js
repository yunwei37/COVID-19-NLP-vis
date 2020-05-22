var chart = echarts.init(document.getElementById('bar'), 'white', {renderer: 'canvas'});
var old_data = [];


var worldmap = echarts.init(document.getElementById('worldMap'), 'white', {renderer: 'canvas'});
var chinamap = echarts.init(document.getElementById('chinaMap'), 'white', {renderer: 'canvas'});


$(
    function () {
        fetchbarData(chart);
        fetchworldMapData(worldmap);
        fetchchinaMapData(chinamap)
        setInterval(getDynamicData, 2000);
    }
);

function fetchbarData() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/lineChart",
        dataType: "json",
        success: function (result) {
            chart.setOption(result);
            old_data = chart.getOption().series[0].data;
        }
    });
}

function fetchchinaMapData(chart) {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/chinamap",
        dataType: "json",
        success: function (result) {
            chart.setOption(result);
        }
    });
}

function fetchworldMapData(chart) {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/worldmap",
        dataType: "json",
        success: function (result) {
            chart.setOption(result);
        }
    });
}

function getDynamicData() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/lineDynamicData",
        dataType: "json",
        success: function (result) {
            old_data.push([result.name, result.value]);
            chart.setOption({
                series: [{data: old_data}]
            });
        }
    });
}
