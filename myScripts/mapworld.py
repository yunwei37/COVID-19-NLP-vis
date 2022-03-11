import time, json
import pandas as pd
from pyecharts.charts import Map
import pyecharts.options as opts
import math

dateId = 20200401

n = "dataSets/countrydata.csv"

def render_mapcountWorld_rate(dateId):
    world_data = pd.read_csv(n)
    world_data = world_data[world_data['dateId'] == dateId]

    #print(world_data)


    world_map = (
        Map()
        .add('', [list(z) for z in zip(world_data['countryFullName'], (world_data['deadCount']*1000 // world_data['confirmedCount'])/10)], 'world')
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
                # 标题
                title_opts=opts.TitleOpts(title="世界疫情分布图(死亡率) "+str(dateId)),
                tooltip_opts=opts.TooltipOpts(formatter='{b}: {c}'),
                # 视觉效果
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                pos_top='center',
                                                pieces=[
                                                    {'min': 40, 'color': '#7f1818'},  #不指定 max
                                                    {'min': 20, 'max': 40},
                                                    {'min': 10, 'max': 20},
                                                    {'min': 8, 'max': 10},
                                                    {'min': 4, 'max': 8},
                                                    {'min': 1, 'max': 4},
                                                    {'min': 0.6, 'max': 1},
                                                    {'min': 0.1, 'max': 0.5},
                                                    {'min': 0, 'max': 0}              
                                                ]),
            )
    )
    return world_map

def render_mapcountWorld_death(dateId):
    world_data = pd.read_csv(n)
    world_data = world_data[world_data['dateId'] == dateId]
    world_data = world_data[['countryFullName', 'deadCount']]

    #print(world_data)


    world_map = (
        Map()
        .add('', [list(z) for z in zip(world_data['countryFullName'], world_data['deadCount'])], 'world')
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
                # 标题
                title_opts=opts.TitleOpts(title="世界疫情分布图(累计死亡人数) "+str(dateId)),
                tooltip_opts=opts.TooltipOpts(formatter='{b}: {c}'),
                # 视觉效果
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                pos_top='center',
                                                pieces=[
                                                    {'min': 100000, 'color': '#7f1818'},
                                                    {'min': 50000, 'max': 99999},
                                                    {'min': 10000, 'max': 49999},
                                                    {'min': 1000, 'max': 9999},
                                                    {'min': 500, 'max': 999},
                                                    {'min': 100, 'max': 499},
                                                    {'min': 10, 'max': 99},
                                                    {'min': 0, 'max': 9} 
                                                ]),
            )
    )
    return world_map

# 中英国名转换函数
def render_mapcountWorld_current(dateId):
    world_data = pd.read_csv(n)
    world_data = world_data[world_data['dateId'] == dateId]
    # 从foreigns中选取 country和confirm 两列
    world_data = world_data[['countryFullName', 'currentConfirmedCount']]

    #print(world_data)


    world_map = (
        Map()
        .add('', [list(z) for z in zip(world_data['countryFullName'], world_data['currentConfirmedCount'])], 'world')
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
                # 标题
                title_opts=opts.TitleOpts(title="世界疫情分布图(现存) "+str(dateId)),
                tooltip_opts=opts.TooltipOpts(formatter='{b}: {c}'),
                # 视觉效果
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                pos_top='center',
                                                pieces=[
                                                    {'min': 1000000, 'color': '#7f1818'},  #不指定 max
                                                    {'min': 500000, 'max': 999999},
                                                    {'min': 100000, 'max': 499999},
                                                    {'min': 50000, 'max': 99999},
                                                    {'min': 10000, 'max': 49999},
                                                    {'min': 1000, 'max': 9999},
                                                    {'min': 500, 'max': 999},
                                                    {'min': 100, 'max': 499},
                                                    {'min': 10, 'max': 99},
                                                    {'min': 0, 'max': 9} 
                                                ]),
            )
    )
    return world_map

def render_mapcountWorld(dateId,type=0):
    if(type==0):
        return render_mapcountWorld_current(dateId)
    elif(type==1):
        return render_mapcountWorld_death(dateId)
    elif(type==2):
        return render_mapcountWorld_rate(dateId)

# 将世界疫情分布图存储进world_map.html
if __name__ == "__main__":
    world_map = render_mapcountWorld(dateId)
    world_map.render('世界疫情地图.html')
