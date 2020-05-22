import time, json, requests
import pandas as pd
from pyecharts.charts import Map
import pyecharts.options as opts

dateId = 20200401

# 中英国名转换函数
def render_mapcountWorld(dateId):
    world_data = pd.read_csv("dataSets\countrydata.csv")
    world_data = world_data[world_data['dateId'] == dateId]
    # 从foreigns中选取 country和confirm 两列
    world_data = world_data[['countryFullName', 'currentConfirmedCount']]

    print(world_data)


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


# 将世界疫情分布图存储进world_map.html
if __name__ == "__main__":
    world_map = render_mapcountWorld(dateId)
    world_map.render('世界疫情地图.html')
