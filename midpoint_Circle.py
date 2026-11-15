import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    points_x = []
    points_y = []
    octants = [[] for _ in range(8)]

    while x <= y:
        points = [
            (xc + x, yc + y),   # Octant 1
            (xc + y, yc + x),   # Octant 2
            (xc + y, yc - x),   # Octant 3
            (xc + x, yc - y),   # Octant 4
            (xc - x, yc - y),   # Octant 5
            (xc - y, yc - x),   # Octant 6
            (xc - y, yc + x),   # Octant 7
            (xc - x, yc + y)    # Octant 8
        ]

        for i in range(8):
            octants[i].append(points[i])
            points_x.append(points[i][0])
            points_y.append(points[i][1])

        x = x + 1

        if p < 0:
            p = p + 2 * x + 1
        else:
            y = y - 1
            p = p + 2 * (x - y) + 1

    return points_x, points_y, octants


# Taking user input
xc = int(input("Enter center x-coordinate: "))
yc = int(input("Enter center y-coordinate: "))
r = int(input("Enter radius: "))

# Calling the function
points_x, points_y, octants = midpoint_circle(xc, yc, r)

# Printing outside the function
print("\nPixels in each octant:")
for i in range(8):
    print("Octant", i + 1, ":", octants[i])

# Drawing outside the function
plt.plot(points_x, points_y, 'ro')
plt.title("Midpoint Circle Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.show()