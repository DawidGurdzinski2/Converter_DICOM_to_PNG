import tkinter as tk
from ConversionFrame import *
from MainButton import *
from tkinter import filedialog as fd
import pydicom 
import numpy as np 
from PIL import Image
class MainWindow:


    def __init__(self,window):
        self.window=window
        self.initialdir="/home/dawid/Desktop/Programing and other" #linux
        #self.initModules()
        self.filetypes=(  ("Dicom Files", "*.dcm*"),("All Files", "*.*"))
        self.frame = tk.Frame(self.window,bg="white",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.frame.grid(row=0,column=0,sticky="nswe")
        self.createButtons()
        self.cframe=ConversionFrame(self.frame,200,200,2,0)
       
   
  

    def createButtons(self):
        data = [[self.frame,"Add File", lambda: self.addFiles(), 0,0,8,16,"nw"],
                    [self.frame,"Convert", lambda: self.converFiles() ,1,0,8,16,"nw"],
                    [self.frame,"Delete Unselected Files", lambda: self.deleteUnSelectedFiles() ,0,1,8,24,"se"],
                    [self.frame,"Delete All Files", lambda: self.deleteFiles() ,1,1,8,24,"se"],]
        self.button=[MainButton(*data[i])for i in range(len(data))]




    def addFiles(self):
        try:
            file_path=fd.askopenfile(initialdir=self.initialdir,filetypes=self.filetypes).name
            print(file_path)
            if file_path in self.cframe.getFiles():
               print("jest juz")
               
            elif(len(str(file_path))>2):
                #print(len(str(file_path)))
                self.cframe.addDicomFile(file_path)
                self.window.update_idletasks()
        except:
            pass

    def deleteUnSelectedFiles(self):

        temparray=self.cframe.getSelectedFiles()
        self.cframe.destroyDicomObjects()
        self.cframe.dicomObjects.clear()
        try:
            for paths in temparray:
                self.cframe.addDicomFile(paths)
            self.window.update_idletasks()
        except:
            pass
    
    def deleteFiles(self):
        self.cframe.destroyDicomObjects()
        self.cframe.dicomObjects.clear()
        self.window.update_idletasks()
            
        
    def converFiles(self):
        self.readDicomFile()

    def readDicomFile(self,path):
        dicom_images=[]
        for path in self.cframe.getSelectedFiles():
            dicom=pydicom.dcmread(path)
            dicom=dicom.pixel_array.astype(float)
            rescaledImage=((np.maximum(dicom,0)/dicom.max())*255)
            finalImage=np.uint8(rescaledImage)
            finalImage=Image.fromarray(finalImage)
            finalImage.show()
            finalImage.save()

    