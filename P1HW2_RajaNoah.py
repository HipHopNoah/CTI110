# Noah Raja
# 2/12/2026
# P1HW2
# Math for travel expenses

# Creating Variables
print("This program calculates and displays travel expenses")
budget = int(input("Enter Budget: "))
destination = (input("Enter your travel destination: "))
gas = int(input("How much do you think you will spend on gas: "))
hotel = int(input("Approximately, how much will you need for accomodation/hotel: "))
food = int(input("Last, how much do you need for food: "))

# Math equation
tomato = budget - gas - hotel - food 

# Print section 
print("-----Travel Expenses-----")
print()
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accomodation: {hotel}")
print(f"Food: {food}")
print()
print(f"Remaining Baalance: {tomato}")