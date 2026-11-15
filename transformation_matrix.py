
import math
import numpy as np
import matplotlib.pyplot as plt


# Transformation functions

def translation(tx, ty):
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])


def scaling(sx, sy):
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, 1]])


def rotation(angle):
    a = math.radians(angle)
    return np.array([[math.cos(a), -math.sin(a), 0],
                     [math.sin(a),  math.cos(a), 0],
                     [0, 0, 1]])


def reflection_x():
    return np.array([[1, 0, 0],
                     [0, -1, 0],
                     [0, 0, 1]])


def reflection_y():
    return np.array([[-1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])


def reflection_origin():
    return np.array([[-1, 0, 0],
                     [0, -1, 0],
                     [0, 0, 1]])


def reflection_yx():
    return np.array([[0, 1, 0],
                     [1, 0, 0],
                     [0, 0, 1]])


def shear_x(shx):
    return np.array([[1, shx, 0],
                     [0, 1, 0],
                     [0, 0, 1]])


def shear_y(shy):
    return np.array([[1, 0, 0],
                     [shy, 1, 0],
                     [0, 0, 1]])


def shear_both(shx, shy):
    return np.array([[1, shx, 0],
                     [shy, 1, 0],
                     [0, 0, 1]])


# Draw original and transformed triangle

def draw(n, title, M, P):

    new = M @ P

    print("\n", title)
    print("Matrix:")
    print(M)
    print("New points:")
    print(new[:2])

    plt.subplot(3, 4, n)

    x1 = list(P[0]) + [P[0][0]]
    y1 = list(P[1]) + [P[1][0]]

    x2 = list(new[0]) + [new[0][0]]
    y2 = list(new[1]) + [new[1][0]]

    plt.plot(x1, y1, 'b-o', label="Original")
    plt.plot(x2, y2, 'r-o', label="New")

    plt.title(title)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid()
    plt.axis("equal")


# Input triangle points

print("Enter 3 points of triangle")

x = []
y = []

for i in range(3):
    x.append(float(input("Enter x: ")))
    y.append(float(input("Enter y: ")))

P = np.array([x, y, [1, 1, 1]])

print("\nOriginal points:")
print(P[:2])


# Input transformation values

tx = float(input("Enter tx: "))
ty = float(input("Enter ty: "))

s = float(input("Enter uniform scale: "))

sx = float(input("Enter sx: "))
sy = float(input("Enter sy: "))

angle = float(input("Enter rotation angle: "))

shx = float(input("Enter shx: "))
shy = float(input("Enter shy: "))


# Apply transformations

draw(1, "Translation", translation(tx, ty), P)

draw(2, "Uniform Scaling", scaling(s, s), P)

draw(3, "Non-uniform Scaling", scaling(sx, sy), P)

draw(4, "Rotation", rotation(angle), P)

draw(5, "Reflection X", reflection_x(), P)

draw(6, "Reflection Y", reflection_y(), P)

draw(7, "Reflection Origin", reflection_origin(), P)

draw(8, "Reflection Y=X", reflection_yx(), P)

draw(9, "Shearing X", shear_x(shx), P)

draw(10, "Shearing Y", shear_y(shy), P)

draw(11, "Both Shearing", shear_both(shx, shy), P)


# Composite transformation
# Translate -> Rotate -> Scale

tx = float(input("Enter composite tx: "))
ty = float(input("Enter composite ty: "))
angle = float(input("Enter composite angle: "))
s = float(input("Enter composite scale: "))

M1 = translation(tx, ty)
M2 = rotation(angle)
M3 = scaling(s, s)

M = M3 @ M2 @ M1

draw(12, "Composite", M, P)


plt.tight_layout()
plt.show()
