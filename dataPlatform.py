
# import dataPlanFunctions

# print('Welcome to the MTN Data Bundle APP')
# data_plan_list = ['daily', 'weekly', 'monthly', 'yearly']

# try:
#     userInput = int(input('Please enter an number between 1 and 4 to choose a data bundle: '))
#     if userInput > 0 and userInput < 5:
#         y =  input('Do you want to bundle or not?, please enter YES to bundle and No to not bundle?: ')
#         if y.lower() == 'yes':
#             userInput2 = data_plan_list[userInput - 1]
#             dataPlanFunctions.data_plan(userInput2)
#         elif y.lower() == 'no':
#             print('Your subscription attempt is cancelled. Thank you for using the MTN data plan app.')
#         else:
#             print('You made a wrong entry, please try again next time.')
#     else:
#         print('You entry is out of range. Please try again')
# except:
#     print('You have not entered a number. Please try again')


Subscriber = input('which data bundle can you afford; monthly(1) or weekly(2) or daily(3)??')

monthly_data_plan = {'M1':'N1000/1.5GB', 'M2':'N1200/2GB', 'M3':'N1500/3GB', 'M4':'N2000/4.5GB', 'M5':'N2500/6GB'}

weekly_data_plan = {'W1':'N500/750MB/14days', 'W2':'N500/1GB/7dyas', 'W3':'N1500/6GB/7dyas', 'W4':'N300/350MG/7days', 'W5':'N100/7ALL So'}

daily_data_plan = {'D1':'N50/40MB/daily', 'D2':'N100/100MB/Daily', 'D3':'N200/20MB/3days', 'D4':'N300/1GB/Daily', 'D5':'N500/2G/Daily'}

def bundle(x):
    i = 1
    try:
        while i <= 5:
            if x == ('M'+ str(i)):
                print(monthly_data_plan.get(str(x)))
                user = input('Enter YES to bundle: ')
                if user.upper() == 'YES':
                    print('you have bundled successfully!!!')
                else:
                    print('Sorry you made a wrong entry, try again next time.')
                    break
                
            elif x == ('W' + str(i)):
                print(weekly_data_plan.get(str(x)))
                user = input('Enter YES to bundle: ')
                if user.upper() == 'YES':
                    print('you have bundled successfully!!!')
                else:
                    print('Sorry you made a wrong entry, try again next time.')
                    break

            elif x == ('D' + str(i)):
                print(daily_data_plan.get(str(x)))
                user = input('Enter YES to bundle: ')
                if user.upper() == 'YES':
                    print('you have bundled successfully!!!')
                    
                else:
                    print('Sorry you made a wrong entry, try again next time.')
                    break
                
            
            else:
                print('Sorry you made a wrong entry, try again next time.')
            
    except:
        
        print('invalid')
        

def data():
    for x in range(1):
        if Subscriber == ('1'):
            print(monthly_data_plan)
            x = input('Select your preferred bundle; M1 - M5: ')
            if x == 'M1' or 'M2' or 'M3' or 'M4' or 'M5':
                bundle(x)
            else:
                print('Sorry your entry does not match. Try again later')
                
        elif Subscriber == ('2'):
            print(weekly_data_plan)
            print('select your preferred bundle; W1 - W5 ')    
               
        elif Subscriber == ('3'):
            print(daily_data_plan)
            print('select your preferred bundle; D1 - D5 ')
        
        else:
            break

data()





# x = input('').capitalize()

# i = 1


# """MTN Data Platform"""
# import MTN_Data_Plan as mdp

# prompt = 'You dialed *131#'
# prompt += "\nPress enter to choose a plan."
# user = input(prompt)
# if user.lower() == "":
#     _user = mdp.choice()
#     if _user == 1:
#         lent = mdp.weekly()
#         user_ = int(input('Select plan _'))
#         if user_ in range(1, lent):
#             mdp.bundle()
#         else:
#             print('Invalid response, try again.')
#     elif _user == 2:
#         _lent = mdp.monthly()
#         user_ = int(input('\nSelect plan _'))
#         if user_ in range(1, _lent):
#             mdp.bundle()
#         else:
#             print('Invalid response, try again.')
#     else:
#         print('Invalid response, try again.')
# else:
#     print('Invalid rsponse, try again.')
    
