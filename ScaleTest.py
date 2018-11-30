from tkinter import *
root = Tk()
Scale(root,from_=0,to=42,tickinterval=5,resolution=5,length=200).pack()
Scale(root,from_=0,to=200,tickinterval=10,orient='horizontal',length=600).pack()
mainloop()
