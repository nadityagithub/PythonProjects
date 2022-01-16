import random
while True:
	roll = random.randint(1, 6)
	print("You have rolled a", roll)
	roll_again = input("Would you like to roll again? Enter Y or N: ").upper()
	if roll_again == "N":
		print("Goodbye!")
		break
