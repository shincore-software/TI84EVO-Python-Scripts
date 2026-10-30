# Local binary-liquid stability check.
# Inputs: liquid fraction x1 and second derivative of GE/RT.
# Output: stability curvature and local stability result.
x1 = float(input("Liquid fraction x1: "))
d2 = float(input("Second derivative of GE/RT: "))
if x1 <= 0 or x1 >= 1:
    print("x1 must be between 0 and 1")
else:
    x2 = 1.0 - x1
    curvature = 1.0 / (x1 * x2) + d2
    print("Stability curvature:")
    print(curvature)
    if curvature > 0:
        print("Locally stable by this test")
    else:
        print("Locally unstable by this test")
