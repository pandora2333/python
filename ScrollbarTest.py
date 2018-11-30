from tkinter import *
root = Tk()
sb = Scrollbar(root)
sb.pack(side='right',fill='y')
lb = Listbox(root,yscrollcommand=sb.set)
lb.pack(side='left',fill='both')
for i in range(30):
    lb.insert('end',i)
sb.config(command=lb.yview)
mainloop()
