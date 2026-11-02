from math import sqrt


def main():
    print("x=sqrt(a*t)")
    print("SI: m, m^2/s, s")
    u = input("Solve for x,a,t: ")
    
    if u == "x":
        a = float(input("a m^2/s: "))
        t = float(input("t s: "))
        if a < 0 or t < 0:
            print("a and t must be >= 0")
            return
        v = sqrt(a * t)
    elif u == "a":
        x = float(input("x m: "))
        t = float(input("t s: "))
        if x < 0 or t < 0:
            print("x and t must be >= 0")
            return
        if t == 0:
            print("No unique a")
            return
        v = x * x / t
    elif u == "t":
        x = float(input("x m: "))
        a = float(input("a m^2/s: "))
        if x < 0 or a < 0:
            print("x and a must be >= 0")
            return
        if a == 0:
            print("No unique t")
            return
        v = x * x / a
    else:
        print("Unknown variable")
        return
    
    if v < 0:
        print("Result must be >= 0")
        return
    if u == "a" and x < 0 or u == "t" and x < 0:
        print("x must be >= 0")
        return
    if u == "x":
        unit = "m"
    elif u == "a":
        unit = "m^2/s"
    elif u == "t":
        unit = "s"
    print(u, "=", v, unit)

main()
