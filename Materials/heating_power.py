def main():
    print("Q=P*t")
    print("SI: J, W, s")
    u = input("Solve for Q,P,t: ")
    
    if u == "Q":
        p = float(input("P W: "))
        t = float(input("t s: "))
        v = p * t
    elif u == "P":
        q = float(input("Q J: "))
        t = float(input("t s: "))
        if t == 0:
            print("No unique P")
            return
        v = q / t
    elif u == "t":
        q = float(input("Q J: "))
        p = float(input("P W: "))
        if p == 0:
            print("No unique t")
            return
        v = q / p
    else:
        print("Unknown variable")
        return
    
    if u == "P" and v < 0 or u == "t" and v < 0:
        print("P and t must be >= 0")
        return
    if u == "Q":
        if p < 0 or t < 0:
            print("P and t must be >= 0")
            return
    elif u == "P":
        if t < 0:
            print("t must be >= 0")
            return
    elif u == "t" and p < 0:
        print("P must be >= 0")
        return
    if u == "Q":
        unit = "J"
    elif u == "P":
        unit = "W"
    elif u == "t":
        unit = "s"
    print(u, "=", v, unit)

main()
