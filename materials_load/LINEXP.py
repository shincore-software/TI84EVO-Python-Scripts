# Linear expansion

def main():
    print("1 dL: length change (m)")
    print("2 a: alpha (1/K)")
    print("3 L0: start length (m)")
    print("4 dT: temp change (K)")
    n = input("Select 1-4: ")
    if n == "1":
        u = "dL"
    elif n == "2":
        u = "a"
    elif n == "3":
        u = "L0"
    elif n == "4":
        u = "dT"
    else:
        print("Invalid choice")
        return
    
    if u == "dL":
        a = float(input("alpha 1/K: "))
        l0 = float(input("L0 m: "))
        dt = float(input("dT K: "))
        v = a * l0 * dt
    elif u == "a":
        dl = float(input("dL m: "))
        l0 = float(input("L0 m: "))
        dt = float(input("dT K: "))
        d = l0 * dt
        if d == 0:
            print("No unique alpha")
            return
        v = dl / d
    elif u == "L0":
        dl = float(input("dL m: "))
        a = float(input("alpha 1/K: "))
        dt = float(input("dT K: "))
        d = a * dt
        if d == 0:
            print("No unique L0")
            return
        v = dl / d
    elif u == "dT":
        dl = float(input("dL m: "))
        a = float(input("alpha 1/K: "))
        l0 = float(input("L0 m: "))
        d = a * l0
        if d == 0:
            print("No unique dT")
            return
        v = dl / d
    else:
        print("Unknown variable")
        return
    
    if u == "dL":
        if l0 <= 0:
            print("L0 must be > 0")
            return
    elif u == "a":
        if l0 <= 0:
            print("L0 must be > 0")
            return
    elif u == "L0" and v <= 0:
        print("L0 must be > 0")
        return
    elif u == "dT" and l0 <= 0:
        print("L0 must be > 0")
        return
    if u == "dL":
        unit = "m"
    elif u == "a":
        unit = "1/K"
    elif u == "L0":
        unit = "m"
    elif u == "dT":
        unit = "K"
    print(u, "=", v, unit)

main()
