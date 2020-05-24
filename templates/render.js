


var worldmap = echarts.init(document.getElementById('worldMap'), 'white', {renderer: 'canvas'});
var chinamap = echarts.init(document.getElementById('chinaMap'), 'white', {renderer: 'canvas'});
var lineChart = echarts.init(document.getElementById('lines'), 'white', {renderer: 'canvas'});
var wordchart = echarts.init(document.getElementById('wordcloud'), 'white', {renderer: 'canvas'});

var slider = document.getElementById('slider');

document.getElementById('slider').onchange =  function changeDate(){
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/changedate",
        dataType: "json",
        data:  "value="+document.getElementById('slider').value,
        success: function (result) {
            worldmap.setOption(result);
        }
    });
    fetchchinaMapData(chinamap);
}

document.getElementById('selectCountrys').onchange = function changeCountry(){
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/changecountry",
        dataType: "json",
        data:  "value="+document.getElementById('selectCountrys').value,
        success: function (result) {
            lineChart.setOption(result);
        }
    });
}

document.getElementById('sliderWord').onchange = function changeWordCloud(){
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/wordcloud",
        dataType: "json",
        data:  "value="+document.getElementById('sliderWord').value,
        success: function (result) {
            wordchart.setOption(result);
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
            url: "http://127.0.0.1:5000/wordcloud",
            dataType: "json",
            success: function (result) {
                wordchart.setOption(result);
            }
        });
    }
);

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

function fetchlineData(chart) {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/lines",
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


