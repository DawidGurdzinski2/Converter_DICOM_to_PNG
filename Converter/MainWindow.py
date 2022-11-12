import tkinter as tk
from ConversionFrame import *
from MainButton import *

class MainWindow:


    def __init__(self,window):
        self.window=window
        #self.initModules()
        self.frame = tk.Frame(self.window,bg="white",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.frame.grid(row=0,column=0,sticky="nswe")
        self.createButtons()
        self.cframe=ConversionFrame(self.frame,200,200,2,0)
       
   
  

    def createButtons(self):
        data = [[self.frame,"Osciloscope", lambda: self.clickOsciloscop(), 0,0,8,16],
                    [self.frame,"Generator", lambda: self.clickGenerator() ,1,0,8,16],]
        self.button=[MainButton(*data[i])for i in range(len(data))]




    def clickOsciloscop(self):
        self.button[0].changeButtonState(False) 
        self.OSC=tk.Toplevel()
        self.OSC.title("Osciloscope")
        self.OSC.geometry(str(1150)+"x"+str(875))
        self.OSC.config(background="grey")
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.button[0].changeButtonState(True) 
                self.OSC.destroy()   
        self.OSC.protocol("WM_DELETE_WINDOW", on_closing)
        
    def clickGenerator(self):
        self.button[1].changeButtonState(False) 
        self.GEN=tk.Toplevel()
        self.GEN.title("Generator")
        self.GEN.geometry(str(700)+"x"+str(700))
        self.GEN.config(background="grey")
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.button[1].changeButtonState(True) 
                self.GEN.destroy()   
        self.GEN.protocol("WM_DELETE_WINDOW", on_closing)         




    