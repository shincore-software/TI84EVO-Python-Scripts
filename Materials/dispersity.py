# Solve one value. Molecular weights: g/mol. PDI has no units.
print("PDI=Mw/Mn. PDI has no units.")
print("1: PDI  2: Mw  3: Mn")
mode = input("Unknown 1-3: ")
if mode in ("1", "2", "3"):
    if mode != "1":
        pdi = float(input("PDI (no units): "))
    if mode != "2":
        mw = float(input("Mw (g/mol): "))
    if mode != "3":
        mn = float(input("Mn (g/mol): "))
    if mode == "1":
        valid = mn > 0 and mw >= mn
        if valid:
            result = mw / mn
    elif mode == "2":
        valid = pdi >= 1 and mn > 0
        if valid:
            result = pdi * mn
    else:
        valid = pdi >= 1 and mw > 0
        if valid:
            result = mw / pdi
    if valid:
        label = "PDI (no units):" if mode == "1" else ("Mw (g/mol):" if mode == "2" else "Mn (g/mol):")
        print(label)
        print(result)
    else:
        print("Check values; PDI must be at least 1")
else:
    print("Select 1-3")
