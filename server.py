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

i = 45

n = "dataSets\\countrydata.csv"
data = pd.read_csv(n)
data = data[data['countryName'] == '中国']
date_list = list(data['dateId'])

app = Flask(__name__, static_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/document")
def document():
    return render_template("README.html")


@app.route("/worldmap")
def get_world_map():
    return render_mapcountWorld(date_list[int(i)]).dump_options_with_quotes()


@app.route("/chinamap")
def get_china_map():
    return render_mapcountChina(date_list[int(i)]).dump_options_with_quotes()

@app.route("/lines")
def get_line_chart():
    return render_lines('中国').dump_options_with_quotes()

@app.route('/changedate',methods=['POST', 'GET'])
def changeDate():
    if request.method == 'GET':
        global i
        i = request.args.get('value', '')
        print(i)
        print(date_list[int(i)])
        return render_mapcountWorld(date_list[int(i)]).dump_options_with_quotes()

if __name__ == "__main__":
    app.run()