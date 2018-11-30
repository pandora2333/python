import time as t
class Timer:
    def __init__(self):
        self.lasted=[]
        self.unit=['年','月','日','小时','分','秒']
        self.begin=0
        self.end=0
        self.msg='未开始计时'
    def __str__(self):
        return self.msg
    __repr__=__str__
    def __add__(self,other):
        return int(self)+int(other)
    #开始计时
    def start(self):
        self.begin=t.localtime()
        self.msg='请先停止计时，才能查看'
        print('开始计时')
    #停止计时
    def stop(self):
        if self.begin==0:
            print('请先开始计时')
        else:
            self.end=t.localtime()
            print("停止计时")
            self.calc()
    #计算时间，供内部使用
    def calc(self):
        self.msg='总共运行了：'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.msg+=str(self.lasted[index])+self.unit[index]
                
                               
        
