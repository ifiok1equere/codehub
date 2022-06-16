def guessing_game():
    import random
    x = random.randint(1,10)
    try:
        userInput = int(input('Guess a number between 1 and 10: '))
        if userInput == x:
            print('You win')
        else:
            print('try again')
    except:
        print('Wrong value enetered. Please enter an integer between 1 and 10.')
    finally:
        print('Thank you for guessing. Goodbye.')

guessing_game()