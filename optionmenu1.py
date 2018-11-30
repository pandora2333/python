from tkinter import *
root = Tk()
var = StringVar()
var.set("one")
w = OptionMenu(root,var,"one","two","three")
w.pack()
mainloop()
