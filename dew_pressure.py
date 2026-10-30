# Ideal or non-ideal dew pressure solver.
# Formula: 1/P = sum(y_i / (gamma_i * Psat_i))

n = int(input("Number of components: "))
if n < 1:
    print("Need at least one component")
else:
    y = []
    gamma = []
    psat = []
    total_y = 0.0
    i = 0
    while i < n:
        print("Component:")
        print(i + 1)
        yi = float(input("y: "))
        gi = float(input("gamma: "))
        pi = float(input("Psat: "))
        y.append(yi)
        gamma.append(gi)
        psat.append(pi)
        total_y = total_y + yi
        i = i + 1

    print("Find value:")
    print("1: Total pressure P")
    print("2: One component y, gamma, or Psat")
    mode = input("Select 1 or 2: ")

    if mode == "1":
        if abs(total_y - 1.0) > 0.001:
            print("y values must sum to 1")
        else:
            den = 0.0
            i = 0
            while i < n:
                if gamma[i] <= 0 or psat[i] <= 0:
                    den = 0.0
                    i = n
                else:
                    den = den + y[i] / (gamma[i] * psat[i])
                    i = i + 1
            if den <= 0:
                print("Need positive gamma and Psat")
            else:
                print("Dew pressure:")
                print(1.0 / den)
    elif mode == "2":
        k = int(input("Component number: ")) - 1
        if k < 0 or k >= n:
            print("Invalid component")
        else:
            print("Solve for:")
            print("1: y")
            print("2: gamma")
            print("3: Psat")
            target = input("Select 1-3: ")
            P = float(input("Known total pressure P: "))
            other = 0.0
            i = 0
            while i < n:
                if i != k:
                    other = other + y[i] / (gamma[i] * psat[i])
                i = i + 1
            rem = 1.0 / P - other
            if target == "1":
                print("y:")
                print(rem * gamma[k] * psat[k])
            elif target == "2":
                if rem == 0 or psat[k] == 0:
                    print("Cannot solve for gamma")
                else:
                    print("gamma:")
                    print(y[k] / (rem * psat[k]))
            elif target == "3":
                if rem == 0 or gamma[k] == 0:
                    print("Cannot solve for Psat")
                else:
                    print("Psat:")
                    print(y[k] / (rem * gamma[k]))
            else:
                print("Select 1, 2, or 3")
    else:
        print("Select 1 or 2")
