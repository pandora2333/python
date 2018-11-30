import urllib.request
import re
import os
def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48')
    response=urllib.request.urlopen(req)
    html=response.read().decode('UTF-8')
    return html
def get_img(html):
    print("开始爬取。。")
    p=r'<img class="BDE_Image" src="([^"]+\.jpg)" '
    #p=r'<img style=".+?" src="(.+\.jpg)"'
    #print(html)
    os.mkdir('pic')
    os.chdir('pic')
    imglist=re.findall(p,html)
    for each in imglist:
        #print(each)
        #print("循环测试。")
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each,filename,None)
        #print(filename)
        
if __name__=='__main__':
    url='http://tieba.baidu.com/p/3563409202'
    #url='http://jandan.net/ooxx/page-60#comments'
    get_img(url_open(url))
    print("结束。。")
    
