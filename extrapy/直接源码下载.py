import requests
import json
import ssl
import sys
ssl._create_default_https_context = ssl._create_unverified_context 
url = input('请输入链接:')
ges = '.mp4'     #input('输入存储格式:')
#dat = input('编码方案')
#url = 'https://manhua.dmzj.com/update_1.shtml'
#url = sys.argv[1]
#ges = sys.argv[2]
'''
'Cookie':'JSESSIONID=ABAAABAAAIAACBI6377500DAAFABE62ABCE4F22170AFB3E; TG-TRACK-CODE=index_navigation; SEARCH_ID=38a1399372a3402a81acfda2d92c80f5; _ga=GA1.2.635482968.1521958682; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521958682; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521959506; user_trace_token=20180325141801-455ef6db-2ff4-11e8-b62d-5254005c3644; LGSID=20180325141801-455ef7ea-2ff4-11e8-b62d-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20180325143145-307ca3f7-2ff6-11e8-b62d-5254005c3644; LGUID=20180325141801-455efa6d-2ff4-11e8-b62d-5254005c3644; _gid=GA1.2.891178732.1521958682; index_location_city=%E6%88%90%E9%83%BD; X_HTTP_TOKEN=7ee9457e9d8982b4de6e7548e7906713',
    'Referer':'https://www.lagou.com/zhaopin/Java/2/?filterOption=3',
   'Host':'www.lagou.com'
'''
headers = {
   'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
   
}
#print(urllib.request.urlopen(list_d).read().decode('utf-8'))
with open('e:/tes.'+ges,"wb") as f:
    f.write(requests.get(url,headers=headers).content)
print('over')


#'w',encoding='utf-8'
