from tkinter import *
import tkinter.colorchooser as colorchooser
root = Tk()
def callback():
    colorbin = colorchooser.askcolor()
    print(colorbin)
Button(root,text='选择颜色',command=callback).pack()
mainloop()
