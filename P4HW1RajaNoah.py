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
    if actscore >= 0 and actscore <=100:
        numbers.append(actscore)
    if actscore < 0 or actscore > 100:
        print()
        print("INVALID Score entered")
        print("Score should be between 0 and 100")
        actscore = float(input(f"Enter score #{scorecount} again: "))
        numbers.append(actscore)
        scorecount = scorecount + 1

# Removing the lowest grade
newnumlist=[x for x in numbers
            if x>min(numbers)]

# Getting smallest grade and the average grade
smallestnum = min(numbers)
avgnum = sum(newnumlist)/len(newnumlist)

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
print(f"{'Modified List':<20}: {newnumlist}")
print(f"{'Scores Average':<20}: {avgnum:.2f}")
print(f"{'Grade':<20}: {gradeavg}")
print("-------------------------------")
