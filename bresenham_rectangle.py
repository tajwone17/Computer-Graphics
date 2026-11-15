import matplotlib.pyplot as plt

def Bresenham_Line(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    d1 = 2 * dy
    d2 = 2 * dy - 2 * dx
    p = 2 * dy - dx

    x = x0
    y = y0
    points_x = []
    points_y = []
    points_x.append(x)
    points_y.append(y)

    while x < x1:
        x = x + 1
        if p < 0:
            p = p + d1
        else:
            y = y + 1
            p = p + d2
        points_x.append(x)
        points_y.append(y)

    return points_x, points_y


x0 = int(input("Enter x0: "))
y0 = int(input("Enter y0: "))
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

# make sure left < right and bottom < top
xl = min(x0, x1)
xr = max(x0, x1)
yb = min(y0, y1)
yt = max(y0, y1)

# horizontal sides: normal call
bx, by = Bresenham_Line(xl, yb, xr, yb)    # bottom
tx, ty = Bresenham_Line(xl, yt, xr, yt)    # top

# vertical sides: swap x and y in the call, and swap the results back
ly, lx = Bresenham_Line(yb, xl, yt, xl)    # left
ry, rx = Bresenham_Line(yb, xr, yt, xr)    # right

plt.plot(bx, by, 'ro-')
plt.plot(tx, ty, 'ro-')
plt.plot(lx, ly, 'ro-')
plt.plot(rx, ry, 'ro-')

plt.title("Rectangle using Bresenham")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.show()