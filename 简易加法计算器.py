from tkinter import *
root = Tk()
root.title('一个简单的计算器')
frame = Frame(root)
frame.pack(padx=10,pady=10)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
def test(content):
    return content.isdigit()
testCMD = root.register(test)
e1 = Entry(frame,width=10,textvariable=v1,validate='key',
           validatecommand=(testCMD,'%P')).grid(row=0,column=0)
Label(frame,text='+').grid(row=0,column=1)
e2 = Entry(frame,width=10,textvariable=v2,validate='key',
           validatecommand=(testCMD,'%P')).grid(row=0,column=2)
Label(frame,text='=').grid(row=0,column=3)
e3 = Entry(frame,width=10,textvariable=v3,state='readonly').grid(column=4,row=0)
def calc():
    result=int(v1.get())+int(v2.get())
    v3.set(str(result))
Button(frame,text='计算结果',command=calc).grid(row=1,column=2,pady=5)
mainloop()
