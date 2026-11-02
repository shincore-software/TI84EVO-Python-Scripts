# Polymer chain length
# Solve the projected-chain or random-chain equation.
from math import sin, asin, sqrt, radians, degrees

print("Polymer chain length")
print("1: L=N*d*sin(theta/2)")
print("2: r=d*sqrt(N)")
eq = input("Equation 1 or 2: ")
if eq in ("1", "2"):
    names = ["L", "N", "d", "theta"] if eq == "1" else ["r", "d", "N"]
    units = {"L":"nm", "r":"nm", "d":"nm", "N":"no units", "theta":"deg"}
    labels = (["L (nm)", "N (no units)",
               "d (nm)", "theta (deg)"]
              if eq == "1" else ["r (nm)", "d (nm)",
                                  "N (no units)"])
    print("Projected chain length" if eq == "1" else "Random-chain distance")
    print("L=N*d*sin(theta/2)" if eq == "1" else "r=d*sqrt(N)")
    for i in range(len(names)):
        print(str(i + 1) + ": " + labels[i])
    choice = input("Find 1-" + str(len(names)) + ": ")
    target = names[int(choice) - 1] if choice in (("1", "2", "3", "4") if eq == "1" else ("1", "2", "3")) else ""
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
            print('Need positive values; theta <\n180')
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
                print(target + " (" + units[target] + "):" + "\n" + str(answer))
else:
    print("Select 1 or 2")
