# Noah Raja
# 2/17/2026
# P2LAB1
# Calculating parameters of a circle

import math

# Creating Variables
radius = float(input("What is the radius of the circle? "))

# Equations
diameter = 2 * radius
circu = 2 * math.pi * radius
areaa = math.pi * math.pow(radius, 2)

# Print
print()
print(f"The diameter of the circle is: {diameter:.1f}")
print()
print(f"The circumference of the circle is: {circu:.2f}")
print()
print(f"The area of the circle is: {areaa:.3f}")
