# Solve the Arrhenius diffusion equation.
# Formula: D = D0 * exp(-Qd / (R * T)). R is 8.314 J/(mol*K).
# Inputs: select D, D0, Qd, T, or concentration C(x,t).
# Use T in kelvin and Qd in J/mol. Output values include their units.
# Approximation for erfc(z), where z is non-negative.
from math import exp, log, sqrt
R = 8.314
def erfc_approx(z):
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
    print("R =",R," J/(mol * K)")
    print("Find value:")
    print("1: Diffusion coefficient D")
    print("2: Pre-exponential factor D0")
    print("3: Activation energy Qd")
    print("4: Temperature T")
    print("5: Concentration C(x,t)")
    print("6: Solve concentration equation")
    mode = input("Select 1-6: ")
    if mode == "1":
        units = input("Units for D and D0 (example m^2/s): ")
        D0 = float(input("D0 value: "))
        Qd = float(input("Qd (J/mol): "))
        T = float(input("T (K): "))
        if D0 <= 0 or T <= 0:
            print("D0 and T must be positive")
        else:
            D = D0 * exp(-Qd / (R * T))
            print("D (" + units + "):")
            print(D)
    elif mode == "2":
        units = input("Units for D and D0 (example m^2/s): ")
        D = float(input("D value: "))
        Qd = float(input("Qd (J/mol): "))
        T = float(input("T (K): "))
        if D <= 0 or T <= 0:
            print("D and T must be positive")
        else:
            D0 = D * exp(Qd / (R * T))
            print("D0 (" + units + "):")
            print(D0)
    elif mode == "3":
        units = input("Units for D and D0 (example m^2/s): ")
        D = float(input("D value: "))
        D0 = float(input("D0 value: "))
        T = float(input("T (K): "))
        if D <= 0 or D0 <= 0 or T <= 0:
            print("D, D0, and T must be positive")
        else:
            Qd = -R * T * log(D / D0)
            print("Qd (J/mol):")
            print(Qd)
    elif mode == "4":
        units = input("Units for D and D0 (example m^2/s): ")
        D = float(input("D value: "))
        D0 = float(input("D0 value: "))
        Qd = float(input("Qd (J/mol): "))
        if D <= 0 or D0 <= 0 or D == D0:
            print("Need positive D and D0, with D different from D0")
        else:
            divisor = R * log(D / D0)
            if divisor == 0:
                print("Cannot solve for T")
            else:
                T = -Qd / divisor
                if T <= 0:
                    print("Inputs do not give a positive T")
                else:
                    print("T (K):")
                    print(T)
    elif mode == "5":
        units = input("D units (length^2/time): ")
        xunits = input("x length units: ")
        tunits = input("t time units: ")
        cunits = input("Concentration units: ")
        D0 = float(input("D0, same units as D: "))
        Qd = float(input("Qd (J/mol): "))
        T = float(input("T (K): "))
        x = float(input("Depth x: "))
        t = float(input("Time t: "))
        C0 = float(input("Initial concentration C0: "))
        Cs = float(input("Surface concentration Cs: "))
        if D0 <= 0 or T <= 0 or x < 0 or t <= 0:
            print("Need D0,T,t positive and x non-negative")
        else:
            D = D0 * exp(-Qd / (R * T))
            if D <= 0 or D * t <= 0:
                print("D*t is below the numeric range")
            else:
                z = x / (2.0 * sqrt(D * t))
                ratio = erfc_approx(z)
                C = C0 + ratio * (Cs - C0)
                print("D (" + units + "):")
                print(D)
                print("C(x,t) (" + cunits + "):")
                print(C)
    elif mode == "6":
        print("C=C0+(Cs-C0)*erfc(x/(2*sqrt(D*t)))")
        print("D: m^2/s. x: m. t: s.")
        print("Use one unit for C, C0, and Cs.")
        cu = input("Concentration unit: ")
        names = ["C", "C0", "Cs", "x", "t", "D"]
        units = {"C":cu, "C0":cu, "Cs":cu, "x":"m", "t":"s", "D":"m^2/s"}
        target = input("Find C, C0, Cs, x, t, or D: ")
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
                print("Equal Cs and C0: no unique answer")
            else:
                ratio = (v["C"] - v["C0"]) / (v["Cs"] - v["C0"])
                if ratio <= 0 or ratio > 1:
                    valid = False
                    print("Need 0 < concentration ratio <= 1")
                elif ratio == 1:
                    if target == "x":
                        answer = 0.0
                    else:
                        valid = False
                        print("No unique finite answer")
                elif target != "x" and v["x"] == 0:
                    valid = False
                    print("No solution at x=0 for this ratio")
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
                print(target + " (" + units[target] + "):")
                print(answer)
    else:
        print("Select 1-6")
try:
    main()
except OverflowError:
    print("Result exceeds the numeric range")
except ZeroDivisionError:
    print("Divisor is zero or below range")
except ValueError:
    print("Check numeric inputs and range")
