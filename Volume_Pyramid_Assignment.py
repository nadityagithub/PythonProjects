# - Ask for inputs
length = float(input("Enter the value for the length of the Pyramid: "))
width = float(input("Enter the value for the width of the Pyramid: "))
height = float(input("Enter the value for the height of the Pyramid: "))


# - Perform the calculation
volume = (length * width * height) / 3

# - Print the answer
print("Your volume for the Pyramid is: {:.2f}".format(volume))


