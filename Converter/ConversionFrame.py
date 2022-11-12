import tkinter as tk
from tkinter import ttk




class ConversionFrame:


    def __init__(self,window,height,width,row,column):
        self.window=tk.Frame(window)
        
        
        self.height=height
        self.width=width
        
        self.window.grid(row=row,column=column,sticky="swe")
        self.createScrollBar()


    def createScrollBar(self):
        self.scrollframe=tk.Frame(self.window,bg="white",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.scrollframe.grid(row=0,column=0,sticky="we")
        self.canvas=tk.Canvas(self.scrollframe,bg="grey")
        self.canvas.pack(side="left",fill="both",expand=1)
        self.scrollbar=ttk.Scrollbar(self.scrollframe,orient="vertical",command=self.canvas.yview)
        self.scrollbar.pack(side="right",fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>',lambda e:self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.frame=tk.Frame(self.canvas,bg="grey",bd=5)
        self.canvas.create_window((0,0),window=self.frame ,anchor="sw")

    
    def UpdateDataScrollbar(self):
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        