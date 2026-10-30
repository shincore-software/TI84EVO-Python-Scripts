# Dew-point temperature solver.
from math import exp

P = float(input("Pressure P: "))
n = int(input("Number of components: "))
lo = float(input("Low temperature: "))
hi = float(input("High temperature: "))
y = []
gamma = []
A = []
B = []
C = []
i = 0
while i < n:
    print("Component:")
    print(i + 1)
    y.append(float(input("Vapor fraction y: ")))
    gamma.append(float(input("Activity coefficient: ")))
    A.append(float(input("Antoine A: ")))
    B.append(float(input("Antoine B: ")))
    C.append(float(input("Antoine C: ")))
    i = i + 1

def residual(T):
    value = -1.0
    j = 0
    while j < n:
        if T + C[j] == 0 or gamma[j] <= 0:
            return 1e30
        psat = exp(A[j] - B[j] / (T + C[j]))
        value = value + y[j] * P / (gamma[j] * psat)
        j = j + 1
    return value

if n < 1 or P <= 0 or lo >= hi:
    print("Check pressure, component count, and range")
else:
    flo = residual(lo)
    fhi = residual(hi)
    if flo * fhi > 0:
        print("Range does not bracket a solution")
    else:
        count = 0
        while count < 40:
            mid = (lo + hi) / 2.0
            fm = residual(mid)
            if flo * fm <= 0:
                hi = mid
                fhi = fm
            else:
                lo = mid
                flo = fm
            count = count + 1
        print("Dew temperature:")
        print((lo + hi) / 2.0)
