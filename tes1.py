def save_data(data_list):    
    import json
               
    file = open('data.txt', 'w')
    json.dump(data_list, file, indent=4)
    file.close()
    
def getData():
    import json
    
    file = open('data.txt', 'r')
    data = json.load(file)
    file.close()
    return data

def input_something(choice):
    if choice == '':
        print('Nothing Entered\n')

def input_int(prompt, errorMessage = 'Invalid input - Try again.'):
    while True:
            value = input(prompt)
            try:
                numResponse = int(value)
                
            except ValueError:
                print(errorMessage)
                continue
            
            if numResponse >= 0: 
                print('No')
                continue

            return numResponse
                                                                              
         
Quit = False
print('\nWelcome to the "would you rather" admin program ;)')
while (not Quit):
    try:     
       data = getData()
    except:
        data_list = []
        data = []
        save_data(data_list)        
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit. ')
    choice = input('Enter Choice:    ')
    while (not Quit):
        true= True
        false= False
        dic =  {
 "option_1": "test",
 "option_2": "test",
 "mature": true,
 "votes_1": 0,
 "votes_2": 0
 }       
        if choice == 'a':
            print('\nWould you rather...   ')            
            dic["option_1"] = input('Enter Option 1:  ')               
            dic["option_2"] = input('Enter Option 2:  ')
            print('Is the question intended for mature audiences')
            choice = input('Y or N:          \n\n')
            
            if choice == '':
                input_something(choice)
                break
                    
            if choice.lower() == 'n':
                 dic["mature"] = False
            
            if choice.lower() == 'y':
                 dic["mature"] = True                                        
            data.append(dic)
            save_data(data)
            print('\nQuestion added.')                 
            break
        
        elif choice == 'l':     #case sensivity needs to be fixed
            try:              
            
                qnum = 1
                for i in data:
                    print('\nQuestion: ',qnum,') ',i["option_1"],' / ',i["option_2"])
                    qnum += 1                                  
            except:
                data.txt = []
                data_list = []
                data = []
                print('whoa')    #fix no list saved                
                
            break
        
        elif choice == 'd' or choice == 'delete':
            try:                
                             
                choice = int(input('Select question number to delete:  ')   )
         
                if choice >= 1:
                    data.pop(add)  
                    save_data(data)                
                    print('\nQuestion', choice, 'deleted')
                    break
            except ValueError:
                print('\nInvalid Input')
                break
        
            except IndexError:
                print('\nInvalid Input - Check the question list for the correct numbers')
                break
        
        elif choice == 's' or choice == 'search':  #case sensivity needs to be fixed
            
            choice = str(input('\nEnter search term:    '))
            
            if choice == '':
                print('\nNothing Entered')
                break
                      
            try:
           
                qnum = 1                                                                                                    
                for i in data:                    
                    if (choice in i["option_1"] or choice in i["option_2"]):
                        print('\nQuestion: ',qnum,') ',i["option_1"],' / ',i["option_2"])
                        qnum += 1
                break
            except input_something(choice):            
                break
            except ValueError:
                break

        elif choice == 'v':
            prompt = ('Enter Number')
           
          
            input_int(prompt)
            add = int(choice) - 1
            print ('\nQuestion: ',choice,')  ', data[add]["option_1"],' / ', data[add]["option_2"])                          
         
        elif choice == 'q' or choice == 'quit':
            Quit = True
            
        else:            
            print('\nInvalid Option \n')
            break
                        
            
                
                
                
                
            
                 #def inputInt(prompt, errorMessage = 'Invalid input - Try again.'):
    #while True:
       # value = input(prompt)
      #  try:
       #     numResponse = int(value)

      #  except ValueError:
      #      print(errorMessage)
      #      continue
      #  return numResponse

                        

         

         
