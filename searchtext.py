from tkinter import *
root = Tk()
text = Text(root,width=30,height=5)
text.pack()
text.insert('insert','i love human forever')
def getIndex(text,index):
    #print(type(text.index(index)))
    #print(map(int,str.split(text.index(index),".")))
    return tuple(map(int,str.split(text.index(index),".")))#将字符串x.y转换成元组（x,y)
start = "1.0"
while True:
    pos = text.search("o",start,stopindex='end')
    if not pos:
        break
    print('我的位置是：',getIndex(text,pos))
    #print('原始值：',pos)
    #print(type(pos))
    start = pos + '+1c'
mainloop()
