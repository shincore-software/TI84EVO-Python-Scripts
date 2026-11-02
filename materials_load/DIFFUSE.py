# Diffusion
# Solve the Arrhenius diffusion equation.
# Formula: D = D0 * exp(-Qd / (R * T)). R is 8.314 J/(mol*K).
# Inputs: select D, D0, Qd, T, or concentration C(x,t).
# Use T in kelvin and Qd in J/mol. Output values include their units.

from math import exp, log, sqrt


R = 8.314
def erfc_approx(z):
    # Approximation for erfc(z), where z is non-negative.
    p = 0.3275911
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    u = 1.0 / (1.0 + p * z)
    poly = (((((a5 * u + a4) * u) + a3) * u + a2) * u + a1) * u
    if z == 0:
        return 1.0
    return poly * exp(-z * z)

def main():
    print("1: Find D")
    print("2: Find D0")
    print("3: Find Qd")
    print("4: Find T")
    print("5: Find C(x,t)")
    print("6: Solve C equation")
    mode = input("Select 1-6: ")
    
    if mode == "1":
        units = "m^2/s"
        D0 = float(input("D0 (m^2/s): "))
        Qd = float(input("Qd (J/mol): "))
        T = float(input("T (K): "))
        if D0 <= 0 or T <= 0:
            print("D0 and T must be positive")
        else:
            D = D0 * exp(-Qd / (R * T))
            print("D (" + units + "):" + "\n" + str(D))
    elif mode == "2":
        units = "m^2/s"
        D = float(input("D (m^2/s): "))
        Qd = float(input("Qd (J/mol): "))
        T = float(input("T (K): "))
        if D <= 0 or T <= 0:
            print("D and T must be positive")
        else:
            D0 = D * exp(Qd / (R * T))
            print("D0 (" + units + "):" + "\n" + str(D0))
    elif mode == "3":
        units = "m^2/s"
        D = float(input("D (m^2/s): "))
        D0 = float(input("D0 (m^2/s): "))
        T = float(input("T (K): "))
        if D <= 0 or D0 <= 0 or T <= 0:
            print("D, D0, and T must be positive")
        else:
            Qd = -R * T * log(D / D0)
            print("Qd (J/mol):" + "\n" + str(Qd))
    elif mode == "4":
        units = "m^2/s"
        D = float(input("D (m^2/s): "))
        D0 = float(input("D0 (m^2/s): "))
        Qd = float(input("Qd (J/mol): "))
        if D <= 0 or D0 <= 0 or D == D0:
            print('Need positive D and D0, with D\ndifferent from D0')
        else:
            divisor = R * log(D / D0)
            if divisor == 0:
                print("Cannot solve for T")
            else:
                T = -Qd / divisor
                if T <= 0:
                    print('Inputs do not give a positive\nT')
                else:
                    print("T (K):" + "\n" + str(T))
    elif mode == "5":
        units = "m^2/s"
        cunits = "kg/m^3"
        D0 = float(input("D0 (m^2/s): "))
        Qd = float(input("Qd (J/mol): "))
        T = float(input("T (K): "))
        x = float(input("Depth x (m): "))
        t = float(input("Time t (s): "))
        C0 = float(input("C0 (kg/m^3): "))
        Cs = float(input("Cs (kg/m^3): "))
        if D0 <= 0 or T <= 0 or x < 0 or t <= 0:
            print('Need D0,T,t positive and x\nnon-negative')
        else:
            D = D0 * exp(-Qd / (R * T))
            if D <= 0 or D * t <= 0:
                print("D*t is below the numeric range")
            else:
                z = x / (2.0 * sqrt(D * t))
                ratio = erfc_approx(z)
                C = C0 + ratio * (Cs - C0)
                print("D (" + units + "):" + "\n" + str(D))
                print("C(x,t) (" + cunits + "):" + "\n" + str(C))
    elif mode == "6":
        cu = "kg/m^3"
        names = ["C", "C0", "Cs", "x", "t", "D"]
        units = {"C":cu, "C0":cu, "Cs":cu, "x":"m", "t":"s", "D":"m^2/s"}
        for i in range(6):
            print(str(i + 1) + ": " + names[i])
        choice = input("Find 1-6: ")
        target = names[int(choice) - 1] if choice in ("1", "2", "3", "4", "5", "6") else ""
        if target not in names:
            print("Invalid selection")
        else:
            v = {}
            valid = True
            for name in names:
                if name != target:
                    v[name] = float(input(name + " (" + units[name] + "): "))
            if target != "x" and v["x"] < 0:
                valid = False
            for name in ("t", "D"):
                if name != target and v[name] <= 0:
                    valid = False
            answer = 0.0
            if not valid:
                print("Need x >= 0, t > 0, D > 0")
            elif target in ("C", "C0", "Cs") and v["D"] * v["t"] <= 0:
                valid = False
                print("D*t is below the numeric range")
            elif target in ("C", "C0", "Cs"):
                q = erfc_approx(v["x"] / (2 * sqrt(v["D"] * v["t"])))
                if v["x"] == 0:
                    q = 1.0
                if target == "C":
                    answer = v["C0"] + q * (v["Cs"] - v["C0"])
                elif target == "C0" and q != 1:
                    answer = (v["C"] - q * v["Cs"]) / (1 - q)
                elif target == "Cs" and q != 0:
                    answer = (v["C"] - (1 - q) * v["C0"]) / q
                else:
                    valid = False
                    print("No unique finite answer")
            elif v["Cs"] == v["C0"]:
                valid = False
                print('Equal Cs and C0: no unique\nanswer')
            else:
                ratio = (v["C"] - v["C0"]) / (v["Cs"] - v["C0"])
                if ratio <= 0 or ratio > 1:
                    valid = False
                    print('Need 0 < concentration ratio\n<= 1')
                elif ratio == 1:
                    if target == "x":
                        answer = 0.0
                    else:
                        valid = False
                        print("No unique finite answer")
                elif target != "x" and v["x"] == 0:
                    valid = False
                    print('No solution at x=0 for this\nratio')
                else:
                    low = 0.0
                    high = 1.0
                    while erfc_approx(high) > ratio:
                        high = high * 2
                    for i in range(50):
                        mid = (low + high) / 2
                        if erfc_approx(mid) > ratio:
                            low = mid
                        else:
                            high = mid
                    z = (low + high) / 2
                    if target == "x":
                        answer = 2 * z * sqrt(v["D"] * v["t"])
                    elif target == "t":
                        answer = (v["x"] / (2 * z)) ** 2 / v["D"]
                    else:
                        answer = (v["x"] / (2 * z)) ** 2 / v["t"]
            if valid:
                print(target + " (" + units[target] + "):" + "\n" + str(answer))
    else:
        print("Select 1-6")

try:
    main()
except OverflowError:
    print('Result exceeds the numeric\nrange')
except ZeroDivisionError:
    print("Divisor is zero or below range")
except ValueError:
    print("Check numeric inputs and range")
