import math
radius = float(input("Enter the value for the radius: "))
height = float(input("Enter the value for the height: "))

volume = math.pi * (radius ** 2) * height

print("The volume of the cylinder is: {:.2f}".format(volume))

