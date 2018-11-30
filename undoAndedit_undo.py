from tkinter import *
root = Tk()
text = Text(root,width=30,height=5,undo=True,autoseparators=False)#undo默认是关闭的，用于恢复文本内容;autoseparators默认是true表示自动插入换行符（表示结束）
text.pack()
text.insert('insert','i love human forever')
def show():
    text.edit_undo()#只有undo为true时才可以用
def callback(event):
    text.edit_separator()#此时为一个一个字符的撤销
text.bind('<Key>',callback)
    
Button(root,text='撤销',command=show).pack()
mainloop()
