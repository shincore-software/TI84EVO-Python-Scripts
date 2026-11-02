
# Linear interpolation between two points.
# Inputs: points (x0, y0), (x1, y1), and a query x between x0 and x1.
# Output: estimated y. The program does not calculate outside the interval.

x0 = float(input("x0: "))
y0 = float(input("y0: "))
x1 = float(input("x1: "))
y1 = float(input("y1: "))

if x1 == x0:
    print("x0 and x1 must differ")
else:
    x = float(input("Find y at x: "))

    if x < min(x0, x1) or x > max(x0, x1):
        print("x is outside the points")
    else:
        y = y0 + (x - x0) * (y1 - y0) / (x1 - x0)
        print("Interpolated y:" + "\n" + str(y))
