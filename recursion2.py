def ask_for_int(low, high):
	while True:
		try:
			user_input = int(input("Enter a number between 0 and 996: "))
			if user_input >= low and user_input <= high:
				return user_input
			else:	
				print("Your number is not between the range. Please try again.")
		except ValueError:
			print("Oops! Your input is not a number. Please try again.")
def factorial(num):
	if num == 0:
		return 1
	return num * factorial(num-1)
def main():
	print("Hello")
	while True:
		user_input = ask_for_int(0, 996)
		print("You have entered a valid number:", user_input)
		result = factorial(user_input)
		print(result)
		again = input("Would you like to go again? Y or N: ").upper()
		if again == "N":
			print("Goodbye!")
			break
		
main()
				
