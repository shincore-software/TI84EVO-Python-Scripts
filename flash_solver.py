# Isothermal flash solver using supplied K values.

n = int(input("Number of components: "))
if n < 1:
    print("Need at least one component")
else:
    z = []
    K = []
    total = 0.0
    valid = True
    i = 0
    while i < n:
        print("Component:")
        print(i + 1)
        zi = float(input("Feed fraction z: "))
        ki = float(input("Equilibrium ratio K: "))
        z.append(zi)
        K.append(ki)
        total = total + zi
        if zi < 0 or ki <= 0:
            valid = False
        i = i + 1

    if abs(total - 1.0) > 0.001 or not valid:
        print("Need z sum 1 and positive K values")
    else:
        lo = 0.0
        hi = 1.0
        flo = 0.0
        fhi = 0.0
        i = 0
        while i < n:
            flo = flo + z[i] * (K[i] - 1.0)
            fhi = fhi + z[i] * (K[i] - 1.0) / K[i]
            i = i + 1
        if flo == 0:
            V = 0.0
        elif fhi == 0:
            V = 1.0
        elif flo * fhi > 0:
            print("No two-phase solution for these K values")
            V = -1.0
        else:
            count = 0
            while count < 40:
                mid = (lo + hi) / 2.0
                fm = 0.0
                i = 0
                while i < n:
                    fm = fm + z[i] * (K[i] - 1.0) / (1.0 + mid * (K[i] - 1.0))
                    i = i + 1
                if flo * fm <= 0:
                    hi = mid
                    fhi = fm
                else:
                    lo = mid
                    flo = fm
                count = count + 1
            V = (lo + hi) / 2.0
        if V >= 0:
            print("Vapor fraction V:")
            print(V)
            i = 0
            while i < n:
                xi = z[i] / (1.0 + V * (K[i] - 1.0))
                yi = K[i] * xi
                print("Component x, y:")
                print(xi)
                print(yi)
                i = i + 1
