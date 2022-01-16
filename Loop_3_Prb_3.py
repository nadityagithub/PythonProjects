import random
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
for x in range(600):
	roll = random.randint(1, 6)
	if roll == 1:
		one += 1
	elif roll == 2:
		two += 1	
	elif roll == 3:
		three += 1
	elif roll == 4:
		four += 1
	elif roll == 5:
		five += 1
	elif roll == 6:
		six += 1
print("Number of times 1 was rolled is", one, "\nPercentage is ", one/600)
print("Number of times 2 was rolled is", two, "\nPercentage is ", two/600)
print("Number of times 3 was rolled is", three, "\nPercentage is ", three/600)
print("Number of times 4 was rolled is",four, "\nPercentage is ", four/600)
print("Number of times 5 was rolled is", five, "\nPercentage is ", five/600)
print("Number of times 6 was rolled is", six, "\nPercentage is ", six/600)
print("Goodbye!")

