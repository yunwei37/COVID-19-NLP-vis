from random import randrange

from flask.json import jsonify
from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Line

from scripts.mapchina import render_mapcountChina
from scripts.mapworld import render_mapcountWorld
from scripts.lineCountry import render_lines

app = Flask(__name__, static_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/document")
def document():
    return render_template("README.html")


@app.route("/worldmap")
def get_world_map():
    return render_mapcountWorld(20200312).dump_options_with_quotes()


@app.route("/chinamap")
def get_china_map():
    return render_mapcountChina(20200315).dump_options_with_quotes()

@app.route("/lines")
def get_line_chart():
    return render_lines('中国').dump_options_with_quotes()


if __name__ == "__main__":
    app.run()