# Noah Raja
# 2/26/2026
# P2HW2
# Calculating a Gradebook

moduleuno = float(input("Enter grade for Module 1: "))
print()
moduledos = float(input("Enter grade for Module 2: "))
print()
moduletres = float(input("Enter grade for Module 3: "))
print()
modulecuatro = float(input("Enter grade for Module 4: "))
print()
modulecinco = float(input("Enter grade for Module 5: "))
print()
moduleseis = float(input("Enter grade for Module 6: "))
print()

modules = [moduleuno, moduledos, moduletres, modulecuatro, modulecinco, moduleseis]

flyinghawaiianpizzafromVsPizzaWhewItsSoGood = min(modules)
HiTeacherHaveAGreatDay = max(modules)
BamWhat = sum(modules)
ImCrine = len(modules)
Averauge = BamWhat/ImCrine

print("------------Results------------")

print(f"{'Lowest Grade:':<21} {flyinghawaiianpizzafromVsPizzaWhewItsSoGood:.1f}")
print(f"{'Highest Grade:':<21} {HiTeacherHaveAGreatDay:.1f}")
print(f"{'Sum of Grades:':<21} {BamWhat:.1f}")
print(f"{'Average:':<21} {Averauge:.2f}")

print("-------------------------------")