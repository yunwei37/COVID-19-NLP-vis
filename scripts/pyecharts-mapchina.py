# -*- coding: utf-8 -*-
import time, json, requests
import pandas as pd
from pyecharts.charts import Map
import pyecharts.options as opts

#-------------------------------------------------------------------------------------
# 第一步：读取数据
#-------------------------------------------------------------------------------------
def render_mapcountChina(dateId):
    n = "dataSets\\china_provincedata.csv"
    data = pd.read_csv(n)
    data = data[data['dateId'] == dateId]
    list_data = zip(list(data['provinceShortName']), list(data['currentConfirmedCount']))
    print(list_data)
    # [('湖北', 48206), ('广东', 1241), ('河南', 1169), ('浙江', 1145), ..., ('澳门', 10), ('西藏', 1)]


    #-------------------------------------------------------------------------------------
    # 第二步：绘制全国疫情地图
    # 参考文章：https://blog.csdn.net/shineych/article/details/104231072 [shineych大神]
    #-------------------------------------------------------------------------------------
    c = (
        Map()
        .add('中国', list_data, 'china')
        .set_global_opts(
            title_opts=opts.TitleOpts(title='全国疫情分布图（现存）'+str(dateId)),
            visualmap_opts=opts.VisualMapOpts(is_show=True,
                                            split_number=6,
                                            is_piecewise=True,  # 是否为分段型
                                            pos_top='center',
                                            pieces=[
                                                {'min': 10000, 'color': '#7f1818'},  #不指定 max
                                                {'min': 1000, 'max': 10000},
                                                {'min': 500, 'max': 999},
                                                {'min': 100, 'max': 499},
                                                {'min': 10, 'max': 99},
                                                {'min': 0, 'max': 9} ],                                              
                                            ),
        )
    )
    return c

if __name__ == "__main__":
    render_mapcountChina(20200212).render('全国疫情地图.html')