import random
counters = [0, 0, 0, 0, 0, 0]
numtimes = 600
for x in range(numtimes):
	roll = random.randint(1, 6)
	counters[roll - 1] += 1
for x in range(6):
	print("Number of times", x + 1, "was rolled is", counters[x], "\nPercentage is", counters[x]/numtimes)

"""
print("Number of times 1 was rolled is", counters[0], "\nPercentage is ", counters[0]/numtimes)
print("Number of times 2 was rolled is", counters[1], "\nPercentage is ", counters[1]/numtimes)
print("Number of times 3 was rolled is", counters[2], "\nPercentage is ", counters[2]/numtimes)
print("Number of times 4 was rolled is", counters[3], "\nPercentage is ", counters[3]/numtimes)
print("Number of times 5 was rolled is", counters[4], "\nPercentage is ", counters[4]/numtimes)
print("Number of times 6 was rolled is", counters[5], "\nPercentage is ", counters[5]/numtimes)
"""

print("Goodbye!")

