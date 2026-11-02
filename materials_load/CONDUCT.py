# Heat conduction

def main():
    print('Steady heat conduction')
    print('q=k*A*(Th-Tc)/ell')
    print("1: q (W)")
    print("2: k (W/m/K)")
    print("3: A (m^2)")
    print("4: Th (K)")
    print("5: Tc (K)")
    print("6: ell (m)")
    n = input("Select 1-6: ")
    if n == "1":
        u = "q"
    elif n == "2":
        u = "k"
    elif n == "3":
        u = "A"
    elif n == "4":
        u = "Th"
    elif n == "5":
        u = "Tc"
    elif n == "6":
        u = "ell"
    else:
        print("Invalid choice")
        return
    
    if u == "q":
        k = float(input("k W/m/K: "))
        a = float(input("A m^2: "))
        th = float(input("Th K: "))
        tc = float(input("Tc K: "))
        ell = float(input("ell m: "))
        if ell == 0:
            print("ell must not be 0")
            return
        v = k * a * (th - tc) / ell
    elif u == "k" or u == "A":
        q = float(input("q W: "))
        th = float(input("Th K: "))
        tc = float(input("Tc K: "))
        ell = float(input("ell m: "))
        if ell == 0 or th == tc:
            print("No unique value")
            return
        d = (th - tc) / ell
        z = float(input("A m^2: ")) if u == "k" else float(input("k W/m/K: "))
        if z == 0:
            print("No unique value")
            return
        v = q / (z * d)
    elif u == "Th" or u == "Tc":
        q = float(input("q W: "))
        k = float(input("k W/m/K: "))
        a = float(input("A m^2: "))
        if u == "Th":
            tc = float(input("Tc K: "))
        else:
            th = float(input("Th K: "))
        ell = float(input("ell m: "))
        d = k * a
        if d == 0:
            print("No unique T")
            return
        dt = q * ell / d
        v = tc + dt if u == "Th" else th - dt
    elif u == "ell":
        q = float(input("q W: "))
        k = float(input("k W/m/K: "))
        a = float(input("A m^2: "))
        th = float(input("Th K: "))
        tc = float(input("Tc K: "))
        if q == 0:
            print("No unique ell")
            return
        v = k * a * (th - tc) / q
    else:
        print("Unknown variable")
        return
    
    if u == "ell" and v <= 0 or u == "A" and v < 0 or u == "k" and v < 0:
        print("ell must be > 0; k and A >= 0")
        return
    if u in ("Th", "Tc") and v < 0:
        print("Temperature must be >= 0 K")
        return
    if u == "q":
        if k < 0 or a < 0 or ell <= 0 or th < 0 or tc < 0:
            print('Use k,A >= 0; ell > 0; T >= 0\nK')
            return
    elif u in ("k", "A"):
        if ell <= 0 or th < 0 or tc < 0 or z < 0:
            print('Use ell > 0; T >= 0 K; k,A >=\n0')
            return
    elif u in ("Th", "Tc"):
        if k < 0 or a < 0 or ell <= 0:
            print("Use k,A >= 0; ell > 0")
            return
    elif u == "ell":
        if k < 0 or a < 0 or th < 0 or tc < 0:
            print("Use k,A >= 0; T >= 0 K")
            return
    if (u == "Th" and tc < 0) or (u == "Tc" and th < 0):
        print("Temperature must be >= 0 K")
        return
    if u == "q":
        unit = "W"
    elif u == "k":
        unit = "W/m/K"
    elif u == "A":
        unit = "m^2"
    elif u == "Th":
        unit = "K"
    elif u == "Tc":
        unit = "K"
    elif u == "ell":
        unit = "m"
    print(u, "=", v, unit)

main()
