import datetime as dt  
import matplotlib as mpl  
import matplotlib.dates as mdate  
import matplotlib.pyplot as plt  
from matplotlib.ticker import MultipleLocator  
from matplotlib.ticker import FormatStrFormatter  
import csv  
#import numpy as np  
#import pandas as pd  
  
date2num = mdate.strpdate2num('%Y-%m-%d')  
x = []  
y = []  
y1 =[]  
y2 =[]  
y3 =[]  
y4 =[]  
y5 =[]  
with open("e:/66001.txt",'r') as csvfile:  
    rows = csv.reader(csvfile, delimiter=',')  
    for row in rows:  
        #print row  
        x.append(date2num(row[0]))  
        y.append(float(row[1]))  
        y1.append(float(row[2]))  
        y2.append(float(row[3]))  
        y3.append(float(row[4]))  
        y4.append(float(row[5]))  
        y5.append(float(row[6]))  
#  
# 加这个两句 可以显示中文  
mpl.rcParams['font.sans-serif'] = [u'SimHei']  
mpl.rcParams['axes.unicode_minus'] = False  
  
fig = plt.figure(figsize=(12,6)) # 1200x600  
fig.autofmt_xdate()        # 设置x轴时间外观  
ax1 = fig.add_subplot(1,1,1)  
autodate = mdate.AutoDateLocator()  
ax1.xaxis.set_major_locator(autodate)  # 设置时间间隔  
# 设置时间标签显示格式  
dateFmt = mdate.DateFormatter('%y%m%d')  
ax1.xaxis.set_major_formatter(dateFmt)  
# 将x轴次刻度标签设置为61的倍数  
xminorLocator = MultipleLocator(61)  
# 显示次刻度标签的位置,没有标签文本  
ax1.xaxis.set_minor_locator(xminorLocator)
#ax1.set_xticks() # 设置x轴间隔    
ax1.set_xlim(date2num('2012-01-01'),date2num('2017-09-30')) # 设置x轴范围  
#plt.xticks(pd.date_range('2012-01-01','2017-09-30'))  
plt.xticks(rotation=90) # 显示日期旋转90度   
plt.title(u'基金净值图')  
plt.plot(x,y, label='660010')  
plt.plot(x,y1,label='660011')  
plt.plot(x,y2,label='660012')  
plt.plot(x,y3,label='660013')  
plt.plot(x,y4,label='660014')  
plt.plot(x,y5,label='660015')  
plt.grid(True)  
plt.xlabel(u'日期')  
plt.ylabel(u'净值')  
plt.legend(loc=2,prop={'family':'SimHei','size':12}) # loc=2 : upper left  
plt.savefig("e:/66001.png", dpi=100)  
#plt.show()  
