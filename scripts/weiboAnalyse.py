import psycopg2
conn = psycopg2.connect(database="hw8", user="postgres", password="postgres", host="127.0.0.1", port="5432")
print("Opened database successfully" )

cur = conn.cursor()
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
from pyecharts.globals import CurrentConfig, NotebookType
import pandas as pd
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode


def generateData():
    results = []
    for d in range(1,32):
        m = 1
        query = """
        with weibo_d as(
            select * from weibo where day = %d and month = %d
        )
        select k0.keyword, k0.c+k1.c+k2.c+k3.c as c from 
        (select keyword0 keyword,count(*) c from weibo_d group by keyword0) k0,
        (select keyword1 keyword,count(*) c from weibo_d group by keyword1) k1,
        (select keyword2 keyword,count(*) c from weibo_d group by keyword2) k2,
        (select keyword3 keyword,count(*) c from weibo_d group by keyword3) k3
        where k0.keyword = k1.keyword and k2.keyword = k1.keyword and k2.keyword = k3.keyword and k1.keyword != '##'
        order by c desc limit 50;
        """%(d,m)
        cur.execute(query)
        rows = cur.fetchall()
        results.append(((m,d),rows))
        print(rows)


    for d in range(1,19):
        m = 2
        query = """
        with weibo_d as(
            select * from weibo where day = %d and month = %d
        )
        select k0.keyword, k0.c+k1.c+k2.c+k3.c as c from 
        (select keyword0 keyword,count(*) c from weibo_d group by keyword0) k0,
        (select keyword1 keyword,count(*) c from weibo_d group by keyword1) k1,
        (select keyword2 keyword,count(*) c from weibo_d group by keyword2) k2,
        (select keyword3 keyword,count(*) c from weibo_d group by keyword3) k3
        where k0.keyword = k1.keyword and k2.keyword = k1.keyword and k2.keyword = k3.keyword and k1.keyword != '##'
        order by c desc limit 50;
        """%(d,m)
        cur.execute(query)
        rows = cur.fetchall()
        results.append(((m,d),rows))
        print(rows)
    
    return results

def generateSentimentsline():
    query="select month ||'-'|| day as time, avg(sentiments) from weibo group by day,month order by month,day;"
    cur.execute(query)
    rows = cur.fetchall()   
    date_list = []
    s_list = []
    for row in rows:
        date_list.append(row[0])
        s_list.append(row[1])
    line = (
        Line()
        .add_xaxis(date_list)
        # 平均线 最大值 最小值
        .add_yaxis('sentiments', s_list, is_smooth=True,
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                        opts.MarkPointItem(type_="min")]))
        # 隐藏数字 设置面积
        .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False))
        # 设置x轴标签旋转角度
        .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)), 
                        yaxis_opts=opts.AxisOpts(name='sentiments', min_=0), 
                        title_opts=opts.TitleOpts(title='微博情感分析每日平均值'))          
        )
    line.render("微博情感分析每日平均值.html")


# dateId: 0-50
def weiboWordcloud(dateId):
    from scripts.weiboWordData import date_data
    words = date_data[int(dateId)][1]
    c = (
        WordCloud()
        .add("", words, word_size_range=[20, 100], shape=SymbolType.ROUND_RECT)
        .set_global_opts(title_opts=opts.TitleOpts(title='全国新型冠状病毒疫情词云图'))
    )
    return c

if __name__ == "__main__":
    generateSentimentsline()

"""    results = generateData()
    with open("weiboWordData.py",'w',encoding='utf-8') as f:
        f.write("date_data="+str(results))
        f.close()"""
