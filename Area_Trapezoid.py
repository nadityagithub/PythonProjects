# - Ask user for inputs
length_of_top = float(input("Enter the length of the top of the trapezoid: "))
length_of_bottom = float(input("Enter the length of the bottom of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))

# - Perform the Calculation
area = ((length_of_top + length_of_bottom) / 2) * height

# - Print the Answer
print("Your answer is: {:.2f}".format(area))

