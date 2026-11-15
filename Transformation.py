import math
import matplotlib.pyplot as plt


# ---------- Each function uses a simple formula on every point ----------

def translate(points, tx, ty):
    new = []
    for (x, y) in points:
        new.append((x + tx, y + ty))
    return new


def scale(points, sx, sy):
    new = []
    for (x, y) in points:
        new.append((x * sx, y * sy))
    return new


def rotate(points, angle):
    a = math.radians(angle)
    new = []
    for (x, y) in points:
        xn = x * math.cos(a) - y * math.sin(a)
        yn = x * math.sin(a) + y * math.cos(a)
        new.append((round(xn, 2), round(yn, 2)))
    return new


def reflect_x_axis(points):
    new = []
    for (x, y) in points:
        new.append((x, -y))
    return new


def reflect_y_axis(points):
    new = []
    for (x, y) in points:
        new.append((-x, y))
    return new


def reflect_origin(points):
    new = []
    for (x, y) in points:
        new.append((-x, -y))
    return new


def reflect_line_yx(points):
    new = []
    for (x, y) in points:
        new.append((y, x))
    return new


def shear_x(points, shx):
    new = []
    for (x, y) in points:
        new.append((x + shx * y, y))
    return new


def shear_y(points, shy):
    new = []
    for (x, y) in points:
        new.append((x, y + shy * x))
    return new


def shear_both(points, shx, shy):
    new = []
    for (x, y) in points:
        new.append((x + shx * y, y + shy * x))
    return new


# ---------- Drawing one result in a small box ----------

def draw(n, title, old, new):
    print(title, ":", new)

    plt.subplot(3, 4, n)
    ox = [p[0] for p in old] + [old[0][0]]
    oy = [p[1] for p in old] + [old[0][1]]
    nx = [p[0] for p in new] + [new[0][0]]
    ny = [p[1] for p in new] + [new[0][1]]

    plt.plot(ox, oy, 'b-o')
    plt.plot(nx, ny, 'r-o')
    plt.title(title, fontsize=9)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(True)
    plt.axis("equal")


# ---------- Taking user input ----------

print("Enter the 3 points of the triangle")
points = []
for i in range(3):
    x = float(input("Enter x" + str(i + 1) + ": "))
    y = float(input("Enter y" + str(i + 1) + ": "))
    points.append((x, y))

print("\n--- Translation ---")
tx = float(input("Enter tx: "))
ty = float(input("Enter ty: "))

print("\n--- Uniform scaling ---")
s = float(input("Enter scale factor s: "))

print("\n--- Non-uniform scaling ---")
sx = float(input("Enter sx: "))
sy = float(input("Enter sy: "))

print("\n--- Rotation ---")
angle = float(input("Enter angle in degrees (anticlockwise): "))

print("\n--- Shearing ---")
shx = float(input("Enter shx: "))
shy = float(input("Enter shy: "))

print("\n--- Composite (translate, then rotate, then scale) ---")
ctx = float(input("Enter tx: "))
cty = float(input("Enter ty: "))
cangle = float(input("Enter angle: "))
cs = float(input("Enter scale factor: "))


# ---------- Calling the functions and showing results ----------

print("\nOriginal :", points)
print()

# 1. Translation
draw(1, "Translation", points, translate(points, tx, ty))

# 2. Uniform scaling (same factor)
draw(2, "Uniform scaling", points, scale(points, s, s))

# 3. Non-uniform scaling (different factors)
draw(3, "Non-uniform scaling", points, scale(points, sx, sy))

# 4. Rotation
draw(4, "Rotation", points, rotate(points, angle))

# 5. Reflection (no input needed)
draw(5, "Reflection x-axis", points, reflect_x_axis(points))
draw(6, "Reflection y-axis", points, reflect_y_axis(points))
draw(7, "Reflection origin", points, reflect_origin(points))
draw(8, "Reflection y = x", points, reflect_line_yx(points))

# 6. Shearing
draw(9, "x-axis shearing", points, shear_x(points, shx))
draw(10, "y-axis shearing", points, shear_y(points, shy))
draw(11, "Both shearing", points, shear_both(points, shx, shy))

# 7. Composite transformation (one after another)
step1 = translate(points, ctx, cty)
step2 = rotate(step1, cangle)
step3 = scale(step2, cs, cs)
draw(12, "Composite", points, step3)

plt.tight_layout()
plt.show()