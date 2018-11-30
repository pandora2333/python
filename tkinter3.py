from tkinter import *
root = Tk()
photo = PhotoImage(file='temp.gif')
textLabel = Label(root,\
                  text='你所下载的影片含有\n未成年人限制的内容',\
                  justify='left',\
                  padx=10,\
                  image=photo,\
                  compound='center',\
                  fg='white')#前景颜色
textLabel.pack(side='left')
mainloop()
#对齐--justify
#设置位置x--padx
 #这是混合背景与text文本，此外还可以设置字体，比如：font('微软字体',20),20是字号大小--compound
