"""Solve one variable in the Nernst equation."""
import math
print("Nernst potential")
print("E=E0+R*T/(n*F)*ln(C)")
print("C is activity / standard activity")
print("Ideal activity assumed; C must be > 0")
print("E: V, T: K, n: dimensionless")
print("R=8.314 J/(mol*K), F=96485 C/mol")
print("1 E 2 E0 3 T 4 n 5 C")
u = input("Solve: ")
if u not in ("1", "2", "3", "4", "5"):
    print("Bad choice")
else:
    names = ["E", "E0", "T", "n", "C"]
    v = [0.0, 0.0, 0.0, 0.0, 0.0]
    k = int(u) - 1
    units = ["V", "V", "K", "dimensionless", "dimensionless"]
    for i in range(5):
        if i != k:
            v[i] = float(input(names[i] + " " + units[i] + ": "))
    ok = True
    if k != 2 and v[2] <= 0:
        print("T must be > 0 K")
        ok = False
    if k != 3 and v[3] <= 0:
        print("n must be > 0")
        ok = False
    if k != 4 and v[4] <= 0:
        print("C must be > 0")
        ok = False
    if ok:
        if k == 0:
            v[0] = v[1] + 8.314 * v[2] / (96485 * v[3]) * math.log(v[4])
        elif k == 1:
            v[1] = v[0] - 8.314 * v[2] / (96485 * v[3]) * math.log(v[4])
        elif k == 2:
            z = math.log(v[4])
            if z == 0:
                if v[0] == v[1]:
                    print("No unique T")
                else:
                    print("No solution for T")
                ok = False
            else:
                v[2] = (v[0] - v[1]) * 96485 * v[3] / (8.314 * z)
                if v[2] <= 0:
                    print("No physical T")
                    ok = False
        elif k == 3:
            z = v[0] - v[1]
            numerator = 8.314 * v[2] * math.log(v[4])
            if z == 0:
                if numerator == 0:
                    print("No unique n")
                else:
                    print("No solution for n")
                ok = False
            else:
                v[3] = numerator / (96485 * z)
                if v[3] <= 0:
                    print("No physical n")
                    ok = False
        else:
            q = 8.314 * v[2] / (96485 * v[3])
            z = (v[0] - v[1]) / q
            try:
                v[4] = math.exp(z)
            except OverflowError:
                print("Result too large")
                ok = False
            if ok and v[4] == 0:
                print("Result too small")
                ok = False
        if ok:
            print(names[k] + " " + units[k] + " = " + str(v[k]))
