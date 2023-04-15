import tkinter
import tkinter.messagebox
class ProgramGUI:
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title('BMI Calculator')

        self.messageFrame = tkinter.Frame(self.main)
        self.messageFrame.pack()

      
        

        self.welcomeMessage = tkinter.Label(self.messageFrame, text='Welcome!')
        self.secondMessage = tkinter.Label(self.messageFrame, text='Is Ryan gai?')
        self.welcomeMessage.pack(side='left')
        self.secondMessage.pack(side='right')
        
        
        self.demoButt = tkinter.Button(self.main, text='Yes', command=self.showBox, pady=20)
        self.demoButt.pack(pady=20)
        self.demoButt = tkinter.Button(self.main, text='No', command=self.showBox2, pady=20)
        self.demoButt.pack(pady=20)
        self.demoEntry = tkinter.Entry(self.main, width=15)
        self.demoEntry.pack(pady=20)
       
        
        tkinter.mainloop()
        
    def showBox(self):
        tkinter.messagebox.showinfo('')
        self.main.destroy()
    def showBox2(self):
        
        tkinter.messagebox.showinfo('')
        self.main.destroy()
            
        

   

gui = ProgramGUI()
