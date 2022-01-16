import math
radius = float(input("Enter the value for the radius: "))
height = float(input("Enter the value for the height: "))

surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

print("The surface area of the cylinder is: {:.2f}".format(surface_area))