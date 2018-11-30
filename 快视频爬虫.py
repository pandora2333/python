import urllib.request
import json
import re
import socket
import os
socket.setdefaulttimeout(10)
page_num = 1
os.mkdir('kuai')
os.chdir('kuai')
while True:
    list_url = "http://pc.k.360kan.com/pc/list?n=10&p=" + str(page_num) + "&f=json&ajax=1&uid=2a3o0fc71c8bbf9bf72302647c7a63o4&channel_id=13&dl="
    list_data = json.loads(urllib.request.urlopen(list_url).read().decode('utf-8'))['data']['res']
    for eve_data in list_data:
        title = eve_data['t']
        #print(title)
        data_id = re.findall('detail/(.+?)\?',eve_data['u'])[0]
        data_url = "http;//pc.k.360kan.com/pc/play?id="+data_id
        file_url = json.loads(urllib.request.urlopen(data_url).read().decode('utf-8'))['data']['url']
        try:
            with open('kuai/'+title+'.mp4','wb') as f:
                f.write(urllib.request.urlopen(file_url).read())
            print(title)
        except:
            pass
    if len(list_data) >5 and page_num <5:
        page_num = page_num +1
    else:
        break
