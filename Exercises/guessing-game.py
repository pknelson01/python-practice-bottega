def guessing_game():
    while True: 
        print ('Guess a number between 1-50')
        guess = input()

        if guess == '42':
            print ('Correct!')
            return False
        else:
            print(f'{guess} is incorrect, please try again.\n')

guessing_game()
