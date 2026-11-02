# Parabolic rate law
# Solve the parabolic mass-gain rate law for delta_m, Kp, or time t.
# Units: delta_m in kg/m^2, Kp in kg^2/(m^4*s), and t in seconds.
# Formula: delta_m = sqrt(Kp * t).

from math import sqrt


print("delta_m = sqrt(Kp * t)")
print("Find:")
print("1: delta_m")
print("2: Kp")
print("3: time t")
mode = input("Select 1, 2, or 3: ")

if mode == "1":
    Kp = float(input("Kp (kg^2/(m^4*s)): "))
    t = float(input("Time t (s): "))
    if Kp < 0 or t < 0:
        print('Kp and time must be\nnon-negative')
    else:
        delta_m = sqrt(Kp * t)
        print("delta_m (kg/m^2):" + "\n" + str(delta_m))
elif mode == "2":
    delta_m = float(input("delta_m (kg/m^2): "))
    t = float(input("Time t (s): "))
    if delta_m < 0 or t <= 0:
        print('delta_m must be non-negative;\ntime must be positive')
    else:
        Kp = delta_m * delta_m / t
        print("Kp (kg^2/(m^4*s)):" + "\n" + str(Kp))
elif mode == "3":
    delta_m = float(input("delta_m (kg/m^2): "))
    Kp = float(input("Kp (kg^2/(m^4*s)): "))
    if delta_m < 0 or Kp <= 0:
        print('delta_m must be non-negative;\nKp must be positive')
    else:
        t = delta_m * delta_m / Kp
        print("Time t (s):" + "\n" + str(t))
else:
    print("Select 1, 2, or 3")
