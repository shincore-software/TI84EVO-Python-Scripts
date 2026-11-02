# Solve M = DP * Mbar. Use one average type throughout.
print("Use Mn with DPn or Mw with DPw.")
print("Mass values: g/mol. DP: no units.")
print("1: DP  2: M  3: Mbar")
mode = input("Select 1-3: ")
if mode in ("1", "2", "3"):
    valid = True
    if mode != "1":
        DP = float(input("DP (no units): "))
        valid = DP > 0
    if mode != "2":
        M = float(input("M (g/mol): "))
        valid = valid and M > 0
    if mode != "3":
        print("1: Enter Mbar  2: Mer mixture")
        method = input("Select 1 or 2: ")
        if method == "1":
            Mbar = float(input("Mbar (g/mol): "))
            valid = valid and Mbar > 0
        elif method == "2":
            n = int(input("Number of mer types: "))
            Mbar = 0.0
            total = 0.0
            valid = valid and n > 0
            for i in range(n):
                x = float(input("Mer fraction (no units): "))
                mass = float(input("Mer mass (g/mol): "))
                valid = valid and x >= 0 and mass > 0
                total = total + x
                Mbar = Mbar + x * mass
            valid = valid and abs(total - 1) <= 0.001
        else:
            valid = False
    if not valid:
        print("Need positive masses and DP.")
        print("Fractions: non-negative, sum 1.")
    elif mode == "1":
        print("DP (no units):")
        print(M / Mbar)
    elif mode == "2":
        print("M (g/mol):")
        print(DP * Mbar)
    else:
        print("Mbar (g/mol):")
        print(M / DP)
else:
    print("Select 1-3")
