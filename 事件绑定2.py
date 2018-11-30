from tkinter import *
root = Tk()
def callback(event):
    print(event.char)
frame = Frame(root,width=300,height=200)
frame.bind('<Key>',callback)
frame.focus_set()#焦点设置
frame.pack()
mainloop()
