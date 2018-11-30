
import re
from numba import jit
import requests
import os
import traceback
@jit
def get_url(url,headers):

    response = requests.get(url,headers=headers)

    return response.text

@jit
def get_img_page(html):

    pattern = re.compile('<figure.*?href="(.*?)".*?</figure>',re.S)

    items = re.findall(pattern,html)

    return items

@jit
def parse_img_page(item):

    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400",'Referer':'http://m.mzitu.com/'}
    

    img_url = get_url(item,headers)

    pattern = re.compile('<figure.*?src="(.*?)".*?</figure>',re.S)

    dow_addr = re.findall(pattern,img_url)
    return dow_addr[0]

def save_img(dow_addr,headers,path2):
    response = requests.get(dow_addr,headers=headers)
    filename = dow_addr.split('/')[-1]
    with open(path2+filename,'wb') as f:
        f.write(response.content)
        f.close()


def main():

    #img_urls = get_url()

    #for img_url in img_urls:
        pass


if __name__ == '__main__':
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400"}
    path2 = input("请输入存储路径(请不要创建已经存在的文件夹):")
    try:
        os.mkdir(path2)
        url = 'http://m.mzitu.com/'
        html = get_url(url,headers)
        items = get_img_page(html)
        #print(items)
        for item in items:
            for i in range(1,35):
                img_addr = item + str('/') + str(i)
                #print(img_addr)
                dow_addr = parse_img_page(img_addr)
                #header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400",'Referer':'http://m.mzitu.com/'}
                headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",'Referer':img_addr}

                save_img(dow_addr,headers,path2)
                print('第'+str(i)+'页的图正在存储','请到',path2,'路径下查看图片')
        print('全部存储完毕','请到',path2,'路径下查看图片')
    except SystemExit:
        pass
    except FileExistsError:
        print('文件夹已经存在')
    except FileNotFoundError:
        print('文件夹错误')
    except:
        print('内部错误请重试或者你已经中断下载')
    input()
