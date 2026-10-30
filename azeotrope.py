# Binary azeotrope checks.
from math import log

print("Mode:")
print("1: Check for an azeotrope")
print("2: Margules azeotrope x1")
mode = input("Select 1 or 2: ")

if mode == "1":
    p1 = float(input("Psat 1: "))
    p2 = float(input("Psat 2: "))
    g1 = float(input("gamma1 infinite dilution: "))
    g2 = float(input("gamma2 infinite dilution: "))
    if p1 <= 0 or p2 <= 0:
        print("Psat values must be positive")
    else:
        a0 = g1 * p1 / p2
        a1 = p1 / (g2 * p2)
        print("alpha at x1=0:")
        print(a0)
        print("alpha at x1=1:")
        print(a1)
        if (a0 > 1 and a1 < 1) or (a0 < 1 and a1 > 1):
            print("Azeotrope predicted")
        else:
            print("Test does not predict azeotrope")
elif mode == "2":
    p1 = float(input("Psat 1: "))
    p2 = float(input("Psat 2: "))
    A = float(input("Margules A: "))
    if p1 <= 0 or p2 <= 0 or A == 0:
        print("Need positive Psat and non-zero A")
    else:
        x1 = 0.5 + log(p1 / p2) / (2.0 * A)
        print("Azeotrope x1:")
        print(x1)
        if x1 < 0 or x1 > 1:
            print("Result is outside 0 to 1")
else:
    print("Select 1 or 2")
