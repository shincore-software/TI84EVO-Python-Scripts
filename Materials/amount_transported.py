"""Solve one variable in m=J*A*t."""

print("Amount transported")
print("m=J*A*t")
print("m: kg, J: kg/(m^2*s), A: m^2, t: s")
print("1 m 2 J 3 A 4 t")
u = input("Solve: ")
if u not in ("1", "2", "3", "4"):
    print("Bad choice")
else:
    names = ["m", "J", "A", "t"]
    v = [0.0, 0.0, 0.0, 0.0]
    k = int(u) - 1
    for i in range(4):
        if i != k:
            units = ["kg", "kg/(m^2*s)", "m^2", "s"]
            v[i] = float(input(names[i] + " " + units[i] + ": "))
    ok = True
    if k != 1 and v[1] == 0 and k in (2, 3):
        print("No unique result")
        ok = False
    if k == 0 and (v[2] <= 0 or v[3] <= 0):
        print("A and t must be > 0")
        ok = False
    if k == 0:
        v[0] = v[1] * v[2] * v[3]
    elif k == 1:
        if v[2] <= 0 or v[3] <= 0:
            print("A and t must be > 0")
            ok = False
        else:
            v[1] = v[0] / (v[2] * v[3])
    elif k == 2:
        if v[1] == 0 or v[3] <= 0:
            print("No unique A")
            ok = False
        else:
            v[2] = v[0] / (v[1] * v[3])
            if v[2] <= 0:
                print("No physical A")
                ok = False
    else:
        if v[1] == 0 or v[2] <= 0:
            print("No unique t")
            ok = False
        else:
            v[3] = v[0] / (v[1] * v[2])
            if v[3] <= 0:
                print("No physical t")
                ok = False
    if ok:
        units = ["kg", "kg/(m^2*s)", "m^2", "s"]
        print(names[k] + " " + units[k] + " = " + str(v[k]))
