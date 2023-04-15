import tkinter
class ProgramGUI: # define a ProgramGUI class
 def __init__(self):
     self.main = tkinter.Tk() # create the main window
     self.main.title('My Awesome App')
     self.main.geometry('350x150')
     self.main.resizable(width=False, height=False)
     self.main.iconbitmap('cat.ico')
     tkinter.mainloop()
gui = ProgramGUI() # create a ProgramGUI object
