# Latent heat

def main():
    print("1 Q: heat (J)")
    print("2 m: mass (kg)")
    print("3 L: latent heat (J/kg)")
    n = input("Select 1-3: ")
    if n == "1":
        u = "Q"
    elif n == "2":
        u = "m"
    elif n == "3":
        u = "L"
    else:
        print("Invalid choice")
        return
    
    if u == "Q":
        m = float(input("m kg: "))
        l = float(input("L J/kg: "))
        v = m * l
    elif u == "m":
        q = float(input("Q J: "))
        l = float(input("L J/kg: "))
        if l == 0:
            print("No unique m")
            return
        v = q / l
    elif u == "L":
        q = float(input("Q J: "))
        m = float(input("m kg: "))
        if m == 0:
            print("No unique L")
            return
        v = q / m
    else:
        print("Unknown variable")
        return
    
    if (u == "m" or u == "L") and v < 0:
        print("m and L must be >= 0")
        return
    if u == "Q":
        if m < 0 or l < 0:
            print("m and L must be >= 0")
            return
    elif u == "m" and l < 0:
        print("L must be >= 0")
        return
    elif u == "L" and m < 0:
        print("m must be >= 0")
        return
    if u == "Q":
        unit = "J"
    elif u == "m":
        unit = "kg"
    elif u == "L":
        unit = "J/kg"
    print(u, "=", v, unit)

main()
