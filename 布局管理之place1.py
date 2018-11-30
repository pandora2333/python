from tkinter import *
root = Tk()
photo = PhotoImage(file='temp.gif')
Label(root,image=photo).pack()
def callback():
    print('正中靶心')
Button(root,text='点我',command=callback).place(relx=0.5,rely=0.5,anchor='center')#relx,rely指相对于附件来说，0指附件左边，1指附件右边，0.5指附件中心,且一直保持中心区位置
mainloop()
