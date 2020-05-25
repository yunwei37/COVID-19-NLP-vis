
import pandas as pd

def merge_orgin():
    df1 = pd.read_csv('dataSets\\nCov_10k_test.csv')  #读取首个csv文件，保存到df1中
    df1 = df1[['微博id','微博发布时间','发布人账号','微博中文内容','微博图片','微博视频']]


    df2 = pd.read_csv('dataSets\\nCoV_100k_train.labled.csv')  #打开csv文件，注意编码问题，保存到df2中
    df2 = df2[['微博id','微博发布时间','发布人账号','微博中文内容','微博图片','微博视频']]
    df1 = pd.concat([df1,df2],axis=0,ignore_index=True)  #将df2数据与df1合并

    df3 = pd.read_csv('dataSets\\nCoV_900k_train.unlabled.csv')  #打开csv文件，注意编码问题，保存到df2中
    df3 = df3[['微博id','微博发布时间','发布人账号','微博中文内容','微博图片','微博视频']]
    df1 = pd.concat([df1,df3],axis=0,ignore_index=True)  #将df2数据与df1合并


    df1 = df1.reset_index(drop=True) #重新生成index
    print(df1.shape)
    df1.to_csv('dataSets\\nCoV_total.csv') #将结果保存为新的csv文件

def process_pp():
    df = pd.read_csv("dataSets\\nCoV_total_p.csv")
    df = df.drop(['Unnamed: 0','Unnamed: 0.1', 'summary'], axis=1)
    df.to_csv('dataSets\\nCoV_total_p1.csv') 
    
if __name__ == "__main__":
    process_pp()