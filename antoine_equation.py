# Antoine equation calculator.
# Formula: ln(P) = A - B / (T + C)
# Use units that match the source of A, B, and C.

from math import exp, log

print("Antoine equation")
print("1: Find pressure from T")
print("2: Find temperature from P")
mode = input("Select 1 or 2: ")

A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

if mode == "1":
    T = float(input("Temperature T: "))

    if T + C == 0:
        print("T + C cannot be zero")
    else:
        P = exp(A - B / (T + C))
        print("Pressure P:")
        print(P)
elif mode == "2":
    P = float(input("Pressure P: "))

    if P <= 0:
        print("P must be greater than zero")
    else:
        divisor = A - log(P)
        if divisor == 0:
            print("Cannot solve for T")
        else:
            T = B / divisor - C
            print("Temperature T:")
            print(T)
else:
    print("Select 1 or 2")
