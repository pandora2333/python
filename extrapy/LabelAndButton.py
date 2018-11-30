from tkinter import *
root = Tk("图片下载简单界面")
Label(root,text='作品:').grid(row=0,column=0)
Label(root,text='作家:').grid(row=1,column=0)
e1 = Entry(root)
e2 = Entry(root)#输入框
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)
def show(dat):
    print('作品:《%s》' % e1.get())
    print('作家:%s' % e2.get())
    print(dat)
    e1.delete(0,'end')
    e2.delete(0,'end')
Button(root,text='获取信息',width=10,command=show("test")).grid(row=3,column=0,sticky='w',padx=10,pady=5)
Button(root,text='退出',width=10,command=root.quit).grid(row=3,column=1,sticky='e',padx=10,pady=5)
mainloop()
