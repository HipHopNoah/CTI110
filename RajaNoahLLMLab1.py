def cat_personality_picker():
    # Dictionary storing cat data for easy lookup
    cats = {
        "1": ("Sitta", "You are very laid back and you need a sweet treat once in a while", "Brown"),
        "2": ("Mookie", "You listen to peoples conversations and you move quickly to any destination", "Orange"),
        "3": ("Oliver", "You love having one best friend and are loud when they aren't around", "White and Orange"),
        "4": ("Moses", "You go where you want and your territorial when people are near your food or walk into you", "Gray/Black"),
        "5": ("Bucc", "Your injuries will never stop you and you love food even though you ate a minute ago", "Orange"),
        "6": ("Sam", "You can survive in the wilderness and you love to play with any cat", "Gray"),
        "7": ("Francesca", "You are fearless and love to explore anything no matter the risk", "White and Black"),
        "8": ("Henry", "You're intrigued by new things but are careful when approaching", "Gray")
    }

    while True:
        print("\n--- Pick a number 1-8 to be assigned to a cat ---")
        user_input = input("Enter a number: ").strip()

        # Check if the user wants to quit immediately
        if user_input.lower() == "done":
            print("Thanks for playing! Goodbye.")
            break

        # Check if the input is a valid number from the list
        if user_input in cats:
            name, personality, fur = cats[user_input]
            print(f"\nYou picked {name}!")
            print(f"Personality: {personality}")
            print(f"Fur color: {fur}")

            # Ask if it matches
            match = input("\nDoes this match your personality? (yes/no): ").strip().lower()
            
            if match == "yes":
                print("That's awesome! It's a perfect match.")
            
            # Ask if they want to try again
            retry = input("Would you like to pick again? (Type 'Done' to end or 'Yes' to continue): ").strip()
            if retry.lower() == "done":
                print("Thanks for playing! Goodbye.")
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    cat_personality_picker()
