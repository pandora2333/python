from tkinter import *
root = Tk()
textLabel = Label(root,\
                  text='你所下载的影片含有\n未成年人限制的内容',\
                  justify='left',\
                  padx=10)
textLabel.pack(side='left')
photo = PhotoImage(file='temp.gif')
imageLabel = Label(root,image=photo)
imageLabel.pack(side='right')
mainloop()
