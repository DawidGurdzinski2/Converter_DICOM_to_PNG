import tkinter as tk
from tkinter import ttk


class DicomStruct:

    def __init__ (self,window,height,width,row,column,name,state):
        self.window=window
        self.path=name
        self.height=height
        self.width=width
        self.row=row
        self.state=state
        self.column=column
        self.x=tk.IntVar()
        self.frame=tk.Frame(self.window,background="white")
        self.frame.grid(row=row,column=0,sticky="nswe")
        self.label=tk.Label(self.frame,text=name,height=height,width=width,background="grey",font=('Arial',10))
        self.label.grid(row=0,column=0,sticky="nswe")
        self.createCheckbox()

    def createCheckbox(self):# struktura dicomstructa w frame z srcoolbarem
        check_button =tk.Checkbutton(self.frame,
                           text="Select File",
                           variable=self.x,
                           onvalue=1,
                           offvalue=0,
                           command=self.changeState,
                           font=('Arial',10),
                           fg='#00FF00',
                           bg='grey',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           compound='left')
        check_button.grid(row=0,column=1)
    
    def changeState(self):#sprawdza czy obiekt dicom został wybrany do conwersji/lub usuniecia
        if(self.x.get()):
            self.state=1
        else:
            self.state=0
