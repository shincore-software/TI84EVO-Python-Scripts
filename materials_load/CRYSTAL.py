# Percent crystallinity

# Solve one value. Densities: kg/m3. Crystallinity: percent.

print("Crystallinity")
print('X=100*rhoc*(rhos-rhoa)/\n(rhos*(rhoc-rhoa))')
print('1: X (%)')
print('2: rhoc (kg/m3)')
print('3: rhos (kg/m3)')
print('4: rhoa (kg/m3)')
mode = input("Unknown 1-4: ")
if mode in ("1", "2", "3", "4"):
    if mode != "1":
        x = float(input("X (%): ")) / 100.0
    if mode != "2":
        c = float(input("rhoc (kg/m3): "))
    if mode != "3":
        s = float(input("rhos (kg/m3): "))
    if mode != "4":
        a = float(input("rhoa (kg/m3): "))
    valid = True
    if mode == "1":
        valid = c > a > 0 and a <= s <= c
        if valid:
            result = 100.0 * c * (s - a) / (s * (c - a))
            print("X (%):" + "\n" + str(result))
    elif mode == "2":
        # c = x*s*a / (x*s-s+a)
        den = x * s - s + a
        if den == 0:
            valid = False
        else:
            result = x * s * a / den
            valid = 0 <= x <= 1 and a > 0 and result > a and a <= s <= result
            if x == 0 and s == a:
                valid = False
            if valid:
                print("rhoc (kg/m3):" + "\n" + str(result))
    elif mode == "3":
        den = c - x * (c - a)
        if den == 0:
            valid = False
        else:
            result = c * a / den
            valid = 0 <= x <= 1 and c > a > 0 and a <= result <= c
            if valid:
                print("rhos (kg/m3):" + "\n" + str(result))
    else:
        den = c - x * s
        if den == 0:
            valid = False
        else:
            result = c * s * (1.0 - x) / den
            valid = 0 <= x <= 1 and c > result > 0 and result <= s <= c
            if valid:
                print("rhoa (kg/m3):" + "\n" + str(result))
    if not valid:
        print('Invalid values or no unique\nresult')
else:
    print("Select 1-4")
