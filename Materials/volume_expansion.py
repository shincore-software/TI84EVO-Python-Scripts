def main():
    print("dV=av*V0*dT")
    print("SI: m^3, 1/K, m^3, K")
    u = input("Solve for dV,av,V0,dT: ")
    
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
