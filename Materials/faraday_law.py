"""Solve one variable in Faraday's law."""

print("Faraday law")
print("m=I*t*M/(n*F)")
print("m: kg, I: A, t: s, M: kg/mol")
print("n: electrons, F=96485 C/mol")
print("1 m 2 I 3 t 4 M 5 n")
u = input("Solve: ")
if u not in ("1", "2", "3", "4", "5"):
    print("Bad choice")
else:
    names = ["m", "I", "t", "M", "n"]
    v = [0.0, 0.0, 0.0, 0.0, 0.0]
    k = int(u) - 1
    units = ["kg", "A", "s", "kg/mol", "dimensionless"]
    for i in range(5):
        if i != k:
            v[i] = float(input(names[i] + " " + units[i] + ": "))
    ok = True
    if k != 2 and v[2] <= 0:
        print("t must be > 0")
        ok = False
    if k != 1 and v[1] <= 0:
        print("I must be > 0 A")
        ok = False
    if k != 0 and v[0] < 0:
        print("m must be >= 0")
        ok = False
    if k != 3 and v[3] <= 0:
        print("M must be > 0")
        ok = False
    if k != 4 and v[4] <= 0:
        print("n must be > 0")
        ok = False
    if ok:
        if k == 0:
            v[0] = v[1] * v[2] * v[3] / (v[4] * 96485)
        elif k == 1:
            z = v[2] * v[3]
            if z == 0:
                print("No unique I")
                ok = False
            else:
                v[1] = v[0] * v[4] * 96485 / z
        elif k == 2:
            z = v[1] * v[3]
            if z == 0:
                print("No unique t")
                ok = False
            else:
                v[2] = v[0] * v[4] * 96485 / z
                if v[2] <= 0:
                    print("No physical t")
                    ok = False
        elif k == 3:
            z = v[1] * v[2]
            if z == 0:
                print("No unique M")
                ok = False
            else:
                v[3] = v[0] * v[4] * 96485 / z
                if v[3] <= 0:
                    print("No physical M")
                    ok = False
        else:
            z = v[0] * 96485
            if z == 0:
                print("No unique n")
                ok = False
            else:
                v[4] = v[1] * v[2] * v[3] / z
                if v[4] <= 0:
                    print("No physical n")
                    ok = False
        if ok:
            print(names[k] + " " + units[k] + " = " + str(v[k]))
