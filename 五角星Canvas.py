from tkinter import *
import math as m
root = Tk()
root.title('五角星测试')
w = Canvas(root,width=400,height=200,background='red')
w.pack()
center_x = 200
center_y = 100
r = 100
points = [
    #左上点
    center_x - int(r*m.sin(2*m.pi/5)),
    center_y-int(r*m.cos(2*m.pi/5)),
    #右上点
    center_x + int(r*m.sin(2*m.pi/5)),
    center_y-int(r*m.cos(2*m.pi/5)),
    #左下点
    center_x-int(r*m.sin(m.pi/5)),
    center_y+int(r*m.cos(m.pi/5)),
    #顶点
    center_x,
    center_y-r,
    #右下点
    center_x+int(r*m.sin(m.pi/5)),
    center_y+int(r*m.cos(m.pi/5))
    ]
w.create_polygon(points,outline='green',fill='yellow')
mainloop()
    
