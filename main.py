# https://www.geeksforgeeks.org/python-create-a-digital-clock-using-tkinter/

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('Ominous Clock')
#root.attributes('-fullscreen', True)

def time():
    string = strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('calibri', 40, 'bold'),
            background='black',
            foreground='red')

lbl.pack(anchor='center')
time()

mainloop()
