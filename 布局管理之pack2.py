from tkinter import *
root = Tk()#横向填充，上一个是沿x轴的纵向填充，而fill=y，则是沿着y轴的纵向填充
Label(root,text='red',bg='red',fg='white').pack(side='left')
Label(root,text='green',bg='green',fg='black').pack(side='left')
Label(root,text='blue',bg='blue',fg='white').pack(side='left')
mainloop()
