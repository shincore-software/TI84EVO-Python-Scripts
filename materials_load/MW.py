# Solve Mw. Molecular weights: g/mol. Fractions have no units.
# xi*Mi^2 - Mw*xi*Mi + b - Mw*a = 0.
from math import sqrt
print("Mi and Mw: g/mol. Fractions sum to 1.")
print("1: Mw, mole fractions")
print("2: Mi, mole fractions")
print("3: xi, mole fractions")
print("4: Mw, weight fractions")
print("5: Mi, weight fractions")
print("6: wi, weight fractions")
mode = input("Select 1-6: ")
if mode in ("1", "2", "3", "4", "5", "6"):
    n = int(input("Number of components: "))
    if n < 1 or n > 20:
        print("Use 1 to 20 components")
        n = 0
    mole = mode in ("1", "2", "3")
    solve_m = mode in ("2", "5")
    solve_f = mode in ("3", "6")
    solve_avg = mode in ("2", "3", "5", "6")
    k = -1
    known = 0.0
    if solve_avg:
        k = int(input("Unknown component (1 to n): ")) - 1
        known = float(input("Mw (g/mol): "))
    masses = []
    fractions = []
    valid = n > 0 and (not solve_avg or (0 <= k < n and known > 0))
    for i in range(n):
        print("Component:")
        print(i + 1)
        m = 0.0 if solve_m and i == k else float(input("Mi (g/mol): "))
        f = 0.0 if solve_f and i == k else float(input("xi (no units): " if mole else "wi (no units): "))
        if not (solve_m and i == k) and m <= 0:
            valid = False
        if f < 0 or f > 1:
            valid = False
        masses.append(m)
        fractions.append(f)
    if valid and solve_f:
        fractions[k] = 1.0 - sum(fractions)
        valid = 0 <= fractions[k] <= 1
    if abs(sum(fractions) - 1.0) > 0.001:
        valid = False
    if not valid:
        print("Check masses, fractions, and selection")
    else:
        if mole:
            a = 0.0
            b = 0.0
            for i in range(n):
                a = a + fractions[i] * masses[i]
                b = b + fractions[i] * masses[i] ** 2
            avg = b / a if a > 0 else 0.0
        else:
            avg = 0.0
            for i in range(n):
                avg = avg + fractions[i] * masses[i]
        if mode in ("1", "4"):
            print("Mw (g/mol):")
            print(avg)
        elif solve_f:
            if mole:
                predicted = avg
                if abs(predicted - known) > 0.000001 * max(1.0, abs(known)):
                    print("Mw and fractions do not agree")
                else:
                    print("xi (no units):")
                    print(fractions[k])
            elif masses[k] <= 0:
                print("Mi must be positive")
            else:
                other = 0.0
                for i in range(n):
                    if i != k:
                        other = other + fractions[i] * masses[i]
                value = (known - other) / masses[k]
                if value < 0 or value > 1 or abs(value - fractions[k]) > 0.001:
                    print("No valid wi")
                else:
                    print("wi (no units):")
                    print(value)
        elif fractions[k] == 0:
            print("Zero fraction: Mi has no unique value")
        elif not mole:
            other = 0.0
            for i in range(n):
                if i != k:
                    other = other + fractions[i] * masses[i]
            result = (known - other) / fractions[k]
            if result <= 0:
                print("No positive Mi")
            else:
                print("Mi (g/mol):")
                print(result)
        else:
            disc = known ** 2 - 4.0 * (b - known * a) / fractions[k]
            if disc < 0:
                print("No real Mi")
            else:
                r1 = (known + sqrt(disc)) / 2.0
                r2 = (known - sqrt(disc)) / 2.0
                if r1 <= 0:
                    print("No positive Mi")
                else:
                    print("Mi (g/mol):")
                    print(r1)
                    if r2 > 0 and abs(r2-r1) > 0.000001 * max(1.0, abs(r1)):
                        print("Second valid Mi (g/mol):")
                        print(r2)
else:
    print("Select 1-6")
