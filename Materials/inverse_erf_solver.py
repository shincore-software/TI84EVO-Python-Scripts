# Find lambda from an erf area or a normalized diffusion concentration.
# Input: an erf value between -1 and 1, or a concentration ratio from 0 to 1.
# Output: lambda, where erf(lambda) = area or erfc(lambda) = concentration ratio.

from math import exp


def erf_approx(x):
    # Abramowitz-Stegun 7.1.26 approximation.
    if x == 0:
        return 0.0
    z = abs(x)
    p = 0.3275911
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    t = 1.0 / (1.0 + p * z)
    poly = (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t
    value = 1.0 - poly * exp(-z * z)
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


def erfc_approx(x):
    # Abramowitz-Stegun 7.1.26 approximation for x >= 0.
    z = x
    p = 0.3275911
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    t = 1.0 / (1.0 + p * z)
    poly = (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t
    return poly * exp(-z * z)


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


print("Find lambda from:")
print("1: erf(lambda) = area")
print("2: diffusion concentration ratio")
mode = input("Select 1 or 2: ")

if mode == "1":
    area = float(input("Area (-1 to 1, no units): "))
    if area <= -1.0 or area >= 1.0:
        print("Area must be greater than -1 and less than 1")
    else:
        print("lambda (no units):")
        print(inverse_erf(area))
elif mode == "2":
    ratio = float(input("(C-C0)/(Cs-C0) (no units): "))
    if ratio <= 0.0 or ratio > 1.0:
        print("Ratio must be greater than 0 and at most 1")
    else:
        # The diffusion solution gives ratio = erfc(lambda) = 1 - erf(lambda).
        print("lambda (no units):")
        print(inverse_erfc(ratio))
else:
    print("Select 1 or 2")
