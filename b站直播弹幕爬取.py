import urllib.request
import urllib.parse
import time
import json
roomid = input('请输入房间号:')
url = 'https://api.live.bilibili.com/ajax/msg'
dat = {'roomid':roomid,
       'token':'',
       'carf_token':''}
data = urllib.parse.urlencode(dat).encode('utf-8')
req = urllib.request.Request(url,data)

asd =[]
while True:
    html1 = urllib.request.urlopen(req)
    html2 = urllib.request.urlopen(req)
    time.sleep(2)
    
    dan1 = json.loads(html1.read().decode('utf-8'))
    try:
        asd1 = list(map(lambda i :dan1['data']['room'][i]['text'],range(10)))
        print(asd1.pop())
    except:
        pass
    '''time.sleep(2)
    
    dan2 = json.loads(html2.read().decode('utf-8'))
    asd2 = list(map(lambda i :dan2['data']['room'][i]['text'],range(5)))
    #asd3 = [i for i in asd2 and i not in asd1]
    try:
        for i in list(set(asd1+asd2)):
            if i not in asd:
                asd.append(i)   
                print(asd.pop())
    except:
        pass

    '''
