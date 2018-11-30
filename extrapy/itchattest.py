#coding=utf8
import itchat
itchat.auto_login(hotReload=True) #热启动你的微信
#itchat.run()
rooms=itchat.get_chatrooms(update=True)
for i in range(len(rooms)):
 print(rooms[i]) #查看你多有的群
 
room = itchat.search_friends(name=r'易宏轩') #这里输入你好友的名字或备注。
print(room)
userName = room[0]['UserName']
f="E:/30.jpg" #图片地址
try:
 itchat.send_image(f,toUserName=userName) #如果是其他文件可以直接send_file
 print("success")
except:
 print("fail")
