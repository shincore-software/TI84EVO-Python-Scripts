"""Solve one variable in C=m/(M*V)."""
print("Molar concentration")
print("C=m/(M*V)")
print("C: mol/L, m: g, M: g/mol, V: L")
print("1 C 2 m 3 M 4 V")
u = input("Solve: ")
if u not in ("1", "2", "3", "4"):
    print("Bad choice")
else:
    names = ["C", "m", "M", "V"]
    v = [0.0, 0.0, 0.0, 0.0]
    k = int(u) - 1
    for i in range(4):
        if i != k:
            units = ["mol/L", "g", "g/mol", "L"]
            v[i] = float(input(names[i] + " " + units[i] + ": "))
    ok = True
    if k != 2 and v[2] <= 0:
        print("M must be > 0")
        ok = False
    if k != 3 and v[3] <= 0:
        print("V must be > 0 L")
        ok = False
    if k != 1 and v[1] < 0:
        print("m must be >= 0 g")
        ok = False
    if k != 0 and v[0] < 0:
        print("C must be >= 0")
        ok = False
    if ok:
        if k == 0:
            v[0] = v[1] / (v[2] * v[3])
        elif k == 1:
            v[1] = v[0] * v[2] * v[3]
            if v[1] < 0:
                print("No physical mass")
                ok = False
        elif k == 2:
            z = v[0] * v[3]
            if z == 0:
                print("No unique M")
                ok = False
            else:
                v[2] = v[1] / z
                if v[2] <= 0:
                    print("No physical M")
                    ok = False
        else:
            z = v[0] * v[2]
            if z == 0:
                print("No unique V")
                ok = False
            else:
                v[3] = v[1] / z
                if v[3] <= 0:
                    print("No physical V")
                    ok = False
        if ok:
            units = ["mol/L", "g", "g/mol", "L"]
            print(names[k] + " " + units[k] + " = " + str(v[k]))
