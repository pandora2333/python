import requests
import threading
import time
from random import *
class AI(threading.Thread):
    def __init__(self,name,startContent):
        threading.Thread.__init__(self)
        self.name = name
        self.flag =0
        self.msg = startContent
        self.copy =''
        self.msgList = ['别重复我说话好吗']
        self.count = 0
    def setContent(self,*content):
        self.ss = content
    def getContent(self):
        self.flag = 1
        return self.msg
    def setAi(self,*ai):
        self.ais = ai
        #self.ai = ai
    def run(self):
        while 1:
            time.sleep(1)
            threadLock.acquire()
            if self.flag:
                temps = []
                for ai in self.ais:
                    temps.append(ai.getContent())
                if not self.count:
                    temp = choice(temps)
                else:
                    temp = self.msg
                    ai.count = 1
                    self.count = 0
                self.setContent(temp)
            s = choice(list(self.ss))
            resp = requests.get("http://api.qingyunke.com/api.php", {
                'key': 'free',
                'appid': 0,
                'msg': s
            })
            resp.encoding = 'utf-8'
            resp = resp.json()
            print(self.name + ':' + resp['content'])
            self.msg = resp['content']
            if self.copy == self.msg:
                self.msg = choice(self.msgList)
                if self.msg == '别重复我说话好吗':
                    print(self.name+':'+'还有别重复我说话好吗,换个说法吧')
                    self.count = 1
                self.msg = input('master,该你说话了:\n')
            else:
                self.copy = self.msg
                self.msgList.append(self.copy)
            threadLock.release()
if __name__ =='__main__':
    print('你好，我是三枚萌萌哒的机器人！')
    threadLock = threading.Lock()
    startContent = input('请输入开始语句:')
    ai1 = AI('AI1',startContent)
    ai2 = AI('AI2',startContent)
    ai3 = AI('AI3',startContent)
    ai1.setAi(ai2,ai3)
    ai2.setAi(ai1,ai3)
    ai3.setAi(ai1,ai2)
    #ai2.setContent('开始吧')
    #print('开始吧')
    ai2.start()
    ai1.setContent(ai2.getContent(),ai3.getContent())
    ai1.start()
    ai2.setContent(ai1.getContent(),ai3.getContent())
    ai3.setContent(ai1.getContent(),ai1.getContent())
    ai3.start()
    




