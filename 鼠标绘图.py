# -*- coding: utf-8 -*
from tkinter import *
root = Tk()
w = Canvas(root,width=400,height=200)
w.pack()
def paint(event):
    x1,y1 = (event.x),(event.y)
    x2,y2 = (event.x),(event.y)
    w.create_oval(x1,y1,x2,y2,fill='red')
w.bind('<B1-Motion>',paint)
Label(root,text='拖住鼠标并移动，便可开始绘图').pack(side='bottom')
mainloop()
