# Noah Raja
# 4/28/2026
# Final Project
# Puffin catching fish game
# the more rarer the harder it is to catch it
import random
import time

def makingcharacter():
    name = input("Enter Puffin's name: ")
    character = {'name': name, 'energy': 50, 'inventory': []}
    print(f"{name} is ready to hunt for fish!")
    return character

def showcharacterinven(character):
    print("Current Sates")
    print(f"Name: {character['name']}")
    print(f"Energy: {character['energy']}")
    print(f"Fish: {(character['inventory'])}")

def raritychooser(character):
    character ['energy'] -= 10
    raritynumber = random.randint(1,5)
    fishtypes = {
        1: ("Common", 100, 1), 2: ("Uncommon", 50, 2), 3: ("Rare", 25, 4), 4: ("Ultra rare", 10, 10), 5: ("Legendary", 5, 20)
    }
    rarityname, percent, chancemax = fishtypes[raritynumber]
    decidingfactor = input(f"A {rarityname} fish has spawned! (Energy: {character['energy']}) Catch it? (Yes/No): ")
    if decidingfactor == ("Yes"):
        print(f"Catching in process... (You have a {percent}% success rate)")
        time.sleep(1.5)
        if random.randint(1, chancemax) == 1:
            print(f"Congrats! You caught a {rarityname} fish!")
            character['inventory'].append(rarityname)
        else:
            print("The fish swam away...")
    else:
        print("You went to sleep for some reason...")
        character ['energy'] += 10

if __name__ == "__main__":
    my_puffin = makingcharacter()
    playing = True
    while playing and my_puffin['energy'] > 0:
        showcharacterinven(my_puffin)
        print()
        raritychooser(my_puffin)
        print()
        if my_puffin['energy'] <= 0:
            print()
            print("You're too tired to fish anymore! Time for a nap.")
            playing = False
        else:
            print()
            choice = input("Would you like to dive back in? (Yes/No): ")
            if choice == "Yes":
                playing = True
            if choice == "No":
                playing = False
    print()
    print("--- Final Results ---")
    showcharacterinven(my_puffin)
    print("Thanks for playing!")
