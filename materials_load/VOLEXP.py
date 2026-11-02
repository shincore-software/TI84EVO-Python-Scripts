# Volume expansion

def main():
    print('Volume thermal expansion')
    print('dV=av*V0*dT')
    print("1: dV (m^3)")
    print("2: av (1/K)")
    print("3: V0 (m^3)")
    print("4: dT (K)")
    n = input("Select 1-4: ")
    if n == "1":
        u = "dV"
    elif n == "2":
        u = "av"
    elif n == "3":
        u = "V0"
    elif n == "4":
        u = "dT"
    else:
        print("Invalid choice")
        return
    
    if u == "dV":
        a = float(input("av 1/K: "))
        v0 = float(input("V0 m^3: "))
        dt = float(input("dT K: "))
        v = a * v0 * dt
    elif u == "av":
        dv = float(input("dV m^3: "))
        v0 = float(input("V0 m^3: "))
        dt = float(input("dT K: "))
        d = v0 * dt
        if d == 0:
            print("No unique av")
            return
        v = dv / d
    elif u == "V0":
        dv = float(input("dV m^3: "))
        a = float(input("av 1/K: "))
        dt = float(input("dT K: "))
        d = a * dt
        if d == 0:
            print("No unique V0")
            return
        v = dv / d
    elif u == "dT":
        dv = float(input("dV m^3: "))
        a = float(input("av 1/K: "))
        v0 = float(input("V0 m^3: "))
        d = a * v0
        if d == 0:
            print("No unique dT")
            return
        v = dv / d
    else:
        print("Unknown variable")
        return
    
    if u in ("dV", "av") and v0 <= 0:
        print("V0 must be > 0")
        return
    if u == "dT" and v0 <= 0:
        print("V0 must be > 0")
        return
    if u == "V0" and v <= 0:
        print("V0 must be > 0")
        return
    if u == "dV":
        unit = "m^3"
    elif u == "av":
        unit = "1/K"
    elif u == "V0":
        unit = "m^3"
    elif u == "dT":
        unit = "K"
    print(u, "=", v, unit)

main()
