from tkinter import *
m = PanedWindow(orient='vertical')
m.pack(fill='both',expand=1)
top = Label(m,text='top pane')
m.add(top)
bottom = Label(m,text='bottonm pane')
m.add(bottom)
mainloop()
#双重分割，一条线
