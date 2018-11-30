import requests  #网络请求
import re
import time
import random
import pandas as pd #数据框操作
import  numpy as np #数据分析
import  matplotlib.pyplot as plt #绘图
import jieba #分词
import matplotlib as mpl #配置字体
from pyecharts import Geo #地理图
mpl.rcParams['font.sans-serif']=['Microsoft YaHei']
#配置字体风格
plt.rcParams['axes.labelsize']=16.
plt.rcParams['xtick.labelsize']=14.
plt.rcParams['ytick.labelsize']=14.
plt.rcParams['legend.fontsize']=12.
plt.rcParams['figure.figsize']=[15.,15.]
#post的网址
url = 'https://www.lagou.com/jobs/companyAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false&isSchoolJob=0'
#http://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0
#https://www.lagou.com/jobs/companyAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false&isSchoolJob=0
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    'Referer':'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=',
    'Cookie':'JSESSIONID=ABAAABAAAIAACBI6377500DAAFABE62ABCE4F22170AFB3E; TG-TRACK-CODE=index_navigation; SEARCH_ID=48ad09a5f34d4d6680271f8bd836a1ec; _ga=GA1.2.635482968.1521958682; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521958682; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521961551; user_trace_token=20180325141801-455ef6db-2ff4-11e8-b62d-5254005c3644; LGSID=20180325141801-455ef7ea-2ff4-11e8-b62d-5254005c3644; LGRID=20180325150550-f35b0ea7-2ffa-11e8-b62d-5254005c3644; LGUID=20180325141801-455efa6d-2ff4-11e8-b62d-5254005c3644; _gid=GA1.2.891178732.1521958682; index_location_city=%E6%88%90%E9%83%BD; X_HTTP_TOKEN=7ee9457e9d8982b4de6e7548e7906713',
}
'''for n in range(30):
    form = {'first':'false',
            'kd':'Python',
            'pn':str(n)
            }
    time.sleep(random.randint(2,5))
    html = requests.post(url,data=form,headers=headers)
    data = re.findall('{"companyId":.*?,"positionName":"(.*?)","workYear":"(.*?)","education":"(.*?)","jobNature":"(.*?)".*',html)'''
data= {'都市':'成都'}
data = pd.DataFrame(data)
data.to_csv('e:/test.csv',header=False,index=False,mode='a+')
data = pd.read_csv('e:/豆瓣top250.csv',encoding='gbk')
data.head()
data['评分'].value_counts().plot(kind='barh',rot=0)
plt.show()

