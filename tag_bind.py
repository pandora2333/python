from tkinter import *
import webbrowser
root = Tk()
text = Text(root,width=30,height=5)
text.pack()
text.insert('insert','i love FishC.com!')
text.tag_add('tag','1.7','1.16')
text.tag_config('tag',foreground='blue',underline=True)
def show_arrow_cursor(event):
    text.config(cursor='arrow')
def show_xterm_cursor(event):
    text.config(cursor='xterm')
def click(event):
    webbrowser.open('http://www.baidu.com')
    
text.tag_bind('tag','<Enter>',show_arrow_cursor)
text.tag_bind('tag','<Leave>',show_xterm_cursor)
text.tag_bind('tag','<Button-1>',click)
mainloop()
