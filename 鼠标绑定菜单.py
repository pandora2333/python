from tkinter import *
root = Tk()
def callback():
    print('你好！')
menubar = Menu(root,tearoff=False)#若不把tearoff设为false则菜单可以脱离root根窗口
menubar.add_command(label='撤销',command=callback)
menubar.add_command(label='重做',command=callback)
frame = Frame(root,width=512,height=512)
frame.pack()
def pop(event):
    menubar.post(event.x,event.y_root)
frame.bind('<Button-3>',pop)
mainloop()
