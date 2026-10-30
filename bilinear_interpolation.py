# Bilinear interpolation for one rectangular grid cell.
# Enter x0 < x1 and y0 < y1.
# Enter z00 at (x0, y0), z10 at (x1, y0),
# z01 at (x0, y1), and z11 at (x1, y1).

def bilinear(x0, x1, y0, y1, z00, z10, z01, z11, x, y):
    tx = (x - x0) / (x1 - x0)
    ty = (y - y0) / (y1 - y0)

    low = z00 + tx * (z10 - z00)
    high = z01 + tx * (z11 - z01)
    return low + ty * (high - low)


x0 = float(input("x0: "))
x1 = float(input("x1: "))
y0 = float(input("y0: "))
y1 = float(input("y1: "))

if x1 <= x0 or y1 <= y0:
    print("Need x1>x0, y1>y0")
else:
    z00 = float(input("z at x0,y0: "))
    z10 = float(input("z at x1,y0: "))
    z01 = float(input("z at x0,y1: "))
    z11 = float(input("z at x1,y1: "))
    x = float(input("Find z at x: "))
    y = float(input("Find z at y: "))

    if x < x0 or x > x1 or y < y0 or y > y1:
        print("Point is outside cell")
    else:
        answer = bilinear(x0, x1, y0, y1,
                          z00, z10, z01, z11, x, y)
        print("Interpolated z:")
        print(answer)
