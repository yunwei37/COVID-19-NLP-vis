# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import codecs
import pandas as pd
import datetime
import os
import jieba
import jieba.analyse
import multiprocessing
import time

def convertDate(t):
    td = datetime.datetime.strptime(t,"%m月%d日 %H:%M")
    return td.strftime("%d"),td.strftime("%m")

def convertTime(t):
    td = datetime.datetime.strptime(t,"%m月%d日 %H:%M")
    return td.strftime("%H%M")

#处理从百分之多少到百分之多少的数据
def processData(source,destination,start=0,end=100):
    data = pd.read_csv(source)
    x = data.shape[0]/100
    print(x)
    data = data.iloc[int(start*x):int(end*x),]
    data['day'] = None
    data['month'] = None
    data['sentiments'] = None
    for i in range(4):
        data['keyword'+str(i)] = None
    for i in range(int(start*x),int(end*x)):
        doc = str(data.loc[i,'微博中文内容'])
        t = data.loc[i,'微博发布时间']
        s = SnowNLP(doc)

        if(i%100==0):
            print(i)

        tags = jieba.analyse.extract_tags(doc, topK=4)
        ki = 0 
        for tag in tags:
            data.loc[i,'keyword'+str(ki)] = tag
            ki=ki+1
        data.loc[i,'微博发布时间'] = convertTime(t)
        data.loc[i,'sentiments'] = s.sentiments - 0.5
        data.loc[i,'day'],data.loc[i,'month'] = convertDate(t)
    data.to_csv(destination)

if __name__ == "__main__":
    p = []
    t = time.time()
    print(t)
    #processData('nCov_10k_test.csv','nCoV_test.csv')

    for i in range(10):
        p.append(multiprocessing.Process(target=processData,args=('dataSets/nCoV_total.csv','dataSets/nCoV_test'+str(i)+'.csv',i*10,(i+1)*10)))
    for i in range(10):
        p[i].start()
    for i in range(10):
        p[i].join()
    
    print('merging')
    df1 =  pd.read_csv('dataSets/nCoV_test0.csv')
    for i in range(1,10):
        df2 = pd.read_csv('dataSets/nCoV_test'+str(i)+'.csv') 
        df1 = pd.concat([df1,df2],axis=0,ignore_index=True)  #将df2数据与df1合并
    df1 = df1.reset_index(drop=True) #重新生成index
    print(df1.shape)
    df1.to_csv('dataSets/nCoV_total_p.csv') #将结果保存为新的csv文件
    for i in range(10):
        os.remove('dataSets/nCoV_test'+str(i)+'.csv')
    t1 = time.time()
    print(t1)
    print("second: "+str(t1-t))
    #processData('dataSets\\nCoV_total.csv','dataSets\\nCoV_total_process.csv')
    #processData('dataSets\\nCov_10k_test.csv','dataSets\\nCoV_test.csv')