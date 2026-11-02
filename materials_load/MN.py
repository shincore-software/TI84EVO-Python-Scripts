# Number-average molecular weight
# Solve one molecular-weight value. Mass units: g/mol.
from math import sqrt

AVERAGE = "Mn"
print("Mass values: g/mol.")
print("Fractions: no units; sum to 1.")
print('1: Average')
print('2: One Mi')
print("3: One xi (use sum xi=1)")
mode = input("Select 1-3: ")
if mode in ("1", "2", "3"):
    n = int(input("Number of components: "))
    if n < 1 or n > 20:
        print("Use 1 to 20 components")
        n = 0
    k = -1
    known = 0.0
    if mode != "1":
        k = int(input("Unknown component (1 to n): ")) - 1
        known = float(input(AVERAGE + " (g/mol): "))
    masses = []
    fractions = []
    valid = n > 0 and (mode == "1" or (0 <= k < n and known > 0))
    for i in range(n):
        print("Component:" + "\n" + str(i + 1))
        m = 0.0 if mode == "2" and i == k else float(input("Mi (g/mol): "))
        x = 0.0 if mode == "3" and i == k else float(input("xi (no units): "))
        if not (mode == "2" and i == k) and m <= 0:
            valid = False
        if x < 0 or x > 1:
            valid = False
        masses.append(m)
        fractions.append(x)
    if valid and mode == "3":
        fractions[k] = 1.0 - sum(fractions)
        valid = 0 <= fractions[k] <= 1
    if abs(sum(fractions) - 1) > 0.001:
        valid = False
    if not valid:
        print('Check masses, fractions, and\nselection')
    else:
        a = 0.0
        b = 0.0
        for i in range(n):
            a = a + fractions[i] * masses[i]
            b = b + fractions[i] * masses[i] ** 2
        if mode == "1":
            print(AVERAGE + " (g/mol):" + "\n" + str(a if AVERAGE == "Mn" else b / a))
        elif mode == "3":
            predicted = a if AVERAGE == "Mn" else b / a
            if abs(predicted - known) > 0.000001 * max(1.0, abs(known)):
                print('Average and fractions do not\nagree')
            else:
                print("xi (no units):" + "\n" + str(fractions[k]))
        elif fractions[k] == 0:
            print('Zero fraction: Mi has no\nunique value')
        elif AVERAGE == "Mn":
            result = (known - a) / fractions[k]
            if result <= 0:
                print("No positive Mi")
            else:
                print("Mi (g/mol):" + "\n" + str(result))
        else:
            # x*M*M - Mw*x*M + b - Mw*a = 0.
            disc = known ** 2 - 4 * (b - known * a) / fractions[k]
            if disc < 0:
                print("No real Mi")
            else:
                r1 = (known + sqrt(disc)) / 2
                r2 = (known - sqrt(disc)) / 2
                if r1 <= 0:
                    print("No positive Mi")
                else:
                    print("Mi (g/mol):" + "\n" + str(r1))
                    if r2 > 0 and r2 != r1:
                        print("Second valid Mi (g/mol):" + "\n" + str(r2))
else:
    print("Select 1-3")
