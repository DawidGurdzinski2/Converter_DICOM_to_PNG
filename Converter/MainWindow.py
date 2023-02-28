import tkinter as tk
from ConversionFrame import *
from MainButton import *
from tkinter import filedialog as fd
import pydicom 
import numpy as np 
from PIL import Image
class MainWindow:


    def __init__(self,window):#inicjalizacja
        self.window=window
        self.initialdir="/home/" #linux
        self.filetypes=(  ("Dicom Files", "*.dcm*"),("All Files", "*.*"))
        self.frame = tk.Frame(self.window,bg="white",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.frame.grid(row=0,column=0,sticky="nswe")
        self.createButtons()
        self.destinationfolder="/home/"
        self.format =".jpg"
        self.cframe=ConversionFrame(self.frame,200,200,2,0)
       
   
  

    def createButtons(self):#tworzy przyciski w oknie
        data = [[self.frame,"Add File", lambda: self.addFiles(), 0,0,8,16,"nw"],
                    [self.frame,"Convert", lambda: self.converFiles() ,1,0,8,16,"nw"],
                    [self.frame,"Delete Unselected Files", lambda: self.deleteUnSelectedFiles() ,0,1,8,24,"se"],
                    [self.frame,"Delete All Files", lambda: self.deleteFiles() ,1,1,8,24,"se"],]
        self.button=[MainButton(*data[i])for i in range(len(data))]




    def addFiles(self):#sluzy do dodawania plikow
        try:
            file_path=fd.askopenfile(initialdir=self.initialdir,filetypes=self.filetypes).name
            print(file_path)
            if file_path in self.cframe.getFiles():
               print("jest juz")
               
            elif(len(str(file_path))>2):
                self.cframe.addDicomFile(file_path)
                self.window.update_idletasks()
        except:
            pass

    def deleteUnSelectedFiles(self):#usuwania nie oznaczone dicom w liscie
        temparray=self.cframe.getSelectedFiles()
        self.cframe.destroyDicomObjects()
        self.cframe.dicomObjects.clear()
        try:
            for paths in temparray:
                self.cframe.addDicomFile(paths)
            self.window.update_idletasks()
        except:
            pass
    
    def deleteFiles(self):#usuwa wszystkie pliki dicom na lisice
        self.cframe.destroyDicomObjects()
        self.cframe.dicomObjects.clear()
        self.window.update_idletasks()
    
    def chooseDestinationFolder(self):# wybiera folder do zapisu
        self.destinationfolder=fd.askdirectory(initialdir=self.initialdir)
        
    def chooseFormat(self):# wybieramy format jpg lub png  (bazowo jest png ale mozemy zmienic go potwierdzajac w oknie na format jpg)
        answer = tk.messagebox.askquestion(title='ask question',message='Do you want save this in JPG format')
        if(answer == 'yes'):
            self.format=".jpg"
        else:
            self.format=".png"
        print(self.format)

    def converFiles(self):# funkcja wcisniecia przycisku Convert ,Wybieramy tu folder do zapisu,wybieramy format, konwertujemy i zapisujemy zdjecia
        self.chooseFormat()
        self.chooseDestinationFolder()
        self.readDicomFile()

    def readDicomFile(self): # zamienia wybrane pliki dicom na zdjecia w formacie jpg lub png
        dicom_images=[]
        for path in self.cframe.getSelectedFiles():
            dicom=pydicom.dcmread(path)
            dicom=dicom.pixel_array.astype(float)
            rescaledImage=((np.maximum(dicom,0)/dicom.max())*255)
            finalImage=np.uint8(rescaledImage)
            finalImage=Image.fromarray(finalImage)
            finalImage.show()
            finalImage.save(self.destinationfolder+self.takePicturename(path)+self.format)

    
    def takePicturename(self,path): # wyłuskuje imie pliku z scieżki w któ©ej sie znajduje
        tempstring=""
        for i in reversed(path):
            if(i =='/'):
                break
            tempstring=tempstring+i
        tempstring=tempstring[::-1]
        for i in range(4):
            tempstring=tempstring.rstrip(tempstring[-1])
        return tempstring 
