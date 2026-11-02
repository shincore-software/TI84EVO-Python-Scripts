# Run this test on the target calculator before the solvers.
from math import exp, log, sqrt, sin, asin, radians, degrees

print("TI runtime check")
print("Enter 2 when asked.")
x = float(input("Test value: "))
if x != 2:
    print("Run again and enter 2")
else:
    values = []
    for i in range(3):
        values.append(i + 1)
    data = {"total": sum(values)}
    ok = data["total"] == 6 and max(1.0, x) == 2
    ok = ok and abs(sqrt(4) - 2) < 0.000001
    ok = ok and abs(log(exp(1)) - 1) < 0.000001
    ok = ok and abs(degrees(asin(sin(radians(30)))) - 30) < 0.000001
    try:
        float("bad")
        ok = False
    except ValueError:
        pass
    if ok:
        print("Feature checks passed")
    else:
        print("Feature check failed")
    print("Small value: expect 1e-20")
    print(1e-20)
    print("Test each solver next.")
