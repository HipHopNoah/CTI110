# Noah Raja
# 3/12/2026
# P3HW2
# Calculating pay

namey = (input("Enter employee's name: "))
hours = float(input("Enter number of hours worked: "))
employra = float(input("Enter employee's pay rate: "))

overtimehoursboo = 0
overtimepaydayyup = 0

if hours > 40:
    normalours = 40
    overtimehoursboo = hours - 40
    overtimepaydayyup = overtimehoursboo * (employra * 1.5)
else:
    normalours = hours

normalpay = normalours * employra
totalpay = normalpay + overtimepaydayyup

print("-------------------------------")
print(f"Employee name:   {namey}")
print()
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<12}')
print("-------------------------------")
print(f'{hours:<15.1f}{employra:<12.1f}{overtimehoursboo:<12.1f}{overtimepaydayyup:<15.2f}${normalpay:<14.2f}${totalpay:<12.2f}')