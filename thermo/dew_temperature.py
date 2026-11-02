# Dew-point temperature solver.
# Inputs: pressure, component count, temperature search range, y, gamma,
# and Antoine A, B, C for each component. Output: dew-point temperature.
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
total = 0.0
valid = True
i = 0
while i < n:
    print("Component:" + "\n" + str(i + 1))
    y.append(float(input("Vapor fraction y: ")))
    total = total + y[i]
    if y[i] < 0:
        valid = False
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
    print('Check pressure, component\ncount, and range')
elif not valid or abs(total - 1.0) > 0.001:
    print('Fractions must be non-negative\nand sum to 1')
else:
    flo = residual(lo)
    fhi = residual(hi)
    if flo * fhi > 0:
        print('Range does not bracket a\nsolution')
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
        print("Dew temperature:" + "\n" + str((lo + hi) / 2.0))
