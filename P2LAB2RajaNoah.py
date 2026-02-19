# Noah Raja
# 2/19/2026
# P2LAB2
# Using a dictionary to store user input

# Create a Dictionary

cars = { "Camaro": 18.21,
        "Prius": 52.36,
        "Model S": 110,
        "Silverado": 26}

keys = cars.keys()

print(keys)
print()

# Get user car
ranchandcucumbers = input("Enter a vehicle to see it's mpg: ")

# Show mpg
barbecuechips = cars[ranchandcucumbers]

print()
print(f"The {ranchandcucumbers} gets {barbecuechips} mpg.")

# Ask for miles
lemonpepperwings = float(input(f"How many miles will you drive the {ranchandcucumbers}: "))

#Math equation
sweattea = lemonpepperwings / barbecuechips

print(f"{sweattea:.2f} gallon(s) of gas are needed to drive the {ranchandcucumbers} {lemonpepperwings} miles.")