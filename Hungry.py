import random as r
class Fish:
    def __init__(self):
        self.x=r.randint(1,10)
        self.y=r.randint(1,10)
    def move(self):
        self.x-=1
        self.y-=2
        print("我的位置是：",self.x,self.y)
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry=True
        self.count=3
    def eat(self):
        if self.hungry:
            print("我要吃！")
            self.count-=1
            if self.count==0:
                self.hungry=False
                print("我吃饱了！")
        else:
            print("我已经吃饱了，不用再吃了！")
s=Shark()
print("已经为你创建了一只鲨鱼：s","请下指令：move,eat.")
