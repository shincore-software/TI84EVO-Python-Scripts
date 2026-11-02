# Oxide thickness

# Solve one value. x: m. dmA: kg/m2. rho: kg/m3.


print("Oxide thickness")
print("x=dmA/rho*(a MM+b MO)/(b MO)")
print('1: x (m)')
print('2: dmA (kg/m2)')
print('3: rho (kg/m3)')
mode = input("Unknown 1-3: ")
if mode in ("1", "2", "3"):
    a = float(input("a: "))
    b = float(input("b: "))
    mm = float(input("MM (g/mol): "))
    mo = float(input("MO (g/mol): "))
    if mode != "1":
        x = float(input("x (m): "))
    if mode != "2":
        dm = float(input("dmA (kg/m2): "))
    if mode != "3":
        rho = float(input("rho (kg/m3): "))
    factor = (a * mm + b * mo) / (b * mo) if b != 0 and mo > 0 else 0
    valid = a >= 0 and b > 0 and mm > 0 and mo > 0 and factor > 0
    if mode == "1":
        valid = valid and dm >= 0 and rho > 0
        if valid:
            result = dm / rho * factor
    elif mode == "2":
        valid = valid and x >= 0 and rho > 0
        if valid:
            result = x * rho / factor
    else:
        valid = valid and x > 0 and dm > 0
        if valid:
            result = dm * factor / x
    if valid:
        label = "x (m):" if mode == "1" else ("dmA (kg/m2):" if mode == "2" else "rho (kg/m3):")
        print(label)
        print(result)
    else:
        print('Check values; result must be\npositive')
else:
    print("Select 1-3")
