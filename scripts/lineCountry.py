# -*- coding: utf-8 -*-
# By: Eastmount CSDN xiuzhang
import time, json, requests
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode

country_name = '美国'


def render_lines(country_name):
    #-------------------------------------------------------------------------------------
    # 第一步：读取数据
    #-------------------------------------------------------------------------------------
    n = "dataSets\\countrydata.csv"
    data = pd.read_csv(n)
    data = data[data['countryName'] == country_name]
    date_list = list(data['dateId'])
    date_list = list(map(lambda x:str(x),date_list))
    confirm_list = list(data['confirmedCount'])
    current_list = list(data['currentConfirmedCount'])
    dead_list = list(data['deadCount'])
    heal_list = list(data['curedCount'])
    print(len(date_list))    
    #print(date_list)                        # 日期
    #print(confirm_list)                     # 确诊数据
    #print(current_list)                     # 疑似数据
    #print(dead_list)                        # 死亡数据
    #print(heal_list)                        # 治愈数据


    #-------------------------------------------------------------------------------------
    # 第二步：绘制折线面积图
    #-------------------------------------------------------------------------------------
    line = (
            Line()
        .add_xaxis(date_list)
        # 平均线 最大值 最小值
        .add_yaxis('确诊数据', confirm_list, is_smooth=True,
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                        opts.MarkPointItem(type_="min")]))
        .add_yaxis('现存确诊数据', current_list, is_smooth=True,
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                        opts.MarkPointItem(type_="min")]))
        .add_yaxis('死亡数据', dead_list, is_smooth=True,
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                        opts.MarkPointItem(type_="min")]))
        .add_yaxis('治愈数据', heal_list, is_smooth=True,
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                        opts.MarkPointItem(type_="min")]))
        # 隐藏数字 设置面积
        .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False))
        # 设置x轴标签旋转角度
        .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)), 
                        yaxis_opts=opts.AxisOpts(name='人数', min_=3), 
                        title_opts=opts.TitleOpts(title='2019-nCoV'+country_name+'疫情数据曲线图'))          
        )


    return line

if __name__ == "__main__":
    render_lines(country_name).render('2019-nCoV'+country_name+'疫情数据曲线图.html')