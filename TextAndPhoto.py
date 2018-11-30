from tkinter import *
root = Tk()
text = Text(root,width=30,height=100)
text.pack()
photo = PhotoImage(file='temp.gif')
def show():
    text.image_create('end',image=photo)
b1 = Button(text,text='点我点我',command=show)
b1.pack()
text.window_create('insert',window=b1)
mainloop()
    
