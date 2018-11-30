import requests
import json
import re

# 定义统一的headers
headers = {
   'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
   'Cookie':'BAIDUID=CF1B17D70483556ED88DCC18B6037D80:FG=1; BIDUPSID=CF1B17D70483556ED88DCC18B6037D80; PSTM=1520597942; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[SL8xzxBXZJn]=mk3SLVN4HKm; PSINO=6; H_PS_PSSID=; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; tip_show_limit=1; shituhistory=%7B%220%22%3A%22http%3A%2F%2Ff.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2Fe1fe9925bc315c60090d0cfa81b1cb134954770e.jpg%22%7D; sttbHint=sttbHintShow; Hm_lvt_9a586c8b1ad06e7e39bc0e9338305573=1520598015; Hm_lpvt_9a586c8b1ad06e7e39bc0e9338305573=1520598015',
   
   'Referer':'https://image.baidu.com/'
   
}

# 图片上传
url = 'http://image.baidu.com/pcdutu/a_upload?fr=html5&target=pcSearchImage&needJson=true'
path = input('请输入图片路径:')
files = {
   'file':open(path,'rb')
}
temp_data = json.loads(requests.post(url=url,headers=headers,files=files).text)
# 获得图像识别结果
ans_url = 'http://image.baidu.com/pcdutu?queryImageUrl=' + str(temp_data['url']) +' &querySign' + temp_data['querySign'] + '&fm=home&uptype=upload_pc&result=result_camera'

page_source= requests.get(url=ans_url,headers=headers).text
with open('e:/re.js','w',encoding='utf-8') as f:
   f.write(page_source)
guessWord = re.findall("'guessWord': '(.*?)'",page_source)[0]

term_data = re.findall('"name":"(.*?)","baike":{"url":"(.*?)","abstract":"(.*?)","',page_source,re.S)
#print(len(term_data))
#print(term_data)
# 最终展示
if guessWord:
   print('您上传的图片可能是：',guessWord)
   print('除此之外，他还可能是：')
else:
   print('您上传的图片最可能是:')

for eve in term_data:
    print('名称：',eve[0],'\n描述：',eve[2],'\n百科地址：',eve[1],'\n')
    
input()  
