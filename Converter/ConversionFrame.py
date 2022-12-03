import tkinter as tk
from tkinter import ttk
from DicomStruct import *



class ConversionFrame:
    def __init__(self,window,height,width,row,column):
        self.windowUp=window
        self.window=tk.Frame(self.windowUp)
        self.height=height
        self.width=width
        self.window.grid(row=2,column=0,columnspan=2,sticky="swe")
        self.createScrollBar()
        self.dicomObjects=[]
        self.row=0


    def addDicomFile(self,path):#obiekty dicomStruct do tablicy  gdzie kazdy obiekt jest tworzony na podstawie sciezki do plikow dicom
        self.dicomObjects.append(DicomStruct(self.frame,2,75,self.row,0,path,0))
        self.row+=1
        self.UpdateDataScrollbar()
        self.window.update_idletasks()
    
    def getSelectedFiles(self):# zwraca tablice wybranych plikow dicom
        temparray=[]
        for file in self.dicomObjects:
            if(file.state):
                temparray.append(file.path)
        return temparray

    def getFiles(self):#zwraca tablice wszystkich plikow dicom
        temparray=[]
        for file in self.dicomObjects:
            temparray.append(file.path)
        return temparray
        
    def destroyDicomObjects(self):#usuwa pliki dicom
        self.row=0
        self.window.destroy()
        self.window=tk.Frame(self.windowUp)
        self.window.grid(row=2,column=0,columnspan=2,sticky="swe")
        self.createScrollBar()
        

    def createScrollBar(self):#frame z scrollbarem
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

    
    def UpdateDataScrollbar(self):#updateuje scrollbara przy zmianie
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        
    