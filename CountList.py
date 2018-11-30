class CountList:
    '定制一个计数容器，用于记录容器中元素被访问的次数'
    def __init__(self,*args):
        self.values=[i for i in args]
        self.count={}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self,key):
        self.count[key]+=1
        return self.values[key]
