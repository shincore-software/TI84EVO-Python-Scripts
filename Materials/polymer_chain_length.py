# Calculate projected chain length and average end-to-end distance.
# Select L, r, or both. Enter the values that the selected calculation needs.
# Inputs: bond length d, bond count N, and angle theta in degrees for L.
# Output: selected chain length value or values.

from math import radians, sin, sqrt

print("Find value:")
print("1: Projected chain length L")
print("2: Average end-to-end distance r")
print("3: Find both L and r")
print("4: Find d from r and N")
mode = input("Select 1-4: ")

if mode not in ("1", "2", "3", "4"):
    print("Select 1, 2, 3, or 4")
elif mode == "4":
    r = float(input("Average end-to-end distance r: "))
    N = int(input("Number of bonds N: "))
    if r <= 0 or N <= 0:
        print("r and N must be positive")
    else:
        d = r / sqrt(N)
        print("Bond length d:")
        print(d)
else:
    d = float(input("Bond length d: "))
    N = int(input("Number of bonds N: "))
    if d <= 0 or N <= 0:
        print("d and N must be positive")
    elif mode == "1" or mode == "3":
        theta = float(input("Angle deg (sp3 ~109): "))
        if theta <= 0 or theta >= 180:
            print("theta must be between 0 and 180 deg")
        else:
            L = N * d * sin(radians(theta / 2.0))
            print("Projected chain length L:")
            print(L)
            if mode == "3":
                r = d * sqrt(N)
                print("Average end-to-end distance r:")
                print(r)
    else:
        r = d * sqrt(N)
        print("Average end-to-end distance r:")
        print(r)
