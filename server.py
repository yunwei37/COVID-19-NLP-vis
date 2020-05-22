from random import randrange

from flask.json import jsonify
from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Line

from scripts.mapchina import render_mapcountChina
from scripts.mapworld import render_mapcountWorld


app = Flask(__name__, static_folder="templates")


def line_base() -> Line:
    line = (
        Line()
        .add_xaxis(["{}".format(i) for i in range(10)])
        .add_yaxis(
            series_name="",
            y_axis=[randrange(50, 80) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="动态数据"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/document")
def document():
    return render_template("README.html")

@app.route("/lineChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()

@app.route("/worldmap")
def get_world_map():
    return render_mapcountChina(20200212).dump_options_with_quotes()

@app.route("/chinamap")
def get_china_map():
    return render_mapcountWorld(20200301).dump_options_with_quotes()

idx = 9


@app.route("/lineDynamicData")
def update_line_data():
    global idx
    idx = idx + 1
    return jsonify({"name": idx, "value": randrange(50, 80)})


if __name__ == "__main__":
    app.run()