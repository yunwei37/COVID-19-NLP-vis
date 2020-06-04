


var worldmap = echarts.init(document.getElementById('worldMap'), 'white', {renderer: 'canvas'});
var chinamap = echarts.init(document.getElementById('chinaMap'), 'white', {renderer: 'canvas'});
var lineChart = echarts.init(document.getElementById('lines'), 'white', {renderer: 'canvas'});
var wordchart = echarts.init(document.getElementById('wordcloud'), 'white', {renderer: 'canvas'});
var weibochart = echarts.init(document.getElementById('weibocloud'), 'white', {renderer: 'canvas'});

var slider = document.getElementById('slider');

document.getElementById('slider').onchange =  function changeDate(){
    fetchworldMapData(worldmap);
    fetchchinaMapData(chinamap);
}

document.getElementById('selectCountrys').onchange = function changeCountry(){
    $.ajax({
        type: "GET",
        url: "/changecountry",
        dataType: "json",
        data:  "value="+document.getElementById('selectCountrys').value,
        success: function (result) {
            lineChart.setOption(result);
        }
    });
}

document.getElementById('mapselecter').onchange = function changeCountry(){
    fetchworldMapData(worldmap);
    fetchchinaMapData(chinamap);
}

document.getElementById('sliderWord').onchange = function changeWordCloud(){
    $.ajax({
        type: "GET",
        url: "/wordcloud",
        dataType: "json",
        data:  "value="+document.getElementById('sliderWord').value,
        success: function (result) {
            wordchart.setOption(result);
        }
    });
}

document.getElementById('sliderWeibo').onchange = function changeWeiboCloud(){
    $.ajax({
        type: "GET",
        url: "/weiboCloud",
        dataType: "json",
        data:  "value="+document.getElementById('sliderWeibo').value,
        success: function (result) {
            weibochart.setOption(result);
        }
    });
}

$(
    function () {
        fetchworldMapData(worldmap);
        fetchchinaMapData(chinamap);
        fetchlineData(lineChart)
        $.ajax({
            type: "GET",
            url: "/wordcloud",
            dataType: "json",
            success: function (result) {
                wordchart.setOption(result);
            }
        });
        $.ajax({
            type: "GET",
            url: "/weiboCloud",
            dataType: "json",
            success: function (result) {
                weibochart.setOption(result);
            }
        });
    }
);

function fetchchinaMapData(chart) {
    $.ajax({
        type: "GET",
        url: "/chinamap",
        dataType: "json",
        data:  "type="+document.getElementById('mapselecter').value+'&'+"index="+document.getElementById('slider').value,
        success: function (result) {
            chart.setOption(result);
        }
    });
}

function fetchlineData(chart) {
    $.ajax({
        type: "GET",
        url: "/lines",
        dataType: "json",
        success: function (result) {
            chart.setOption(result);
        }
    });
}

function fetchworldMapData(chart) {
    $.ajax({
        type: "GET",
        url: "/worldmap",
        dataType: "json",
        data:  "type="+document.getElementById('mapselecter').value+'&'+"index="+document.getElementById('slider').value,
        success: function (result) {
            chart.setOption(result);
        }
    });
}


