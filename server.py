from random import randrange

from flask.json import jsonify
from flask import Flask, render_template
from flask import request

import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import Line

from scripts.mapchina import render_mapcountChina
from scripts.mapworld import render_mapcountWorld
from scripts.lineCountry import render_lines
from scripts.jiebafenci import render_wordcloud

# map time index
i = 45

# map type 
maptype = 0

n = "dataSets\\countrydata.csv"
data = pd.read_csv(n)
date_list = list(data[data['countryName'] == '中国']['dateId'])
countrylist = list(data[data['dateId'] == 20200412]['countryName'])
countrylist = ['中国']+countrylist
#print(date_list)
#print(countrylist)

selectCountry = '中国'

app = Flask(__name__, static_folder="templates")

@app.route("/")
def index():
    return render_template("index.html",cates = countrylist)

@app.route("/document")
def document():
    return render_template("README.html")


@app.route("/worldmap")
def get_world_map():
    return render_mapcountWorld(date_list[int(i)],maptype).dump_options_with_quotes()


@app.route("/chinamap")
def get_china_map():
    return render_mapcountChina(date_list[int(i)],maptype).dump_options_with_quotes()

@app.route("/lines")
def get_line_chart():
    return render_lines(selectCountry).dump_options_with_quotes()

@app.route("/wordcloud",methods=['POST', 'GET'])
def get_word_chart():
    if request.method == 'GET':
        i = request.args.get('value', '')
        if not i:
            i = 0
        print(i)
        return render_wordcloud(i).dump_options_with_quotes()

@app.route('/changecountry',methods=['POST', 'GET'])
def changeCountry():
    if request.method == 'GET':
        global selectCountry
        selectCountry = request.args.get('value', '')
        print(selectCountry)
        return render_lines(selectCountry).dump_options_with_quotes()

@app.route('/changemap',methods=['POST', 'GET'])
def changeMapType():
    if request.method == 'GET':
        global maptype
        maptype = int(request.args.get('value', ''))
        print(maptype)
        return render_mapcountWorld(date_list[int(i)],maptype).dump_options_with_quotes()

@app.route('/changedate',methods=['POST', 'GET'])
def changeDate():
    if request.method == 'GET':
        global i
        i = request.args.get('value', '')
        print(i)
        print(date_list[int(i)])
        return render_mapcountWorld(date_list[int(i)],maptype).dump_options_with_quotes()

if __name__ == "__main__":
    app.run()