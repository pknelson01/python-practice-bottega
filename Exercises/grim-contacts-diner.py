# Grim
    # import random

    # def grim(years, cod):
    #     return str(f"You have {years} years left to live and your cause of death will be because {cod}.")

    # years = random.randint(2, 50)
    # cod = [
    #     'The death star just came into orbit',
    #     'Some jedi wasn\'t granted the rank of master and you happen to be a youngling',
    #     'of the Sarlacc Pit',
    #     'You accused Chewey of cheating'
    #     ]

    # random_cod = random.choice(cod)
    # print (grim(years, random_cod))

# Contacts

    # class Contacts():
    #     def __init__(self, name, number = str, address = str, done = False):
    #         self.number = number
    #         self.address = address
    #         self.name = name
    #         self.done = done

    #     def p_address(self):
    #         addy = input('What is your address? ')
    #         self.address = addy

    #         answer = input(f'You entered {addy}, is that correct? ')
    #         if answer == "yes" or answer == "y":
    #             self.main_menu()
    #         elif answer == "no" or answer == "n":
    #             self.p_address()


    #     def p_number(self):
    #         digits = input('What is your number? ')
    #         self.number = digits

    #         answer = input(f'You entered {digits}, is that correct? ')
    #         if answer == "yes" or answer == "y":
    #             self.main_menu()
    #         elif answer == "no" or answer == "n":
    #             self.p_number()

    #     def info(self):
    #         print(f'Your info is:\n {self.name}\n {self.number}\n {self.address}')
    #         answer = input('m = Main Menu x = Exit ')
    #         if answer == "m":
    #             self.main_menu()
    #         elif answer == "x":
    #             self.done = True

    #     def exit(self):
    #         answer = input("Are you done here? yes or no.\n")

    #         if answer == "yes":
    #             self.done = True
    #         elif answer == "no":
    #             self.main_menu()

    #     def main_menu(self):
    #         menu = int(input(f"""
    #         Hello There, {self.name}!
    #         1. Address
    #         2. Number
    #         3. Show User Info
    #         4. Exit
    #         """))

    #         if menu == 1:
    #             self.p_address()
    #         if menu == 2:
    #             self.p_number()
    #         if menu == 3:
    #             self.info()
    #         if menu == 4:
    #             self.p_name()
            


    # name = input("Hello, what is your name? \n")
    # user = Contacts(name)

    # while user.done != True:
    #     user.main_menu()

# Diner

from decimal import Decimal

class Diner():
    def __init__(self, name, entrees = 0, sides = 0, desserts = 0, total = 0, receipt = 0, wallet = 100, done = False):
        self.entrees = entrees
        self.sides = sides
        self.desserts = desserts
        self.total = total
        self.done = done
        self.receipt = receipt
        self.wallet = wallet

    def full_course(self):
        answer = int(input("""
        Entrees:
        1. Grilled Chicken - 12
        2. Sirloin Steak - 17
        3. Salmon - 15
        """))

        chicken = 12
        steak = 17
        salmon = 15

        if answer == 1:
            self.entrees += chicken
        if answer == 2:
            self.entrees += steak
        if answer == 3:
            self.entrees += salmon

        answer_2 = int(input(f"""
        You chose {answer}, is this correct?
        1. Yes
        2. No 
        """))

        if answer_2 == 1:
            self.main_menu_2()
        elif answer_3 == 2:
            self.full_course()
        else:
            self.full_course()

    def side_dish(self):
        answer = int(input("""
        Sides:
        1. Fries - 3
        2. Caesar Salad - 6
        3. Loaded Potato - 4
        """))

        fries = 3
        salad = 6
        potato = 4

        if answer == 1:
            self.sides += fries
        if answer == 2:
            self.sides += salad
        if answer == 3:
            self.sides += potato

        answer_2 = int(input(f"""
        You chose {answer}, is this correct? 
        1. Yes
        2. No
        """))

        if answer_2 == 1:
            self.main_menu_2()
        elif answer_3 == 2:
            self.side_dish()
        else:
            self.side_dish()

    def sweets(self):
        answer = int(input("""
        Sides:
        1. Pazooki - 7
        2. Molten Chocolate Cake - 5
        3. Cheesecake - 5
        """))

        pazooki = 7
        cake = 5
        cheese_cake = 5

        if answer == 1:
            self.desserts += pazooki
        if answer == 2:
            self.desserts += cake
        if answer == 3:
            self.desserts += cheese_cake

        answer_2 = int(input(f"""
        You chose {answer}, is this correct? 
        1. Yes
        2. No
        """))

        if answer_2 == 1:
            self.main_menu_2()
        elif answer_3 == 2:
            self.sweets()
        else:
            self.sweets()

    def order_summary(self):
        print(f"""
        Your order:
        {self.entrees}
        {self.sides}
        {self.desserts}
        """)
        answer = str(input("""
        Back to main menu?
        yes or no.
        """))

        if answer == "yes":
            self.main_menu_2()
        elif answer == "no":
            self.order_summary()

    def payment(self):
        sub_total = self.entrees + self.sides + self.desserts
        tax = sub_total * 0.06
        total = sub_total + tax
        tip = total * 0.15
        grand_total = total + tip
        
        answer = input(f"""
        Your total is ${round(total, 2)}:
        Would you like to add a 15% tip?
        yes or no.
        """)
        if answer == "yes":
            self.receipt += grand_total

            answer_2 = (input(f"""
            Your new total is ${round(grand_total, 2)}:
            enter ' p ' to pay
            """))
            if answer_2 == 'p':
                self.wallet -= grand_total
            else:
                self.payment()

            answer_3 = input(f"""
            You have ${self.wallet} left in your wallet.
            Would you like to exit?
            x = exit, m = main menu
            """)

            if answer_3 == "x":
                self.done = True
            elif answer_3 == "m":
                self.main_menu_2()
        elif answer == "no":
            self.receipt += total

            answer_4 = (input(f"""
            Your new total is ${round(total, 2)}:
            enter ' p ' to pay
            """))
            if answer_4 == 'p':
                self.wallet -= total
            else:
                self.payment()

            answer_5 = input(f"""
            You have ${self.wallet} left in your wallet.
            Would you like to exit?
            x = exit, m = main menu
            """)

            if answer_5 == "x":
                self.done = True
            elif answer_5 == "m":
                self.main_menu_2()

    def exit(self):
        answer = input("""
        Thank you for dining with us today!
        press ' x ' to exit.
        """)
        if answer == "x":
            self.done = True
        else:
            self.main_menu_2()

    def main_menu(self):
        menu = int(input(f"""
        Welcome {name}! my name is Dex.
        What can I get for you?

        menu:
        1. Entrees
        2. Sides
        3. Desserts
        4. Order Summary
        5. Checkout
        6. Exit

        You have ${self.wallet} in your wallet
        """))

        if menu == 1:
            self.full_course()
        if menu == 2:
            self.side_dish()
        if menu == 3:
            self.sweets()
        if menu == 4:
            self.order_summary()
        if menu == 5:
            self.payment()
        if menu == 6:
            self.exit()

    def main_menu_2(self):
        menu = int(input("""
        Menu:

        1. Entrees
        2. Sides
        3. Desserts
        4. Order Summary
        5. Checkout
        6. Exit
        """))

        if menu == 1:
            self.full_course()
        if menu == 2:
            self.side_dish()
        if menu == 3:
            self.sweets()
        if menu == 4:
            self.order_summary()
        if menu == 5:
            self.payment()
        if menu == 6:
            self.exit()

name = input("What's the name on the reservation? ")
user = Diner(name)

while user.done != True:
    user.main_menu()