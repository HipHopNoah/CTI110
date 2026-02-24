# Noah Raja
# 2/24/2026
# P2HW1
# Travel Expenses Displayer

print()
print("This program calculates and displays travel expenses")
print()

budget = float(input("Enter Budget: "))
print()
desti = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
accom = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))

bamwhat = budget - gas - accom - food

print()
print("-------------Travel Expenses------------")
print(f"{'Location:':<21} {desti}")
print(f"{'Initial Budget:':<21} ${budget:.2f}")
print(f"{'Fuel:':<21} ${gas:.2f}")
print(f"{'Accomodation:':<21} ${accom:.2f}")
print(f"{'Food:':<21} ${food:.2f}")
print("----------------------------------------")
print()

print(f"Remaining Balance: ${bamwhat:.2f}")