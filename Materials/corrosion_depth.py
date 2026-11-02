# Solve one value. x: m; m: kg; rho: kg/m3; A: m2.
print("x=m/(rho A)")
print("1: x  2: m  3: rho  4: A")
mode = input("Unknown 1-4: ")
if mode in ("1", "2", "3", "4"):
    if mode != "1":
        x = float(input("x (m): "))
    if mode != "2":
        mass = float(input("m (kg): "))
    if mode != "3":
        rho = float(input("rho (kg/m3): "))
    if mode != "4":
        area = float(input("A (m2): "))
    valid = True
    if mode == "1":
        valid = mass >= 0 and rho > 0 and area > 0
        if valid:
            result = mass / (rho * area)
    elif mode == "2":
        valid = x >= 0 and rho > 0 and area > 0
        if valid:
            result = x * rho * area
    elif mode == "3":
        valid = x > 0 and mass > 0 and area > 0
        if valid:
            result = mass / (x * area)
    else:
        valid = x > 0 and mass > 0 and rho > 0
        if valid:
            result = mass / (x * rho)
    if valid:
        label = "x (m):" if mode == "1" else ("m (kg):" if mode == "2" else ("rho (kg/m3):" if mode == "3" else "A (m2):"))
        print(label)
        print(result)
    else:
        print("Values must be positive")
else:
    print("Select 1-4")
