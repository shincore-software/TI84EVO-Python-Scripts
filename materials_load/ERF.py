# Error function
# Calculate erf(x), erfc(x), or inverse erf values.
# Input: select a calculation, then enter x, an erf area, or a diffusion ratio.
# Output: approximate erf values or lambda. The result is dimensionless.
# TI-Python does not list erf or erfc in its math module.

from math import exp



def erfc_approx(x):
    z = abs(x)
    p = 0.3275911
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    t = 1.0 / (1.0 + p * z)
    poly = (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t
    erfc_pos = poly * exp(-z * z)
    if x >= 0:
        return erfc_pos
    return 2.0 - erfc_pos


def erf_approx(x):
    if x == 0:
        return 0.0
    value = 1.0 - erfc_approx(abs(x))
    if x < 0:
        return -value
    return value


def inverse_erf(area):
    # Bisection for -1 < area < 1.
    low = -6.0
    high = 6.0
    for i in range(50):
        mid = (low + high) / 2.0
        if erf_approx(mid) < area:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0


def inverse_erfc(ratio):
    # Find x >= 0 where erfc_approx(x) is close to ratio.
    if ratio == 1.0:
        return 0.0
    low = 0.0
    high = 1.0
    count = 0
    while erfc_approx(high) > ratio and count < 32:
        high = high * 2.0
        count = count + 1
    for i in range(40):
        mid = (low + high) / 2.0
        if mid == low or mid == high:
            break
        if erfc_approx(mid) > ratio:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0


print("Error function")
print("erfc(x)=1-erf(x)")
print("1: erf(x) and erfc(x)")
print("2: inverse erf from area")
print("3: lambda from diffusion ratio")
mode = input("Select 1, 2, or 3: ")

if mode == "1":
    x = float(input("x (no units): "))
    print("Approximate erf(x):" + "\n" + str(erf_approx(x)))
    print("Approximate erfc(x):" + "\n" + str(erfc_approx(x)))
elif mode == "2":
    area = float(input("Area (-1 to 1, no units): "))
    if area <= -1.0 or area >= 1.0:
        print('Area must be greater than -1\nand less than 1')
    else:
        print("lambda (no units):" + "\n" + str(inverse_erf(area)))
elif mode == "3":
    ratio = float(input("(C-C0)/(Cs-C0) (no units): "))
    if ratio <= 0.0 or ratio > 1.0:
        print('Ratio must be greater than 0\nand at most 1')
    else:
        # The diffusion solution gives ratio = erfc(lambda) = 1 - erf(lambda).
        print("lambda (no units):" + "\n" + str(inverse_erfc(ratio)))
else:
    print("Select 1, 2, or 3")
