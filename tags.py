from tkinter import *
root = Tk()
text = Text(root,width=20,height=5)
text.pack()
text.insert('insert','i love human forever')
text.tag_add('here','1.7','1.12','1.14')
text.tag_config('here',background='yellow',foreground='red')
mainloop()
