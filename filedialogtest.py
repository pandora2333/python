from tkinter import *
import tkinter.filedialog as filedialog
root  = Tk()
def callback():
    filename = filedialog.askopenfilename(filetypes=[("PNG",".png"),("GIF",".gif")])#此外还有asksavefilename函数,该函数内传入defaultextension=".py"则表示为文件默认打开类型
    print(filename)
Button(root,text='打开文件',command=callback).pack()
mainloop()
#此外还有参数initialdir:制定打开和保存的默认路径，默认情况下是当前文件夹，即当前工作目录
#parent：如果不指定该项，那么对话框默认显示在根窗口上，如果指定在子窗口w上，则parent=w
#title：指定文件对话框的标题栏文本
#返回值：1.如果用户选择了一个文件，那么返回值是该文件的完整路径（绝对路径），2.如果用户点击了取消按钮则返回值是空字符串
