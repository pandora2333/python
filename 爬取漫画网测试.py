import requests
headers ={'Host':'manhua1021-61-174-50-99.cdndm5.com','Referer':'http://www.dm5.com/m130561-p17/','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'}
#http://www.dm5.com/m130561-p22/#ipg21

res = requests.get('http://manhua1021-61-174-50-99.cdndm5.com/13/12138/130561/17_7344.jpg?cid=130561&key=3b09cdc6c314cd0c44032ff7101fc55e',headers=headers)

#print(res.encoding)

with open('e:/p22.jpg','wb') as f:
    f.write(res.content)
