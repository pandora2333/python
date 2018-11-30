from tkinter import *
root = Tk()
w1 = Message(root,text='这是一条测试信息',width=100)
w2 = Message(root,text='这是一条很长的测试信息。。。。长长',width=100)#message窗口组件会使文本自动换行
w1.pack()
w2.pack()
mainloop()
