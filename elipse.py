import matplotlib.pyplot as plt

def midpoint_ellipse(xc, yc, a, b):
    a2 = a * a
    b2 = b * b

    x = 0
    y = b

    points_x = []
    points_y = []
    quadrants = [[] for _ in range(4)]

    # Region 1 : slope magnitude < 1 (x increases every step)
    p = b2 - a2 * b + 0.25 * a2

    while 2 * b2 * x < 2 * a2 * y:
        points = [
            (xc + x, yc + y),   # Quadrant 1
            (xc - x, yc + y),   # Quadrant 2
            (xc - x, yc - y),   # Quadrant 3
            (xc + x, yc - y)    # Quadrant 4
        ]

        for i in range(4):
            quadrants[i].append(points[i])
            points_x.append(points[i][0])
            points_y.append(points[i][1])

        x = x + 1

        if p < 0:
            p = p + 2 * b2 * x + b2
        else:
            y = y - 1
            p = p + 2 * b2 * x + b2- 2 * a2 * y 

    # Region 2 : slope magnitude >= 1 (y decreases every step)
    p = b2 * (x + 0.5) ** 2 + a2 * (y - 1) ** 2 - a2 * b2

    while y >= 0:
        points = [
            (xc + x, yc + y),   # Quadrant 1
            (xc - x, yc + y),   # Quadrant 2
            (xc - x, yc - y),   # Quadrant 3
            (xc + x, yc - y)    # Quadrant 4
        ]

        for i in range(4):
            quadrants[i].append(points[i])
            points_x.append(points[i][0])
            points_y.append(points[i][1])

        y = y - 1
 
        if p > 0:
            p = p + a2 - 2 * a2 * y
        else:
            x = x + 1
            p = p + 2 * b2 * x - 2 * a2 * y + a2

    return points_x, points_y, quadrants


# Taking user input
xc = int(input("Enter center x-coordinate: "))
yc = int(input("Enter center y-coordinate: "))
a = int(input("Enter x-radius (a): "))
b = int(input("Enter y-radius (b): "))

# Calling the function
points_x, points_y, quadrants = midpoint_ellipse(xc, yc, a, b)

# Printing outside the function
print("\nPixels in each quadrant:")
for i in range(4):
    print("Quadrant", i + 1, ":", quadrants[i])

# Drawing outside the function
plt.plot(points_x, points_y, 'ro')
plt.title("Midpoint Ellipse Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.show()