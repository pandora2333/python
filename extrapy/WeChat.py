import itchat
import os
from itchat.content import *
import re
import requests
import json
import time
from simple import load
import _thread
os.mkdir('req_pics')
os.chdir('req_pics')
@itchat.msg_register([PICTURE])#指定图片
def download_files(msg):
    msg.download(msg.fileName)#下载图片
    num=load('e:/req_pics/'+msg['FileName'])
   # time.sleep(5)
    print(num)
    for i in range(num):
        #print(msg['FromUserName'])
       # _thread.start_new_thread(itchat.send_file,('E:/req_pics/dupic/'+str(i)+'.jpg',msg['FromUserName']))
        time.sleep(0.5)
        #os.remove(msg['FileName'])
itchat.auto_login(hotReload=True)#热登陆
itchat.run()
#time.sleep(5)
print('over')
#str(int(key)-1)+'.jpg'

'''
count=0
    for eve in guessOne:
       try:
          #key =eve.split('=')[1]
          key =str(count)
          with open('E:/py/dupic'+key+'.jpg','wb') as f:
             count+=1
             f.write(requests.get(eve,headers=headers).content)
       except:
          print(eve)
          with open('E:/py/dupic'+str(int(key)-1)+'.jpg','ab') as f:
             count+=1
             f.write(requests.get(eve,headers=headers).content)
'''
''' headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36',
        'Referer':'https://image.baidu.com/'
    }
    url = 'http://image.baidu.com/pcdutu/a_upload?fr=html5&target=pcSearchImage&needJson=true'
    files = {
        'file': open(msg['FileName'], 'rb')
    }
    print(msg['FileName'])
    r = json.loads(requests.post(url, headers=headers, files=files).text)
    ansr_url = 'http://image.baidu.com/pcdutu?queryImageUrl=' + str(r['url']) + '&querySign=' + r[
        'querySign'] + '&fm=home&uptype=upload_pc&result=result_camera'
    page_source = requests.get(ansr_url, headers=headers).text
    guessOne = re.findall('"LargeThumbnailImageUrl":"(.*?)",',page_source)
    print(guessOne)
    #guessOne = re.findall('"LargeThumbnailImageUrl":"(.*?)",',page_source)
   # guessword = re.findall("'guessword':'(.*?)'", page_source[0])
    #print(guessword)r'\"ObjURL":\"http://(.*?)\"',
    #img_url = re.findall('"LargeThumbnailImageUrl":"(.*?)",', page_source)[0:5]
    

'''
