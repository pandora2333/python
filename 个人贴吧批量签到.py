import urllib.request
import urllib.parse
import re
import json
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    'Cookie':'H_PS_PSSID=; FP_UID=8153df78ebe8d18cbcbe32931c446a43; BAIDUID=B2CA1E44FC00772F90617A219DBA8F7C:FG=1; BIDUPSID=B2CA1E44FC00772F90617A219DBA8F7C; PSTM=1521020470; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDUSS=VhnWXFVVlFVdHh1MW5YN25DTWJ6Wk9LMFM4eXNKdnk0M29VampvMThCQ1BlOUJhQVFBQUFBJCQAAAAAAAAAAAEAAACAQl5L0OnO3tau0P7S9AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI~uqFqP7qhaM; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1521021618; 1264468608_FRSVideoUploadTip=1; bottleBubble=1; wise_device=0; showCardBeforeSign=1; TIEBAUID=512142464c5544d9730a7163; TIEBA_USERTYPE=8609f3e2e8dfbb7dcc1175be; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1521020475,1521020563,1521020732,1521021618; STOKEN=fde06a643cb3f4d63399efd386542c42b3049b3aa3f0b350bf218d3b429017bf; rpln_guide=1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    'Referer':'https://www.baidu.com/link?url=s-zoo9sSfqTH87iDXqR2UuWyBPMS0SUkq3mCzKk-1ZfYHjALdJfnLREuOZUc6hTY&wd=&eqid=d238c05300007c88000000065aa8ee36',
    'Host':'tieba.baidu.com'
    }
def SignAdd(kw,tbs_data):
    url = 'https://tieba.baidu.com/sign/add'
    post_data ={
        'ie':'utf-8',
        'kw':kw,
        'tbs':tbs_data
        }
    data =urllib.parse.urlencode(post_data).encode('utf-8')
    post_req =urllib.request.Request(url,data=data,headers=headers)
    try:
        return(kw,json.loads(urllib.request.urlopen(post_req).read().decode('utf-8'))['data']['errmsg'])
    except:    
        return(kw,'faild')
