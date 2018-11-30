from tkinter import *
root = Tk()
text = Text(root,width=30,height=5)
text.pack()
text.insert('insert','i am pandora')
text.insert('end','i love comic')
def show():
    print('哟，我被点了一下')
p1 = Button(text,text='点我点我',command=show)
text.window_create('insert',window=p1)
mainloop()
