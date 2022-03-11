import pandas as pd

data = pd.read_csv('dataSets/nCoV_total_p1.csv')

data = data.drop(['微博图片','微博视频','Unnamed: 0.1.1','Unnamed: 0'],axis=1)

data.to_csv('dataSets/nCoV_total_p2.csv')

if __name__ == "__main__":
    pass