import tkinter as tk
class App:
    def __init__(self,master):
        frame=tk.Frame(master)
        frame.pack(side='left')
        self.h1_there=tk.Button(frame,text='打招呼',bg='black',fg='white',command=self.say_hi)
        self.h1_there.pack(padx=10,pady=5)
    def say_hi(self):
        print('大家好！')
root=tk.Tk()
app=App(root)
root.mainloop()

    




