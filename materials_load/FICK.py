# Fick's first law

"""Solve one variable in Fick's first law."""

print("Fick first law")
print("J=-D*(C2-C1)/(x2-x1)")


print('1: J (kg/(m^2*s))')
print('2: D (m^2/s)')
print('3: C1 (kg/m^3)')
print('4: C2 (kg/m^3)')
print('5: x1 (m)')
print('6: x2 (m)')
u = input("Solve: ")

if u not in ("1", "2", "3", "4", "5", "6"):
    print("Bad choice")
else:
    names = ["J", "D", "C1", "C2", "x1", "x2"]
    v = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    k = int(u) - 1
    ok = True
    for i in range(6):
        if i != k:
            units = ["kg/(m^2*s)", "m^2/s", "kg/m^3", "kg/m^3", "m", "m"]
            v[i] = float(input(names[i] + " " + units[i] + ": "))
    if k != 1 and v[1] <= 0:
        print("D must be > 0")
        ok = False
    if k != 2 and v[2] < 0 or k != 3 and v[3] < 0:
        print("Concentrations must be >= 0")
        ok = False
    if ok:
        d = v[5] - v[4]
        dc = v[3] - v[2]
        if k == 0:
            if d == 0:
                print("x2-x1 must not be 0")
                ok = False
            else:
                v[0] = -v[1] * dc / d
        elif k == 1:
            if d == 0 or dc == 0:
                print("No unique D")
                ok = False
            else:
                v[1] = -v[0] * d / dc
                if v[1] <= 0:
                    print("No physical D")
                    ok = False
        elif k == 2:
            if v[1] == 0 or d == 0:
                print("No unique C1")
                ok = False
            else:
                v[2] = v[3] + v[0] * d / v[1]
                if v[2] < 0:
                    print("No physical C1")
                    ok = False
        elif k == 3:
            if v[1] == 0 or d == 0:
                print("No unique C2")
                ok = False
            else:
                v[3] = v[2] - v[0] * d / v[1]
                if v[3] < 0:
                    print("No physical C2")
                    ok = False
        elif k == 4:
            if v[0] == 0:
                print("No unique x1")
                ok = False
            else:
                v[4] = v[5] + v[1] * dc / v[0]
                if v[5] - v[4] == 0:
                    print("No valid x1")
                    ok = False
        else:
            if v[0] == 0:
                print("No unique x2")
                ok = False
            else:
                v[5] = v[4] - v[1] * dc / v[0]
                if v[5] - v[4] == 0:
                    print("No valid x2")
                    ok = False
        if ok:
            units = ["kg/(m^2*s)", "m^2/s", "kg/m^3", "kg/m^3", "m", "m"]
            print(names[k] + " " + units[k] + " =")
            print(v[k])
