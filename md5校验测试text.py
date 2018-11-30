from tkinter import *
import hashlib
root = Tk()
text = Text(root,width=30,height=5)
text.pack()
text.insert('insert','i love human forever')
content = text.get(1.0,'end')
def getSig(content):
    m = hashlib.md5(content.encode())
    return m.digest()
sig = getSig(content)
def check():
    content = text.get(1.0,'end')
    if getSig(content)!=sig:
        print('警告，内容已经变动')
    else:
        print('内容无变动')
Button(root,text='检查',command=check).pack()
mainloop()
    
