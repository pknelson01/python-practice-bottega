class Wallet():
    def __init__(self, name, balance = 0, done = False):
        self.name = name
        self.balance = balance
        self.done = done

    def add_funds(self):
        amount = int(input("How much would you like to deposit? $"))
        self.balance += amount

        print(f'You\'ve added ${amount} to your account. Your new balance is ${self.balance}')

        answer = input("Add more funds? ")

        if answer == "yes" or answer == "y":
            self.add_funds()
        elif answer == "no" or answer == "n":
            self.main_menu()
        else:
            "That is not a proper response, please respond with either yes or no."
            self.add_funds()

    def withdraw_funds(self):
        amount = int(input("How much would you like to withdraw? $"))
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f'You don\'t have enough funds to withdraw ${amount}, your current balance is {self.balance}')
            self.withdraw_funds()

        answer = input("Withdraw more funds? ")

        if answer == "yes" or answer == "y":
            self.withdraw_funds()
        elif answer == "no" or answer == "n":
            self.main_menu()
        # else:
        #     answer != "yes" or answer != "y" or answer != "no" or answer != "n":
        #     print(f'That is not a proper response, please respond with either yes or no. respond with "ok" to go back')
        #     self.withdraw_funds()

    def check_balance(self):
        print(f'Your current balance is ${self.balance}')

        answer = input("Main Menu? ")

        if answer == "yes" or answer == "y":
            self.main_menu()
        else:
            self.exit()

    def exit(self):
        answer = input("Are you finished? ")

        if answer == "yes" or answer == "y":
            self.done = True
        elif answer == "no" or answer == "n":
            self.main_menu()

    def main_menu(self):
        menu = int(input(f"""
        Hello {self.name}, Welcome to your virtual wallet!

        1. Add Funds
        2. Withdraw Funds
        3. Check Balance
        4. Exit
        """))

        if menu == 1 :
            self.add_funds()
        elif menu == 2:
            self.withdraw_funds()
        elif menu == 3:
            self.check_balance()
        elif menu == 4:
            self.exit()


name = input("Hello, what is your name? ")
user = Wallet(name)

while user.done == False:
    user.main_menu()