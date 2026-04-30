# Noah Raja
# 4/28/2026
# Final Project
# Puffin catching fish game
# the more rarer the harder it is to catch it
import random
import time

def makingcharacter():
    name = input("Enter Puffin's name: ")
    energy = 50
    character = {'name': name, 'energy': energy}
    print(f"{name} is ready to hunt for fish!")
    return character, energy

def showcharacterinven(character):
    for char in character:
        print(f"Name: {char['name']}, Energy: {char['energy']}")

def raritychooser():
    raritynumber = round(random.uniform(1,5))
    if raritynumber == 1:
        typeofrarity = ("common")
        decidingfactor = input("A common fish has spawned! Would you like to try to catch it? (Yes/No): ")
        if decidingfactor == ("Yes"):
            print("Catching in process... (You have a 75% success rate)")
            randomnumber = random.randint(1,3)
            if randomnumber <= 2:
                time.sleep(3)
                print("Congrats you have caught the fish! Your inventory has been updated.")
            if randomnumber >= 2:
                time.sleep(3)
                print("You failed ")
                print(randomnumber)
    elif raritynumber == 2:
        typeofrarity = ("uncommon")
        decidingfactor = input("An uncommon fish has spawned! Would you like to try to catch it? (Yes/No): ")
        if decidingfactor == ("Yes"):
            print("Catching in process... (You have a 50% success rate)")
            randomnumber = random.randint(1,2)
            if randomnumber == 1:
                time.sleep(3)
                print("Congrats you have caught the fish! Your inventory has been updated.")
            if randomnumber != 1:
                time.sleep(3)
                print("You failed")
                print(randomnumber)
    elif raritynumber == 3:
        typeofrarity = ("rare")
        decidingfactor = input("A rare fish has spawned! Would you like to try to catch it? (Yes/No): ")
        if decidingfactor == ("Yes"):
            print("Catching in process... (You have a 25% success rate)")
            randomnumber = random.randint(1,4)
            if randomnumber == 1:
                time.sleep(3)
                print("Congrats you have caught the fish! Your inventory has been updated.")
            if randomnumber != 1:
                time.sleep(3)
                print("You failed")
                print(randomnumber)
    elif raritynumber == 4:
        typeofrarity = ("ultra rare")
        decidingfactor = input("An ultra rare fish has spawned! Would you like to try to catch it? (Yes/No): ")
        if decidingfactor == ("Yes"):
            print("Catching in process... (You have a 10% success rate)")
            randomnumber = random.randint(1,10)
            if randomnumber == 1:
                time.sleep(3)
                print("Congrats you have caught the fish! Your inventory has been updated.")
            if randomnumber != 1:
                time.sleep(3)
                print("You failed")
                print(randomnumber)
    elif raritynumber == 5:
        typeofrarity = ("legendary")
        decidingfactor = input("A legendary fish has spawned! Would you like to try to catch it? (Yes/No): ")
        if decidingfactor == ("Yes"):
            print("Catching in process... (You have a 5% success rate)")
            randomnumber = random.randint(1,20)
            if randomnumber == 1:
                time.sleep(3)
                print("Congrats you have caught the fish! Your inventory has been updated.")
            if randomnumber != 1:
                time.sleep(3)
                print("You failed")
                print(randomnumber)


if __name__ == "__main__":
    makingcharacter()
    showcharacterinven(character)
    print()
    raritychooser()
    print()
    playagain = input("Would you like to dive back into the water? (Yes/No): ")
    for playagain in ("Yes"):
        raritychooser()
        playagain = input("Would you like to dive back into the water? (Yes/No): ")
