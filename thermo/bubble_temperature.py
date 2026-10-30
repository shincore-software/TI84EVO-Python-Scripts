# Bubble-point temperature solver.
# Inputs: pressure, component count, temperature search range, x, gamma,
# and Antoine A, B, C for each component. Output: bubble-point temperature.
from math import exp

P = float(input("Pressure P: "))
n = int(input("Number of components: "))
lo = float(input("Low temperature: "))
hi = float(input("High temperature: "))
x = []
gamma = []
A = []
B = []
C = []
i = 0
while i < n:
    print("Component:")
    print(i + 1)
    x.append(float(input("Liquid fraction x: ")))
    gamma.append(float(input("Activity coefficient: ")))
    A.append(float(input("Antoine A: ")))
    B.append(float(input("Antoine B: ")))
    C.append(float(input("Antoine C: ")))
    i = i + 1

def residual(T):
    value = -1.0
    j = 0
    while j < n:
        if T + C[j] == 0:
            return 1e30
        psat = exp(A[j] - B[j] / (T + C[j]))
        value = value + x[j] * gamma[j] * psat / P
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
        print("Bubble temperature:")
        print((lo + hi) / 2.0)
