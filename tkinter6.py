from tkinter import *
root = Tk()
langs=[('python',1),
      ('perl',2),
      ('ruby',3),
      ('lua',4)]
for lang,num in langs:
    b=Radiobutton(root,text=lang,value=num,indicatoron=False)
    b.pack(fill='x')
mainloop()
