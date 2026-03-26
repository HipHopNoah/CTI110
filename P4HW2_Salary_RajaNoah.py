# Noah Raja
# 3/26/2026
# P4HW2
# Calculating pay updated

overtimepaydayyuplist = []
normalpaylist = []
totalpaylist = []
startint = 1

overtimehoursboo = 0
overtimepaydayyup = 0
numberemploy = 0

while startint == 1:
    namey = (input("Enter employee's name or Done to terminate: "))
    if namey != "Done":
        numberemploy = numberemploy + 1
        overtimehoursboo = 0
        overtimepaydayyup = 0
        hours = float(input(f"How many hours did {namey} work? "))
        employra = float(input(f"What is {namey}'s pay rate? "))
        if hours > 40:
            normalours = 40
            overtimehoursboo = hours - 40
            overtimepaydayyup = overtimehoursboo * (employra * 1.5)
            overtimepaydayyuplist.append(overtimepaydayyup)
        else: normalours = hours
        normalpay = normalours * employra
        normalpaylist.append(normalpay)
        totalpay = normalpay + overtimepaydayyup
        totalpaylist.append(totalpay)
        print()
        print("-------------------------------")
        print(f"Employee name:   {namey}")
        print()
        print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<12}')
        print("-------------------------------")
        print(f'{hours:<15.1f}{employra:<12.1f}{overtimehoursboo:<12.1f}{overtimepaydayyup:<15.2f}${normalpay:<14.2f}${totalpay:<12.2f}')
        print()
    if namey == "Done":
        print()
        print(f"Total number of employee entered: {numberemploy}")
        sumovertime = sum(overtimepaydayyuplist)
        print(f"Total amount paid for overtime: {sumovertime}")
        sumregularhou = sum(normalpaylist)
        print(f"Total amount paid for regular hours: {sumregularhou}")
        sumgross = sum(totalpaylist)
        print(f"Total amount paid in gross: {sumgross}")
        startint = 2

