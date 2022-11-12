import tkinter as tk

from tkinter import messagebox
class MainButton:
    
    def __init__(self,frame, text, func,row,column,height,width):
        tk.Grid.rowconfigure(frame, row, weight=1)
        tk.Grid.columnconfigure(frame, column, weight=1)
        self.button = tk.Button(
            frame,
            text=text,
            state="normal",
            compound = tk.TOP,
            command=func,
            height=height,
            width=width
            )
        self.flag=0
        self.button.grid(row=row,column=column ,sticky="nw")
        
 
    def changeButtonState(self,state):
        if state:
            self.button.config(state="normal")
        else:
            self.button.config(state="disabled")

    def getButtonState(self):
        return self.button['state']=="normal"