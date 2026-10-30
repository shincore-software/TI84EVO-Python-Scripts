# Calculate weight-average molecular weight Mw.
# Inputs: component count, molecular weight Mi, and mole fraction xi.
# The program calculates each weight fraction wi from xi and Mi.
# Output: Mw in the same units as Mi.

n = int(input("Number of components: "))
if n < 1:
    print("Need at least one component")
else:
    total_x = 0.0
    valid = True
    molecular_weights = []
    mole_fractions = []
    i = 0
    while i < n:
        print("Component:")
        print(i + 1)
        Mi = float(input("Molecular weight Mi: "))
        xi = float(input("Mole fraction xi: "))
        if Mi <= 0 or xi < 0:
            valid = False
        molecular_weights.append(Mi)
        mole_fractions.append(xi)
        total_x = total_x + xi
        i = i + 1

    if not valid:
        print("Mi must be positive; xi cannot be negative")
    elif abs(total_x - 1.0) > 0.001:
        print("Mole fractions must sum to 1")
    else:
        mass_sum = 0.0
        i = 0
        while i < n:
            mass_sum = mass_sum + mole_fractions[i] * molecular_weights[i]
            i = i + 1
        if mass_sum <= 0:
            print("Total mass fraction basis must be positive")
        else:
            Mw = 0.0
            wi_values = []
            i = 0
            while i < n:
                wi = mole_fractions[i] * molecular_weights[i] / mass_sum
                wi_values.append(wi)
                Mw = Mw + wi * molecular_weights[i]
                i = i + 1
            i = 0
            while i < n:
                print("w" + str(i + 1) + " = (" + str(mole_fractions[i])
                      + " * " + str(molecular_weights[i]) + ") / "
                      + str(mass_sum))
                print(wi_values[i])
                i = i + 1
            print("Weight-average Mw:")
            print(Mw)
