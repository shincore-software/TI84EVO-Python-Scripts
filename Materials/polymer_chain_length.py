# Solve the projected-chain or random-chain equation.
from math import sin, asin, sqrt, radians, degrees
print("Lengths: nm. Angle: deg.")
print("N: bond count (no units).")
print("1: L=N*d*sin(theta/2)")
print("2: r=d*sqrt(N)")
eq = input("Equation 1 or 2: ")
if eq in ("1", "2"):
    names = ["L", "N", "d", "theta"] if eq == "1" else ["r", "d", "N"]
    units = {"L":"nm", "r":"nm", "d":"nm", "N":"no units", "theta":"deg"}
    for name in names:
        print(name)
    target = input("Find variable: ")
    if target not in names:
        print("Invalid selection")
    else:
        v = {}
        valid = True
        for name in names:
            if name != target:
                v[name] = float(input(name + " (" + units[name] + "): "))
                if v[name] <= 0 or (name == "theta" and v[name] >= 180):
                    valid = False
        if not valid:
            print("Need positive values; theta < 180")
        else:
            answer = 0.0
            if eq == "2":
                if target == "r":
                    answer = v["d"] * sqrt(v["N"])
                elif target == "d":
                    answer = v["r"] / sqrt(v["N"])
                else:
                    answer = (v["r"] / v["d"]) ** 2
            elif target == "theta":
                q = v["L"] / (v["N"] * v["d"])
                if q >= 1:
                    valid = False
                    print("Need 0 < L/(N*d) < 1")
                else:
                    answer = 2 * degrees(asin(q))
            elif target == "L":
                answer = v["N"] * v["d"] * sin(radians(v["theta"] / 2))
            elif target == "N":
                answer = v["L"] / (v["d"] * sin(radians(v["theta"] / 2)))
            else:
                answer = v["L"] / (v["N"] * sin(radians(v["theta"] / 2)))
            if valid:
                print(target + " (" + units[target] + "):")
                print(answer)
else:
    print("Select 1 or 2")
