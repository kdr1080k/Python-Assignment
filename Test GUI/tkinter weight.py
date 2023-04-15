def showresult(self):
    try:
        weigt = float(self.weight.get())
        height = float(self.height.get())

        if weight <= 0 or height <= 0:
            raise ValueError
        else:
            bmi = round(weight / (height ** 2), 1)
            tkinter.messagebox.showinfor('Results', 'Your BMI is ' + str(bmi))

    except ValueError:
        tkinter.messagebox.showerror('Invalid input', 'Enter two positives inputs')
        
