### MTN Data Platform ###
# list all data plans
# when the user selects a data plan, ask them if they want to bundle or not
# if they want to bundle, "display you have bundled succ"
# if they don't want to bundle, "display subcription canceled"
#yearly: 1TB, 135..2.5TB, 136....4.5TB 137

data_allocation = ['N50 for 40MB', 'N100 for 100MB' , 'N200 for 200MB' , 'N300 for 1GB',
                   'N500 for 2GB', 'N200 for 1GB', 'N300 for 350MB(TIKTOK Only)', 'N500 for 1.5GB',  
                   'N1,500 for 6GB', 'N1,000 for 1.5GB', 'N1,000 for 1.5GB', 'N1,200 for 2GB', 
                   'N1,500 for 3GB', 'N100,000 for 1TB', 'N250,000 for 2.5TB', 
                   'N450,000 for 4.5TB']

def data_plan(userInput):
    try:
        if userInput.lower() == 'daily':
            x = int(input('Please choose a data allocation for this plan by entering any number between 1 and 5: '))
            if x > 0 and x < 6:
                print('You have sucessfully bundled for the ' + data_allocation[x - 1] + ' daily plan.')
            else:
                print('Sorry, you did not enter a number within the range.')
        elif userInput.lower() == 'weekly':
            x = int(input('Please choose a data allocation for this plan by entering any number between 5 and 8: '))
            if x > 4 and x < 9:
                print('You have sucessfully bundled for the ' + data_allocation[x] + ' weekly plan.')
            else:
                print('Sorry, you did not enter a number within the range.')
        elif userInput.lower() == 'monthly':
            x = int(input('Please choose a data allocation for this plan by entering any number between 9 and 12: '))
            if x > 8 and x < 13:
                print('You have sucessfully bundled for the ' + data_allocation[x] + ' monthly plan.')
            else:
                print('Sorry, you did not enter a number within the range.')
        elif userInput.lower() == 'yearly':
            x = int(input('Please choose a data allocation for this plan by entering any number between 13 and 15: '))
            if x > 12 and x < 16:
                print('You have sucessfully bundled for the ' + data_allocation[x] + ' yearly plan.')
            else:
                print('Sorry, you did not enter a number within the range.')
        else:
            print('Your subcription is cancelled.')
    except:
        print('Sorry your entry is either out of range or not a number. Try again next time.')
    finally:
        print('Thank you for using the MTN app.')
