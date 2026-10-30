# Binary activity-coefficient models.
from math import exp, log

print("Model:")
print("1: Margules 1")
print("2: Margules 2")
print("3: van Laar")
print("4: Wilson")
print("5: NRTL")
mode = input("Select 1-5: ")
x1 = float(input("x1: "))
x2 = 1.0 - x1
ok = True

if x1 <= 0 or x1 >= 1:
    print("x1 must be between 0 and 1")
    ok = False
else:
    if mode == "1":
        A = float(input("A: "))
        lng1 = A * x2 * x2
        lng2 = A * x1 * x1
    elif mode == "2":
        A12 = float(input("A12: "))
        A21 = float(input("A21: "))
        lng1 = x2 * x2 * (A12 + 2.0 * (A21 - A12) * x1)
        lng2 = x1 * x1 * (A21 + 2.0 * (A12 - A21) * x2)
    elif mode == "3":
        A12 = float(input("A12: "))
        A21 = float(input("A21: "))
        if A12 == 0 or A21 == 0:
            print("A12 and A21 cannot be zero")
            ok = False
        else:
            q1 = 1.0 + A12 * x1 / (A21 * x2)
            q2 = 1.0 + A21 * x2 / (A12 * x1)
            lng1 = A12 / (q1 * q1)
            lng2 = A21 / (q2 * q2)
    elif mode == "4":
        L12 = float(input("Lambda12: "))
        L21 = float(input("Lambda21: "))
        d1 = x1 + x2 * L12
        d2 = x2 + x1 * L21
        if L12 <= 0 or L21 <= 0 or d1 <= 0 or d2 <= 0:
            print("Lambda values must be positive")
            ok = False
        else:
            lng1 = -log(d1) + x2 * (L12 / d1 - L21 / d2)
            lng2 = -log(d2) + x1 * (L21 / d2 - L12 / d1)
    elif mode == "5":
        T = float(input("Temperature T: "))
        R = float(input("Gas constant R: "))
        b12 = float(input("b12: "))
        b21 = float(input("b21: "))
        alpha = float(input("Alpha: "))
        if T <= 0 or R == 0:
            print("T must be positive and R non-zero")
            ok = False
        else:
            t12 = b12 / (R * T)
            t21 = b21 / (R * T)
            g12 = exp(-alpha * t12)
            g21 = exp(-alpha * t21)
            d1 = x1 + x2 * g21
            d2 = x2 + x1 * g12
            lng1 = x2 * x2 * (t21 * (g21 / d1) ** 2 + g12 * t12 / (d2 * d2))
            lng2 = x1 * x1 * (t12 * (g12 / d2) ** 2 + g21 * t21 / (d1 * d1))
    else:
        print("Select 1-5")
        lng1 = 0.0
        lng2 = 0.0

    if ok and mode in ("1", "2", "3", "4", "5"):
        print("ln gamma 1:")
        print(lng1)
        print("gamma 1:")
        print(exp(lng1))
        print("ln gamma 2:")
        print(lng2)
        print("gamma 2:")
        print(exp(lng2))
