from tkinter import *
def callback():
    var.set('吹吧，我才不信~!')
root = Tk()
frame1=Frame(root)
frame2=Frame(root)
var=StringVar()
var.set('你所下载的内容含有未成年人限制,\n\n请满18周岁后再观看')
textLabel = Label(frame1,
                  textvariable=var,
                  justify='left')
textLabel.pack(side='left')
img = PhotoImage(file='temp.gif')
imgs = Label(frame1,image=img)
imgs.pack(side='right')
theButton = Button(frame2,text='我已经满了18岁',command=callback)
theButton.pack()
frame1.pack(padx=10,pady=10)
frame2.pack(padx=3,pady=3)
mainloop()

