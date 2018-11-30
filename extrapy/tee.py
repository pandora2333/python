import time

'''# 1:使用web浏览器自动化框架，实现登陆
import selenium.webdriver

driver = selenium.webdriver.Ie()
login_url = 'http://web2.qq.com/'
driver.get(login_url)'''
input('Please press enter to continue.')
friend_list = []
for eve_friend in driver.find_elements_by_class_name(list_item):
   friend_list.append(eve_friend.find_element_by_xpath('a/@_uin').text)

temp_cookie =''
for eve_cookie in driver.get_cookies():
   temp_cookie = temp_cookie + eve_cookie['name'] +'='+ eve_cookie['value'] +''; 

headers = {
   'Accept': '*/*',
   'Accept-Language':' zh-CN,zh;q=0.9,en;q=0.8',
   'Cache-Control':' no-cache',
   'Connection':'keep-alive',
   'Content-Type':'application/x-www-form-urlencoded',
   'Cookie':temp_cookie,
   'Host':'d1.web2.qq.com',
   'Origin':' http://d1.web2.qq.com',
   'Pragma':' no-cache',
   'Referer':' http://d1.web2.qq.com/cfproxy.html?v=20151105001&callback=1',
   'User-Agent':' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
   ,
}
driver.quit()

print(headers)

# 2:通过urllib进行信息发送
import urllib.parse
import urllib.request

for eve_friend in friend_list:
   post_data = {
      'r': r'{to: ' + str(eve_friend) + r',content: [\这是一条测试信息，请您忽略.\,[\font\,{\name\:\宋体\,\size\:10,\style\:[0,0,0],\color\:\000000\}]],face: 603, clientid: 53999199, msg_id: 82180004,psessionid: 8368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857}'
   }
   print(urllib.request.urlopen(urllib.request.Request(url='http://d1.web2.qq.com/channel/send_buddy_msg2', data=urllib.parse.urlencode(post_data).encode('utf-8'), headers=headers)).read().decode('utf-8'))
   time.sleep(5)
