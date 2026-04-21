# Noah
# 4/19/2026
# P5LAB
# Money change calculator functions

import random

def disperse_change(changemoney):
    ahund = changemoney
    ahund = ahund * 100
    dolla = int(ahund // 100)
    quarterstart = ahund - dolla * 100
    quarters = int(quarterstart // 25)
    dimestart = ahund - (dolla * 100) - (quarters * 25)
    dimes = int(dimestart // 10)
    nickelstart = ahund - (dolla * 100) - (quarters * 25) - ( dimes * 10 )
    nickles = int(nickelstart // 5)
    pennystart = ahund - (dolla * 100) - (quarters * 25) - ( dimes * 10 ) - (nickles * 5)
    pennys = int(pennystart // 1)

    if ahund == 0:
        print("No change")

    if dolla > 0:
        if dolla == 1:
            print (f"{dolla} Dollar")
        else:
            print (f"{dolla} Dollars")

    if quarters > 0:
        if quarters == 1:
            print (f"{quarters} Quarter")
        else:
            print (f"{quarters} Quarters")

    if dimes > 0:
        if dimes == 1:
            print (f"{dimes} Dime")
        else:
            print (f"{dimes} Dimes")

    if nickles > 0:
        if nickles == 1:
            print (f"{nickles} Nickle")
        else:
            print (f"{nickles} Nickles")

    if pennys > 0:
        if pennys == 1:
            print (f"{pennys} Penny")
        else:
            print (f"{pennys} Pennies")
    pass


def calculations():
    randommoney = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${randommoney}")
    howmuchcash = float(input("How much cash will you put in the self-checkout?: "))
    changemoney = round(howmuchcash - randommoney, 2)
    print(f"Change is: ${changemoney:.2f}")
    print()
    disperse_change(changemoney)

calculations()