
from tkinter import messagebox
import tkinter as tk
from MainWindow import *





def main():#głowna funkcja
    window =tk.Tk() 
    windowHeight=500
    windowWidth=800
    window.geometry(str(windowWidth)+"x"+str(windowHeight))
    window.title("Main Window")
    window.config(background="white")
    frame=MainWindow(window)
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop() 


if __name__== '__main__':
    main()