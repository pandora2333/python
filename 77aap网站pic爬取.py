""" 
    目标网址：http://www.77aap.com/
    采集需求：获取图片特区下的所有图片
    时间：2018-04-06
    作者：pandora
    版本： v 2.0
"""
# -*- coding: utf-8 -*-


import urllib.request
from lxml import etree
import os  
import time
from multiprocessing import Pool
url_sourse = "http://www.77aap.com"
if os.path.exists("pic_download"):
    os.chdir("pic_download")
else:
    os.mkdir("pic_download")
    os.chdir("pic_download")
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
                with open(dowload_img_name, 'wb') as f:
                    f.write(urllib.request.urlopen(img_list).read())
if __name__ == '__main__':
    list = [
        "article-list-id-6", "article-list-id-7", "article-list-id-8", "article-list-id-9", "article-list-id-10",
        "article-list-id-11", "article-list-id-12", "article-list-id-13"
    ]
    pool = Pool(len(list))
    firstTime = time.time()
    pool.map(pic_download,list)
    pool.close()
    pool.join()
    lastTime = time.time()
    print("over:共计用时 ",str(lastTime-firstTime),"s")




