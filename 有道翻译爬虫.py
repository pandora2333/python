import traceback
import urllib.request
import urllib.parse
import json
import re
#import random
#iplist = ['119.6.144.73:81', '183.203.208.166:8118', '111.1.32.28:81']
while True:
    content = input("请输入需要翻译的内容(输入‘q’退出程序):")
    if content == 'q':
        break
    '''proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')]
    urllib.request.install_opener(opener)'''
    

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"
    data = {}
    data['action'] = 'FY_BY_REALTIME'
    data['client'] = 'fanyideskweb'
    data['doctype'] = 'json'
    data['from'] = 'AUTO'#日文：zh-CHS
    data['i'] = content
    data['keyfrom'] = 'fanyi.web'
    data['salt']= '1519813015513'#日文翻译号;1519824564479
    data['sign'] = '1dfa101842d6775455e2bf36d13888a0'#日文:973ac8f34448be89a8ebc398190da023
    data['smartresult'] = 'dict'
    data['to'] = 'AUTO'#日文：ja
    data['typoResult'] = 'false'
    data['version'] = '2.1'
    data = urllib.parse.urlencode(data).encode('utf-8')
    try:
        request = urllib.request.Request(url)
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
        response = urllib.request.urlopen(request, data)
        html = response.read().decode('utf-8')
        target = json.loads(html)
        #print(target)
        print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
        print('更多用法;\n')
        print(target['type'])
        dat = input('请输入查询的单词:')
        url2 = 'http://dict.youdao.com/search?q='+dat+'&keyfrom=new-fanyi.smartResult'
        response = urllib.request.urlopen(url2)
        html = response.read().decode('utf-8')
        rex = re.compile(r'(<div class="trans-container">){1}(.+?)(</div>){1}',re.S)
        data2 = re.findall(re.compile(r'<li>(.+?)</li>',re.S),str(re.findall(rex,html)))
        for i in range(10):
            if '</span>' in data2[i]:
                break
            else:
                print(data2[i])
    except SystemExit:
        pass
    except Exception as f:
        print('输入不正确')
        print(f)
