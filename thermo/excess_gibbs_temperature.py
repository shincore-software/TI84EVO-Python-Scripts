# Temperature adjustment of GE/RT for constant excess enthalpy.
# Inputs: gas constant R, start and end temperatures, start GE/RT, and HE.
# Output: estimated end GE/RT. Assumes HE is constant.
R = float(input("Gas constant R: "))
T0 = float(input("Start temperature T0: "))
T1 = float(input("End temperature T1: "))
g0 = float(input("Start GE/RT: "))
HE = float(input("Constant excess enthalpy HE: "))

if R == 0 or T0 == 0 or T1 == 0:
    print("R, T0, and T1 cannot be zero")
else:
    g1 = g0 + HE / R * (1.0 / T1 - 1.0 / T0)
    print("Estimated end GE/RT:")
    print(g1)
