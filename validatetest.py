from tkinter import *
root=Tk()
root.title('测试')
def test():
    if e1.get()=='pandora':
        print('正确')
        return True
    else:
        print('错误')
        e1.delete(0,'end')
        return False
def test2():
    print('我被调用了')
    return True
v = StringVar()
e1 = Entry(root,textvariable=v,validate='focusout',validatecommand=test,invalidcommand=test2)#前一个volidate是验证器，后一个是函数验证的触发器,最后一个是前一个返回false时的触发函数

e2=Entry(root)
e1.pack(padx=10,pady=5)
e2.pack(padx=10,pady=5)
mainloop()
