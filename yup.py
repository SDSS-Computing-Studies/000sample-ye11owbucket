import tkinter as tk 
from tkinter import *
from tkinter import ttk




window = tk.Tk()
window.title("dubious little creature")
sus = PhotoImage(file="sus.jpg")
label1 = tk.Label(window, image=sus)
label1.grid(column=0, row=0) 

window.mainloop()
