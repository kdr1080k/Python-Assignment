import tkinter
import tkinter.messagebox
import json

class ProgramGUI:
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title('Would you rather')       
        self.messageFrame = tkinter.Frame(self.main)
        self.messageFrame.pack()
        try:
            self.file = open('data.txt', 'r')
            self.data = json.load(self.file)
            self.file.close()
            self.question = tkinter.Label(self.main, text="Would you rather...", pady= 10)
            self.question.pack(side='top')
            self.vote1 = tkinter.Button(self.main, command=lambda: self.record_vote('votes_1'))
            self.vote1.pack(side='left')
            self.vote2 = tkinter.Button(self.main, command=lambda: self.record_vote('votes_2'))
            self.vote2.pack(side='right')
            self.question_num = 0
            self.show_mature = tkinter.messagebox.askyesno('Mature Content',  'Do you want to view questions for mature audiences?')
            self.show_question()
            tkinter.mainloop()
            
        except FileNotFoundError:
            tkinter.messagebox.showerror('Error',  'No Questions Saved')
            self.main.destroy()

    def show_question(self):
        try:    
            if (self.data[self.question_num]["mature"] == True and self.show_mature == False):
                self.question_num += 1
                self.show_question()
            else:
                self.vote1.config(text=self.data[self.question_num]["option_1"]+"?", pady= 20)
                self.vote2.config(text=self.data[self.question_num]["option_2"]+"?", pady= 20)
        except IndexError:
            tkinter.messagebox.showerror('Error',  'No more questions')
            self.main.destroy()
            return
        
    def record_vote(self, vote):
        self.data[self.question_num][vote] += 1
        self.file = open('data.txt', 'w')
        json.dump(self.data, self.file, indent=4)
        self.file.close()
        tkinter.messagebox.showinfo('Vote Recorded',  'Your choice has been recorded')
        self.question_num += 1
        self.show_question()
        
gui = ProgramGUI()
    
             
        

        
    


    
        
        

   
