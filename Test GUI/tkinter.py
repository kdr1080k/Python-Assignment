import tkinter
import tkinter.messagebox
class ProgramGUI:
    def __init__(self):
        self.main = tkinter.Tk()

        self.messageFrame = tkinter.Frame(self.main)
        self.messageFrame.pack()

        self.welcomeMessage = tkinter.Label(self.messageFrame, text='Welcome to the would you rather game!')
        self.secondMessage = tkinter.Label(self.messageFrame, text='How are you')
        self.welcomeMessage.pack(side='right')
        self.secondMessage.pack(side='right')
        

        self.demoButt = tkinter.Button(self.main, text='Continue', command=self.showBox)
        self.demoButt.pack()

    
   
       
        
        tkinter.mainloop()

    try:
        data = getData()

    except:
        data_list = []
        data = []
        def showBox(self):
            tkinter.messagebox.showerror('YEEEESSS')

        



    
        
        

   

gui = ProgramGUI()
