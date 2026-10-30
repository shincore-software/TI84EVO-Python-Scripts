# Henry's law solver.
# Formula: y * P = x * H

print("Find value:")
print("1: y")
print("2: P")
print("3: x")
print("4: H")
mode = input("Select 1-4: ")

if mode == "1":
    P = float(input("Pressure P: "))
    x = float(input("Liquid fraction x: "))
    H = float(input("Henry constant H: "))
    if P == 0:
        print("P cannot be zero")
    else:
        print("y:")
        print(x * H / P)
elif mode == "2":
    y = float(input("Vapor fraction y: "))
    x = float(input("Liquid fraction x: "))
    H = float(input("Henry constant H: "))
    if y == 0:
        print("y cannot be zero")
    else:
        print("P:")
        print(x * H / y)
elif mode == "3":
    y = float(input("Vapor fraction y: "))
    P = float(input("Pressure P: "))
    H = float(input("Henry constant H: "))
    if H == 0:
        print("H cannot be zero")
    else:
        print("x:")
        print(y * P / H)
elif mode == "4":
    y = float(input("Vapor fraction y: "))
    P = float(input("Pressure P: "))
    x = float(input("Liquid fraction x: "))
    if x == 0:
        print("x cannot be zero")
    else:
        print("H:")
        print(y * P / x)
else:
    print("Select 1, 2, 3, or 4")
