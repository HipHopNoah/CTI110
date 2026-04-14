# Noah Raja
# 3/24/2026
# P4HW1
# Calculating stats for an amount of scores

# Creating list
print()
numbers = []
# Getting score input from the user and seeing if it is viable
for scorecount in range(int(input("How many scores do you want to enter? "))):
    scorecount = scorecount + 1
    actscore = float(input(f"Enter score #{scorecount}: "))
    while actscore < 0 or actscore > 100:
        print()
        print("INVALID Score entered")
        print("Score should be between 0 and 100")
        actscore = float(input(f"Enter score #{scorecount} again: "))
    numbers.append(actscore)
    scorecount = scorecount + 1


# Getting smallest grade and the average grade
smallestnum = min(numbers)

# Removing the lowest grade
numbers.remove(min(numbers))

avgnum = sum(numbers)/len(numbers)

# Numerical grade calculation
if avgnum >= 90:
    gradeavg = ("A")
elif avgnum >= 80:
    gradeavg = ("B")
elif avgnum >= 70:
    gradeavg = ("C")
elif avgnum < 70:
    gradeavg = ("F")

print()
# Section for printing out the results with certain formatting
print("------------Results------------")
print(f"{'Lowest score':<20}: {smallestnum}")
print(f"{'Modified List':<20}: {numbers}")
print(f"{'Scores Average':<20}: {avgnum:.2f}")
print(f"{'Grade':<20}: {gradeavg}")
print("-------------------------------")
