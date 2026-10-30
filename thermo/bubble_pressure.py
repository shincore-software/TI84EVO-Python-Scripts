# Ideal or non-ideal bubble pressure solver.
# Formula: P = sum(x_i * gamma_i * Psat_i)
# Inputs: component count, x, gamma, and Psat for each component.
# Select total pressure P or one component x, gamma, or Psat.

n = int(input("Number of components: "))
if n < 1:
    print("Need at least one component")
else:
    x = []
    gamma = []
    psat = []
    total_x = 0.0
    i = 0
    while i < n:
        print("Component:")
        print(i + 1)
        xi = float(input("x: "))
        gi = float(input("gamma: "))
        pi = float(input("Psat: "))
        x.append(xi)
        gamma.append(gi)
        psat.append(pi)
        total_x = total_x + xi
        i = i + 1

    print("Find value:")
    print("1: Total pressure P")
    print("2: One component x, gamma, or Psat")
    mode = input("Select 1 or 2: ")

    if mode == "1":
        if abs(total_x - 1.0) > 0.001:
            print("x values must sum to 1")
        else:
            P = 0.0
            i = 0
            while i < n:
                P = P + x[i] * gamma[i] * psat[i]
                i = i + 1
            print("Bubble pressure:")
            print(P)
    elif mode == "2":
        k = int(input("Component number: ")) - 1
        if k < 0 or k >= n:
            print("Invalid component")
        else:
            print("Solve for:")
            print("1: x")
            print("2: gamma")
            print("3: Psat")
            target = input("Select 1-3: ")
            P = float(input("Known total pressure P: "))
            other = 0.0
            i = 0
            while i < n:
                if i != k:
                    other = other + x[i] * gamma[i] * psat[i]
                i = i + 1
            if target == "1":
                den = gamma[k] * psat[k]
                if den == 0:
                    print("gamma*Psat cannot be zero")
                else:
                    print("x:")
                    print((P - other) / den)
            elif target == "2":
                den = x[k] * psat[k]
                if den == 0:
                    print("x*Psat cannot be zero")
                else:
                    print("gamma:")
                    print((P - other) / den)
            elif target == "3":
                den = x[k] * gamma[k]
                if den == 0:
                    print("x*gamma cannot be zero")
                else:
                    print("Psat:")
                    print((P - other) / den)
            else:
                print("Select 1, 2, or 3")
    else:
        print("Select 1 or 2")
