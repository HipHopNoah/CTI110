# Noah Raja
# 3/17/2026
# P4LAB1
# Creating a multipication program

minccino = 0
radish = 1
potatochips = 0

while potatochips != 1:
    koreansweetandspicyfriedchicken = int(input("Enter an integer: "))
    if koreansweetandspicyfriedchicken < 0:
        print("This program does not handle negative number")
        radish = 13
    if koreansweetandspicyfriedchicken > 0:
        print()
        for multiplication in range(12):
            minccino = koreansweetandspicyfriedchicken * radish
            print(f"{koreansweetandspicyfriedchicken} * {radish} = {minccino}")
            radish = radish + 1
    if radish > 12:
        print()
        asking = (input("Would you like to run the program again? "))
        print()
        if asking == "yes":
            minccino = 0
            radish = 1
            potatochips = 0
        if asking == "no":
            potatochips = 1
            print("Exiting program...")