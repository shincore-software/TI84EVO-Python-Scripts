# Poynting correction factor.
# Inputs: select factor, volume, pressure, saturation pressure, or temperature.
# Enter the other values and gas constant R. Output: selected result.
from math import exp, log

print("Find value:")
print("1: Factor")
print("2: Liquid molar volume")
print("3: Pressure")
print("4: Saturation pressure")
print("5: Temperature")
mode = input("Select 1-5: ")

if mode == "1":
    Vl = float(input("Liquid molar volume: "))
    P = float(input("Pressure P: "))
    Psat = float(input("Saturation pressure: "))
    R = float(input("Gas constant R: "))
    T = float(input("Temperature T: "))
    if R == 0 or T == 0:
        print("R and T cannot be zero")
    else:
        print("Poynting factor:")
        print(exp(Vl * (P - Psat) / (R * T)))
elif mode in ("2", "3", "4", "5"):
    F = float(input("Poynting factor: "))
    R = float(input("Gas constant R: "))
    T = float(input("Temperature T: "))
    Vl = float(input("Liquid molar volume: "))
    P = float(input("Pressure P: "))
    Psat = float(input("Saturation pressure: "))
    if F <= 0 or R == 0 or T == 0 or Vl == 0:
        print("Need positive factor and non-zero R, T, and Vl")
    else:
        q = R * T * log(F) / Vl
        if mode == "2":
            if P == Psat:
                print("P and Psat must differ")
            else:
                print("Liquid molar volume:")
                print(R * T * log(F) / (P - Psat))
        elif mode == "3":
            print("Pressure:")
            print(Psat + q)
        elif mode == "4":
            print("Saturation pressure:")
            print(P - q)
        else:
            if P == Psat:
                print("P and Psat must differ")
            else:
                print("Temperature:")
                print(Vl * (P - Psat) / (R * log(F)))
else:
    print("Select 1-5")
