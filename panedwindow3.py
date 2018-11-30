from tkinter import *
m1 = PanedWindow(showhandle=True,sashrelief='sunken')#showhandle可以使线条显现,可以用handlepad调整手柄的位置，默认分割线上的手柄到最近的一端距离为八个像素
m1.pack(fill='both',expand=1)
left = Label(m1,text='left pane')
m1.add(left)
m2 = PanedWindow(orient='vertical',showhandle=True,sashrelief='sunken')
m1.add(m2)
top = Label(m2,text='top pane')
m2.add(top)
bottom = Label(m2,text='bottom pane')
m2.add(bottom)
mainloop()
