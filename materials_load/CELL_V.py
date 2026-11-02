# Cell voltage

"""Solve one variable in Ecell=Ecath-Ean."""

print("Cell voltage")
print("Ecell=Ecath-Ean")

print('1: Ecell (V)')
print('2: Ecath (V)')
print('3: Ean (V)')
u = input("Solve: ")
if u not in ("1", "2", "3"):
    print("Bad choice")
else:
    names = ["Ecell", "Ecath", "Ean"]
    v = [0.0, 0.0, 0.0]
    k = int(u) - 1
    for i in range(3):
        if i != k:
            v[i] = float(input(names[i] + " V: "))
    if k == 0:
        v[0] = v[1] - v[2]
    elif k == 1:
        v[1] = v[0] + v[2]
    else:
        v[2] = v[1] - v[0]
    print(names[k] + " V = " + str(v[k]))
