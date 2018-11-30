from tkinter import *
root = Tk()
theLB = Listbox(root)
theLB.pack()
for item in['鸡蛋','鸭蛋','鹅蛋','鱼蛋']:
    theLB.insert('end',item)
theButton = Button(root,text='删除它',
                   command=lambda x=theLB : x.delete('active'))
theButton.pack()
mainloop()
