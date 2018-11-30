""" 
    目标网址：http://www.77aap.com/
    采集需求：获取图片特区下的所有图片
    时间：2018-04-06
    作者：pandora
    版本： v 3.0
"""
# -*- coding: utf-8 -*-


import urllib.request
from lxml import etree
import os
import _thread
from tkinter import *
import  time
import socket
#socket.setdefaulttimeout = 50
url_sourse = "http://www.77aap.com"
if os.path.exists("pic_download"):
    os.chdir("pic_download")
else:
    os.mkdir("pic_download")
    os.chdir("pic_download")

root = Tk(className="图片下载简单界面")
Label(root, text='请不要到处散播，仅供学习使用！！否者一切责任都由阁下承担，谢谢！！！').grid(row=0, column=0)

def show():
    list = [
        "article-list-id-6", "article-list-id-7", "article-list-id-8", "article-list-id-9", "article-list-id-10",
        "article-list-id-11", "article-list-id-12", "article-list-id-13"
    ]
    for i in range(len(list)):
        try:
            _thread.start_new_thread(pic_download,(list[i],))
            time.sleep(1)
        except:
            pass
    global v1
    if i== len(list)-1:
        v1.set( "多线程部署就位")
def pic_download(list_id):
    url_now = url_sourse + "/" + list_id + ".html"
    # 获取当前页面数据
    page_html = urllib.request.urlopen(url_now).read().decode("utf-8")
    # 获取标签页中总数
    num_max = int(etree.HTML(page_html).xpath('//*[@class="end"]/text()')[0])

    for eve_content_list_page in range(1, num_max + 1):
        url = url_sourse + "/" + list_id + "-page-" + str(eve_content_list_page) + ".html"
        eve_list_page = urllib.request.urlopen(url).read().decode("utf-8")
        # 页面标签
        content_list = etree.HTML(eve_list_page).xpath('//ul[@class="textList"]/li/a/@href')
        for eve_content in content_list:
            content_url = url_sourse + eve_content
            content_page_html = urllib.request.urlopen(content_url).read().decode("utf-8")
            dowload_img_url = etree.HTML(content_page_html).xpath('//div[@class="picContent"]/img/@src')
            for img_list in dowload_img_url:
                dowload_img_name = img_list.split('/')[-1]
                try:
                    with open(dowload_img_name, 'wb') as f:
                        f.write(urllib.request.urlopen(img_list).read())
                except:
                    pass
v1=StringVar()
v1.set("pic_download目录下查看")
e1=Entry(root,textvariable=v1)
e1.grid(row=0,column=1,padx=10,pady=5)
Button(root, text='点击就下', width=10, command=show).grid(row=3, column=0, sticky='w', padx=10, pady=5)
Button(root,text='退出',width=10,command=root.quit).grid(row=3,column=1,sticky='e',padx=10,pady=5)

mainloop()







