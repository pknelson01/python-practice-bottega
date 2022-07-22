# Day 1
    # challenge to build before she taught us anything
        # def RandomNameGen():
        #     city = input("""
        #     Welcome to the Band Name Generator.
        #     What's the name of the City you grew up in?
        #     """)
        #     name = input("""
        #     What was the name of your first / favorite pet?
        #     """)
        #     print (f"""
        #     Your band name could be {city} {name}!
        #     """)

        # RandomNameGen()

    
    # name = 'Parker Nelson'
    # birth_day_ = 10
    # birth_month_ = 9
    # birth_year = 2001
    # school_old = 'Westlake'
    # school_new = 'Bottega'
    # print(f"""
    # Hello World!
    # My name is {name} and my birthday is {birth_month_}/{birth_day_}/{birth_year}.
    # I graduated from {school_old} and am currently enrolled in {school_new}.
    # """)

    # print('Hello ' + input('What is your name? ') + ', how are you doing today?')

    # two_digit_number = input("Type a two digit number: ")

    # first = int(two_digit_number[0])
    # second = int(two_digit_number[1])
    # two_digit_number = first + second

    # print(f"{first} + {second}=",  two_digit_number)

    # # print(len(input("What is your name? ")))

    # name = 'Parker'
    # print(name)
    # name = 'Ava'
    # print(name)

    # print(len(input("What is your name? ")))

    # or...

    # x = input("What is your name? ")
    # y = len(x)
    # print(y)

# Day 2
    # STARTER CHALLENGE

        # def total():
        #     bill = 0
        #     friends = 0
        #     tip = 0
        #     total = 0

        #     print('Welcome to the Tip Calculator')
        #     answer = float(input("What was the total bill? "))
        #     bill += answer
        #     answer_two = float(input(f"How many ways should we split the bill of ${bill}? "))
        #     friends += answer_two
        #     answer_three = float(input(f"What percentage tip would you like to give? "))
        #     tip += answer_three
        #     answer_four = round(bill / friends * 1.15, 2)
        #     total += answer_four
        #     print(f'Each person should pay ${total}')

        # total()

    # # num_char = len(input("what is your name? "))
    # # print("your name has " + str(num_char) + " characters.")

    # # def skywalker_y_or_n():
    # #     answer = input("""
    # #     Is Rey a Skywalker? yes or no.
    # #     """)
    # #     if answer == 'yes' or answer == 'Yes' or answer == 'y' or answer == 'YES' or answer == 'Y':
    # #         print("""
    # #         The force is strong with you.
    # #         """)
    # #     elif answer == 'no' or answer == 'No' or answer == 'n' or answer == 'N' or answer == 'NO':
    # #         print("""
    # #         You are simply a dumb bitch.
    # #         """)
    # #     else: skywalker_y_or_n()

    # # skywalker_y_or_n()

    # # numbers = input('type a two digit number: ')
    # # dig_one = numbers[0]
    # # dig_two = numbers[1]
    # # summ = int(dig_one) + int(dig_two)
    # # print(summ)

    # # def body_mass_index_calculator():
    # #     weight = float(input('What is your weight in kilograms?  '))
    # #     height = float(input('What is your height in meters?  '))
    # #     new_height = height ** 2
    # #     bmi = weight / new_height
    # #     print(round(bmi))

    # # body_mass_index_calculator()

    # def Time_Left():
    #     age = input("Enter your age in years:  ")
    #     average_age = 90
    #     average_months = average_age * 12
    #     average_weeks = average_age * 52
    #     average_days = average_age * 365
    #     age_months = int(age) * 12
    #     age_weeks = int(age) * 52
    #     age_days = int(age) * 365
    #     months_left = average_months - age_months
    #     weeks_left = average_weeks - age_weeks
    #     days_left = average_days - age_weeks
    #     print (f'You have {days_left} days, {weeks_left} weeks, {months_left} and months left.')

    # Time_Left()

# Day 3

    # Starter Challenge

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')