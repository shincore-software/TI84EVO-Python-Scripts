def main():
    print("a=k/(rho*cp)")
    print("SI: m^2/s, W/m/K, kg/m^3, J/kg/K")
    u = input("Solve for a,k,rho,cp: ")
    
    if u == "a":
        k = float(input("k W/m/K: "))
        r = float(input("rho kg/m^3: "))
        cp = float(input("cp J/kg/K: "))
        if r == 0 or cp == 0:
            print("rho and cp must not be 0")
            return
        v = k / (r * cp)
    elif u == "k":
        a = float(input("a m^2/s: "))
        r = float(input("rho kg/m^3: "))
        cp = float(input("cp J/kg/K: "))
        v = a * r * cp
    elif u == "rho":
        a = float(input("a m^2/s: "))
        k = float(input("k W/m/K: "))
        cp = float(input("cp J/kg/K: "))
        d = a * cp
        if d == 0:
            print("No unique rho")
            return
        v = k / d
    elif u == "cp":
        a = float(input("a m^2/s: "))
        k = float(input("k W/m/K: "))
        r = float(input("rho kg/m^3: "))
        d = a * r
        if d == 0:
            print("No unique cp")
            return
        v = k / d
    else:
        print("Unknown variable")
        return
    
    if u == "a" and v <= 0 or u == "k" and v <= 0 or u == "rho" and v <= 0 or u == "cp" and v <= 0:
        print("Properties must be > 0")
        return
    if u == "a" and (k <= 0 or r <= 0 or cp <= 0):
        print("k, rho and cp must be > 0")
        return
    if u == "k" and (r <= 0 or cp <= 0 or a <= 0):
        print("a, rho and cp must be > 0")
        return
    if u == "rho" and (a <= 0 or k <= 0 or cp <= 0):
        print("a, k and cp must be > 0")
        return
    if u == "cp" and (a <= 0 or k <= 0 or r <= 0):
        print("a, k and rho must be > 0")
        return
    if u == "a":
        unit = "m^2/s"
    elif u == "k":
        unit = "W/m/K"
    elif u == "rho":
        unit = "kg/m^3"
    elif u == "cp":
        unit = "J/kg/K"
    print(u, "=", v, unit)

main()
