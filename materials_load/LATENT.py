def main():
    print("Q=m*L")
    print("SI: J, kg, J/kg")
    u = input("Solve for Q,m,L: ")
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