'''form_data = {
    'staticpage':'https://tieba.baidu.com/tb/static-common/html/pass/v3Jump.html',
    'charset':'UTF-8',
    'token':'5812b7d853f18b317f32c7f7806d07b8',
    'tpl':'tb',
    'subpro':'',
    'apiver':'v3',
    'tt':'1520735483356',
    'codestring':'',
    'safeflg':'0',
    'u':'https://tieba.baidu.com/index.html',
    'isPhone':'',
    'detect':'1',
    'gid':'FAB5A3B-9B8E-4CBB-9A29-6CD64DCBF4C4',
    'quick_user':'0',
    'logintype':'dialogLogin',
    'logLoginType':'pc_loginDialog',
    'idc':'',
    'loginmerge':'true',
    'splogin':'rate',
    'username':'15775107464',
    'password':'lAzNTYetf74crxI8bXlnANc+B0kKWuVDXlTcoTkfGTfu+stuMfwGIlIFjnJ4uyuHnTqz9Gq8q/ckpe7eQKpe6Vx1WFWMyjmoTn/zz4sLByVmaOZW+FaJS167RiJJMjgH/sg+HJjKK6GIjRE998LcNE/8opi+ucpGGpe0WdPoWOM=',
    'mem_pass':'on',
    'rsakey':'eSfdKPTJUgYjHHwjPUU18kyxKs1ICoOM',
    'crypttype':'12',
    'ppui_logintime':'44191',
    'countrycode':'',
    'fp_uid':'8a93a36d27465d6db7e372e2f2bb46cb',
    'fp_info':'8a93a36d27465d6db7e372e2f2bb46cb002~~~qCqqoRey8zkhrMo_iqqcue~r5lVra0frp02ee~r5lVra0frpr2Kqg0XOqg0XFqqXaqg~pIe0gqAs2mrLg2B-ryBplyBpYzrag2Qarm95ryBplyBpYzragMQpKWcIfMNY__riquHiqXViquviqXJeDHseVEs3~Qs81Qz7UQI8hE1NjAWUFEu__Ge0Zg7pksrpFprp1d95k1rvUXBpcV65Afr-Ad9p7X7p1UYyrMrH1gR-9pBpYgrMX365AVY5YdBpcgrVy27-Ev6581Y5XXr-t39173Y4gv9pkXB5A29vU39lHy6HNsY5ld7MFp7~yTry8v7pX19583rHc_NiqXSiqXBiqX~iqXQqqoLeyZW0dYyT_ye~EIgOQWeiQ0__qiqXsqquziquhiqujiqudiquPiqupeK651h7pof7pYTBpoMBpAy7Moy7u__',
    'loginversion':'v4',
    'dv':'tk0.86963475212907811520735439399@ppo0uICkPQomiJ2J-5J3snGxw2JxhToDhTGZhRPZnZ9Z03rkpZCkuxrkplnWfgn4ffrsAhD3F42JxTGxhDJsdioswTPvs~PZFjP72QoNVfoDuQoNpgTkHZrkqQBusCAx0hDBwTJsn2G~ufGxwfHGn~Fgwl8mflCkVZo4floN8dnDuQomiJ2J-5J3snGxw2JxhToDhTGZhRPZnZ9Z03rkp-Cku~rkplnWfxo1ffrsAhD3F42JxTGxhDJsdioswTPvs~PZFjP72Qo~qxnkoQoNpgTq__jo0ajCD3-rkHxn1finD2Zn1fQoNpgTkVgCmfxCDHQoDPfo~oQrkplnWfaCDHQnku-rkuZoN2frsAhD3F42JxTGxhDJsdioswTPvs~PZFjP72QoNpgTk3~o1fyoNPQoD3iCDpQBusCAx0hDBwTJsn2G~ufGxwfHGn~Fgwl8mfloN8doDq-CmfaoDpQo~PfnkuQrkplnWf_wvv8Ivu6D0ULhuoho4flrkJaFoiFvQfrNVgCDH~nkPxoNulCDqZCkuinDpfn~oxnko-o~3--onCDHQomfiCDqfrkJxCDPQoD3lomfiokVfrku-oNqQoD3~Cmfiok2a~o0bvomfxrkpZrk2frk2-rkJ-rkHlrkVlrkVgrkufolfioNHQoDp-rkugomfinN3QoDPxrkuaomfiCDPQoD3arku-C4flok2QoNpg',
    'traceid':'D40A5301',
    'callback':'parent.bd__pcbs__3i92sm',
    }
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    'Cookie':'BAIDUID=E9D56547479F0E961FF70523BF1D51F1:FG=1; BIDUPSID=E9D56547479F0E961FF70523BF1D51F1; PSTM=1520735427; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[SL8xzxBXZJn]=mk3SLVN4HKm; PSINO=5; H_PS_PSSID=; FP_UID=8a93a36d27465d6db7e372e2f2bb46cb; HOSUPPORT=1; UBI=fi_PncwhpxZ%7ETaKARmy8CqYhMGKN469STOxhyCTaETJwoI4fScLBZx3VgEuNN99R41GRG9Xv0F9ysFKjqIl',
    'Referer':'https://tieba.baidu.com/index.html'
    }

data_url = urllib.request.urlopen(urllib.request.Request(url='https://passport.baidu.com/v2/api/?login',headers=header,data=urllib.parse.urlencode(form_data).encode('utf-8'))).read().decode('utf-8')
#print(data_url)
#with open('test.html','w',encoding='utf-8') as f:
    #f.write(data_url)
'''
forum_list = list(set(re.findall('"forum_id":(.*?),"forum_name":"(.*?)"',urllib.request.urlopen(urllib.request.Request(url='https://tieba.baidu.com/index.html?traceid=',headers=headers)).read().decode('utf-8'))))
count = 0
for eve in forum_list:
    kw = eve[1].encode('latin-1').decode('unicode_escape')
    forum_url = 'https://tieba.baidu.com/f?kw='+urllib.parse.quote(kw)
    #with open('e:/te.html','w',encoding='utf-8') as f:
       # f.write(urllib.request.urlopen(urllib.request.Request(forum_url,headers=headers)).read().decode('utf-8'))
    #break
    tbs = re.findall('\'tbs\': "(.*?)"',urllib.request.urlopen(urllib.request.Request(forum_url,headers=headers)).read().decode('utf-8'))[0]
    #print(tbs)
    
    count+=1
    time.sleep(2)
    print('-'.join(SignAdd(kw,tbs)))
print('over','共计贴吧数;',str(count))
input()

