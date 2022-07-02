# Calculator application (would be cool to give fixed amounts to the year, month, and day and after the user plugs in their borthday the application will calculate how many days they have been alive)

class Birthday():
	def __init__(self, name, year = int, month = str, day = int, done = False):
		self.name = name
		self.year = year
		self.month = month
		self.day = day
		self.done = done

	def birth_year(self):
		perrenial = int(input('What year were you born? '))
		self.year = perrenial

		answer = input(f'You entered {perrenial}, is that correct? ')
		if answer == "yes" or answer == "y":
			self.main_menu()
		elif answer == "no" or answer == "n":
			self.birth_year()

	def birth_month(self):
		nov = str(input('In what Month? '))
		self.month = nov

		answer = input(f'You entered {nov}, is that correct? ')
		if answer == "yes" or answer == "y":
			self.main_menu()
		elif answer == "no" or answer == "n":
			self.birth_month()

	def birth_day(self):
		date = int(input('On what day? '))
		self.day = date

		answer = input(f'You entered {date}, is that correct? ')
		if answer == "yes" or answer == "y":
			self.main_menu()
		elif answer == "no" or answer == "n":
			self.birth_day()

	def results(self):
		print(f'Your birthday is {self.month}, {self.day}, {self.year}')
		answer = input('m = Main Menu x = Exit ')
		if answer == "m":
			self.main_menu()
		elif answer == "x":
			self.done = True

	def exit(self):
		answer = input("Are you finished? ")

		if answer == "yes" or answer == "y":
			z = input("""
			Thank you! Have a good rest of your day.
			press ' x ' to exit.
			""")
			if z == "x":
				self.done = True
		elif answer == "no" or answer == "n":
			self.main_menu()
		

	def main_menu(self):
		menu = int(input(f"""
		Hello {self.name}, 
		first bit of information we need to 
		gather is your birthday.

		1. Input Year
		2. Input Month
		3. Input Day
		4. Show Results
		5. Exit
		"""))

		if menu == 1:
			self.birth_year()
		if menu == 2:
			self.birth_month()
		if menu == 3:
			self.birth_day()
		if menu == 4:
			self.results()
		if menu == 5:
			self.exit()

name = input("Hello, what is your name? ")
user = Birthday(name)

while user.done != True:
	user.main_menu()