import random

choices = ['rock', 'paper', 'scissors']
tie = "It is a tie."
lost = "You have lost."
won = "Congrats, you have won!"
#row is the user and column is the computer
outcomes = [[tie, lost, won],
			[won, tie, lost],
	        [lost, won, tie]]

human_score = 0
comp_score = 0
while True:
	try:
		user_choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
		print("You chose", choices[user_choice - 1])
	except ValueError:
		print("You have chosen an invalid value. Enter integers only. Please Try again.")
		continue	
	except IndexError:
		print("You have entered a number that is not a choice. Try again.")
		continue	
	
	comp_choice = random.randint(1, 3)
	print("Computer chose", choices[comp_choice - 1])
	outcome = outcomes[user_choice - 1][comp_choice - 1]
	print(outcome)
	
	if outcome == won:
		human_score += 1
	elif outcome == lost:
		comp_score += 1
	print("You have:", human_score, "points.\nThe Computer has:", comp_score, "points.")
	
	if human_score == 2 or comp_score == 2:
		break

print("Thank you for playing!")

