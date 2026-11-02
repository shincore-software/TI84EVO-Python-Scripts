# Sensible heat

def main():
    print("1 Q: heat (J)")
    print("2 m: mass (kg)")
    print("3 cp: heat cap (J/kg/K)")
    print("4 Tf: final temp (K)")
    print("5 Ti: start temp (K)")
    n = input("Select 1-5: ")
    if n == "1":
        u = "Q"
    elif n == "2":
        u = "m"
    elif n == "3":
        u = "cp"
    elif n == "4":
        u = "Tf"
    elif n == "5":
        u = "Ti"
    else:
        print("Invalid choice")
        return
    
    if u == "Q":
        m = float(input("m kg: "))
        cp = float(input("cp J/kg/K: "))
        tf = float(input("Tf K: "))
        ti = float(input("Ti K: "))
        v = m * cp * (tf - ti)
    elif u == "m":
        q = float(input("Q J: "))
        cp = float(input("cp J/kg/K: "))
        tf = float(input("Tf K: "))
        ti = float(input("Ti K: "))
        d = cp * (tf - ti)
        if d == 0:
            print("No unique m")
            return
        v = q / d
    elif u == "cp":
        q = float(input("Q J: "))
        m = float(input("m kg: "))
        tf = float(input("Tf K: "))
        ti = float(input("Ti K: "))
        d = m * (tf - ti)
        if d == 0:
            print("No unique cp")
            return
        v = q / d
    elif u == "Tf" or u == "Ti":
        q = float(input("Q J: "))
        m = float(input("m kg: "))
        cp = float(input("cp J/kg/K: "))
        if m == 0 or cp == 0:
            print("No unique T")
            return
        d = q / (m * cp)
        if u == "Tf":
            ti = float(input("Ti K: "))
            v = ti + d
        else:
            tf = float(input("Tf K: "))
            v = tf - d
    else:
        print("Unknown variable")
        return
    
    if u == "Q":
        if m <= 0 or cp <= 0 or tf < 0 or ti < 0:
            print("m,cp > 0; temperatures >= 0 K")
            return
    elif u == "m":
        if cp <= 0 or tf < 0 or ti < 0 or v <= 0:
            print("cp > 0; mass > 0; T >= 0 K")
            return
    elif u == "cp":
        if m <= 0 or tf < 0 or ti < 0 or v <= 0:
            print("m,cp > 0; T >= 0 K")
            return
    elif u == "Tf":
        if m <= 0 or cp <= 0 or ti < 0 or v < 0:
            print("m,cp > 0; T >= 0 K")
            return
    elif u == "Ti":
        if m <= 0 or cp <= 0 or tf < 0 or v < 0:
            print("m,cp > 0; T >= 0 K")
            return
    if u == "Q":
        unit = "J"
    elif u == "m":
        unit = "kg"
    elif u == "cp":
        unit = "J/kg/K"
    elif u == "Tf":
        unit = "K"
    elif u == "Ti":
        unit = "K"
    print(u, "=", v, unit)

main()
