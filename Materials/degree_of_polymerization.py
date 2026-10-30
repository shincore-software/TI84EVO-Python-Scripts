# Calculate degree of polymerization from an average mer mass.
# Inputs: choose Mn or Mw, enter it, then enter each mer fraction xj and mass Mj.
# Mbar is the average molecular weight (weight) of one mer.
# Output: Mbar and dimensionless degree of polymerization.

print("Average molecular weight:")
print("1: Number average Mn")
print("2: Weight average Mw")
mode = input("Select 1 or 2: ")

if mode == "1":
    M = float(input("Number-average Mn: "))
    label = "Number-average DPn:"
elif mode == "2":
    M = float(input("Weight-average Mw: "))
    label = "Weight-average DPw:"
else:
    M = 0.0
    label = ""
    print("Select 1 or 2")

if mode == "1" or mode == "2":
    n = int(input("Number of mer types: "))
    if M <= 0 or n < 1:
        print("Need positive M and at least one mer type")
    else:
        total_x = 0.0
        Mbar = 0.0
        valid = True
        i = 0
        while i < n:
            print("Mer type:")
            print(i + 1)
            xj = float(input("Chain fraction xj: "))
            Mj = float(input("Mer molecular weight Mj: "))
            if xj < 0 or Mj <= 0:
                valid = False
            total_x = total_x + xj
            Mbar = Mbar + xj * Mj
            i = i + 1
        if not valid:
            print("xj must be non-negative; Mj must be positive")
        elif abs(total_x - 1.0) > 0.001:
            print("Chain fractions must sum to 1")
        elif Mbar <= 0:
            print("Average mer mass must be positive")
        else:
            DP = M / Mbar
            print("Weight of one mer, Mbar:")
            print(Mbar)
            print(label)
            print(DP)
