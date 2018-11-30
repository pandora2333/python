from socket import *
host = ''#监听所有ip
port = 9001#用来接收消息的端口
bufSize = 1024
addr = (host,port)
udpServer = socket(AF_INET,SOCK_DGRAM)#udp通信类
udpServer.bind(addr)#开始监听
while True:
    data,addr = udpServer.recvfrom(bufSize)
    data = data.decode()#收到的byte[]转成utf8编码
    if data == 'exit':#收到exit消息后退出
        udpServer.close()
        exit(0)
    else:
        print(data)
