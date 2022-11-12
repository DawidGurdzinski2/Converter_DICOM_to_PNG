
from tkinter import messagebox
import tkinter as tk
from MainWindow import *

window =tk.Tk() 
windowHeight=500
windowWidth=800
#window.resizable(False,False)
window.geometry(str(windowWidth)+"x"+str(windowHeight))
window.title("Main Window")
window.config(background="white")
frame=MainWindow(window)




def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() 

