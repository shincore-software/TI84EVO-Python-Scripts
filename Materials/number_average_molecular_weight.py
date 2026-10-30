# Calculate number-average molecular weight Mn.
# Inputs: component count, molecular weight Mi, and mole fraction xi.
# Output: Mn in the same units as Mi.

n = int(input("Number of components: "))
if n < 1:
    print("Need at least one component")
else:
    total_x = 0.0
    Mn = 0.0
    valid = True
    i = 0
    while i < n:
        print("Component:")
        print(i + 1)
        Mi = float(input("Molecular weight Mi: "))
        xi = float(input("Mole fraction xi: "))
        if Mi <= 0 or xi < 0:
            valid = False
        total_x = total_x + xi
        Mn = Mn + xi * Mi
        i = i + 1

    if not valid:
        print("Mi must be positive; xi cannot be negative")
    elif abs(total_x - 1.0) > 0.001:
        print("Mole fractions must sum to 1")
    else:
        print("Number-average Mn:")
        print(Mn)
