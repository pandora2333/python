from tkinter import *
root = Tk()
options = [
    'calif',
    '458',
    'wer',
    'aodi'
    ]
var = StringVar()
var.set(options[0])
w = OptionMenu(root,var,*options)
w.pack()
mainloop()
