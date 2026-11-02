# Infinite-dilution activity coefficients and Henry constants.
# Inputs: model, component, model parameters, and saturation pressure.
# Output: ln(gamma infinity), gamma infinity, and Henry constant H.
from math import exp, log


print("Model:")
print("1: Margules 1")
print("2: Margules 2")
print("3: van Laar")
print("4: Wilson")
print("5: NRTL")
mode = input("Select 1-5: ")
component = input("Find component 1 or 2: ")
if component == "1":
    index = 1
elif component == "2":
    index = 2
else:
    index = 0

if index == 0:
    print("Select component 1 or 2")
else:
    if mode == "1":
        A = float(input("A: "))
        lng = A
    elif mode == "2":
        A12 = float(input("A12: "))
        A21 = float(input("A21: "))
        if index == 1:
            lng = A12
        else:
            lng = A21
    elif mode == "3":
        A12 = float(input("A12: "))
        A21 = float(input("A21: "))
        if index == 1:
            lng = A12
        else:
            lng = A21
    elif mode == "4":
        L12 = float(input("Lambda12: "))
        L21 = float(input("Lambda21: "))
        if L12 <= 0 or L21 <= 0:
            print("Lambda values must be positive")
            lng = 0.0
            mode = "bad"
        elif index == 1:
            lng = -log(L12) + 1.0 - L21
        else:
            lng = -log(L21) + 1.0 - L12
    elif mode == "5":
        T = float(input("Temperature T: "))
        R = float(input("Gas constant R: "))
        b12 = float(input("b12: "))
        b21 = float(input("b21: "))
        alpha = float(input("Alpha: "))
        if T <= 0 or R == 0:
            print('T must be positive and R\nnon-zero')
            lng = 0.0
            mode = "bad"
        else:
            t12 = b12 / (R * T)
            t21 = b21 / (R * T)
            if index == 1:
                lng = t21 + t12 * exp(-alpha * t12)
            else:
                lng = t12 + t21 * exp(-alpha * t21)
    else:
        print("Select a model from 1 to 5")
        lng = 0.0
        mode = "bad"

    if mode != "bad":
        g = exp(lng)
        psat = float(input("Psat (same units as H): "))
        print("ln gamma infinite:" + "\n" + str(lng))
        print("gamma infinite:" + "\n" + str(g))
        print("Henry constant H:" + "\n" + str(g * psat))
