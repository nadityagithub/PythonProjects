import random

while True:
		while True:
			user_choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
			if user_choice == 1:
				print("You chose Rock.")
				break
			elif user_choice == 2:
				print("You chose Paper.")
				break
			elif user_choice == 3:
				print("You chose Scissors.")
				break
			else:
				print("Invalid Choice. Please choose again!")
		comp_choice = random.randint(1, 3)
		if comp_choice == 1:
			print("The computer chose Rock.")
		elif comp_choice == 2:	
			print("The computer chose Paper.")
		else:
			print("The computer chose Scissors.")
		tie_message = "It is a tie. Try again."
		lost_message = "The computer has won. Try again."
		won_message = "You have won!"

		if user_choice == 1 and comp_choice == 1:
			print(tie_message)
		elif user_choice == 1 and comp_choice == 2:
			print(lost_message)
		elif user_choice == 1 and comp_choice == 3:
			print(won_message)
			break
		elif user_choice == 2 and comp_choice == 1:
			print(won_message)
			break
		elif user_choice == 2 and comp_choice == 2:
			print(tie_message)
		elif user_choice == 2 and comp_choice == 3:
			print(lost_message)
		elif user_choice == 3 and comp_choice == 1:
			print(lost_message)
		elif user_choice == 3 and comp_choice == 2:
			print(won_message)
			break
		else:
			print(tie_message)
		
print("Thank you for playing!")


