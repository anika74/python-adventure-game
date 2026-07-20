import math

# Taking radius as input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculating the area (Area = pi * r^2)
area = math.pi * (radius ** 2)

# Printing the result (rounded to 2 decimal places using :.2f)
print(f"The area of the circle is: {area:.2f}")