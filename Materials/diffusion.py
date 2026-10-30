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
    return poly * exp(-z * z)

print("R =",R," J/(mol * K)")
print("Find value:")
print("1: Diffusion coefficient D")
print("2: Pre-exponential factor D0")
print("3: Activation energy Qd")
print("4: Temperature T")
print("5: Concentration C(x,t)")
mode = input("Select 1-5: ")

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
        z = x / (2.0 * sqrt(D * t))
        ratio = erfc_approx(z)
        C = C0 + ratio * (Cs - C0)
        print("D (" + units + "):")
        print(D)
        print("x units: " + xunits + ", t units: " + tunits)
        print("Normalized concentration:")
        print(ratio)
        print("C(x,t) (" + cunits + "):")
        print(C)
else:
    print("Select 1, 2, 3, 4, or 5")
