import tkinter as tk
from MainButton import *
from Osciloscope import *
from Generator import *

class ButtonFrame:


    def __init__(self,window):
        self.window=window
        self.initModules()
        self.frame = tk.Frame(self.window,bg="black",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.createButtons()
        self.frame.grid(row=0,column=0,sticky="nswe")
       
    def initModules(self):
        self.teporaryWindow=tk.Toplevel()
        self.Osc=Osciloscope(self.teporaryWindow,0,0 ,False,0)
        self.Gen=Generator(self.teporaryWindow,False)
        #self.Mod=
        #self.Ter=
        self.teporaryWindow.destroy()

    def createButtons(self):
        data = [[self.frame,"Osciloscope", lambda: self.clickOsciloscop(), 0,0,"blue.png"],
                    [self.frame,"Generator", lambda: self.clickGenerator() ,0,1,"blue.png"],
                    [self.frame,"Modulator", lambda: self.clickModulator(), 0,2,"blue.png"],
                    [self.frame,"Terminal", lambda: self.clickTerminal(), 0,3,"blue.png"],]
        self.button=[MainButton(*data[i])for i in range(len(data))]


    def clickOsciloscop(self):
        self.button[0].changeButtonState(False) 
        self.OSC=tk.Toplevel()
        self.OSC.title("Osciloscope")
        self.OSC.geometry(str(1150)+"x"+str(875))
        self.OSC.config(background="white")
        self.Osc=Osciloscope(self.OSC,400,800,True,1)
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.button[0].changeButtonState(True) 
                self.Osc.resetData()
                self.OSC.destroy()   
        self.OSC.protocol("WM_DELETE_WINDOW", on_closing)
        
    def clickGenerator(self):
        self.button[1].changeButtonState(False) 
        self.GEN=tk.Toplevel()
        self.GEN.title("Generator")
        self.GEN.geometry(str(700)+"x"+str(700))
        self.GEN.config(background="white")
        self.Gen=Generator(self.GEN,True)
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.button[1].changeButtonState(True) 
                self.Gen.resetData()
                self.GEN.destroy()   
        self.GEN.protocol("WM_DELETE_WINDOW", on_closing)         



    def clickModulator(self):
        self.button[2].changeButtonState(False) 
        Modulator=tk.Toplevel()
        Modulator.title("Modulator")
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                Modulator.destroy()
        Modulator.protocol("WM_DELETE_WINDOW", on_closing)
        print("modulator")
    
    

    def clickTerminal(self):
        self.button[3].changeButtonState(False) 
        Terminal=tk.Toplevel()
        Terminal.title("Terminal")
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                Terminal.destroy()
        Terminal.protocol("WM_DELETE_WINDOW", on_closing)
        print("terminal") 
    
    
    def getData(self):
        return [self.Gen.dataout,[[0,0],[0,0]],[[0,0],[0,0]]]

    def UpdateData(self):
        self.Osc.UpdateData(self.buttonsStates())
        self.Gen.UpdateData()
        #self.Mod.UpdateData()
        #self.Ter.UpdateData()

    def setData(self,data):
        self.Osc.datain=data
        #self.Mod.datain=data2
        

    def buttonsStates(self):
        return [self.button[i].getButtonState() for i in range(len(self.button))]
    
    
        
    
