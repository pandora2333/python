from tkinter import *
root = Tk()
def create():
    top = Toplevel()
    top.title('pandora place')
    msg = Message(top,text='i love human')
    msg.pack()
Button(root,text='创建顶级窗口',command=create).pack()
mainloop()
