from tkinter import *
root = Tk()
group = LabelFrame(root,text='最好的脚本语言是？',padx=5,pady=5)
group.pack(padx=10,pady=10)
langs=[('python',1),
       ('perl',2),
       ('ruby',3),
       ('lua',4)]
for lang,num in langs:
    b=Radiobutton(group,text=lang,value=num,indicatoron=False)
    b.pack(anchor='w')
mainloop()
