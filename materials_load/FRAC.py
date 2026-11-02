# Fraction conversion

# Convert mole fractions and weight fractions.
print('1: Mole to weight')
print('2: Weight to mole')
mode = input("Select 1-2: ")
if mode in ("1", "2"):
    n = int(input("Number of components: "))
    if n < 1 or n > 20:
        print("Use 1 to 20 components")
        n = 0
    masses = []
    fractions = []
    valid = n > 0
    for i in range(n):
        print("Component:" + "\n" + str(i + 1))
        m = float(input("Mi (g/mol): "))
        f = float(input("xi (no units): " if mode == "1" else "wi (no units): "))
        if m <= 0 or f < 0 or f > 1:
            valid = False
        masses.append(m)
        fractions.append(f)
    if abs(sum(fractions) - 1.0) > 0.001:
        valid = False
    if valid:
        values = []
        total = 0.0
        for i in range(n):
            value = fractions[i] * masses[i] if mode == "1" else fractions[i] / masses[i]
            values.append(value)
            total = total + value
        if total <= 0:
            print('Fractions must have a positive\nsum')
        else:
            print("wi (no units):" if mode == "1" else "xi (no units):")
            for i in range(n):
                print(values[i] / total)
    else:
        print("Check masses and fractions")
else:
    print("Select 1-2")
