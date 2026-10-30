# Gibbs-Duhem data residual calculator.
from math import log

n = int(input("Number of data points: "))
if n < 1:
    print("Need at least one point")
else:
    total = 0.0
    valid_count = 0
    i = 0
    while i < n:
        print("Data point:")
        print(i + 1)
        x1 = float(input("x1: "))
        g1 = float(input("Measured gamma1: "))
        g2 = float(input("Measured gamma2: "))
        c1 = float(input("Model gamma1: "))
        c2 = float(input("Model gamma2: "))
        if x1 <= 0 or x1 >= 1 or g1 <= 0 or g2 <= 0 or c1 <= 0 or c2 <= 0:
            print("Invalid point: fractions and gammas must be positive")
        else:
            x2 = 1.0 - x1
            ge = x1 * log(g1) + x2 * log(g2)
            residual = log(g1 / g2) - log(c1 / c2)
            print("GE/RT:")
            print(ge)
            print("Residual:")
            print(residual)
            total = total + residual
            valid_count = valid_count + 1
        i = i + 1
    if valid_count > 0:
        print("Mean residual:")
        print(total / valid_count)
    else:
        print("No valid data points")
