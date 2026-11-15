import matplotlib.pyplot as plt

def Bresenham_Line(x0, y0, x1, y1):

    # Calculate dx and dy
    dx = x1 - x0
    dy = y1 - y0

    # Calculate constants
    d1 = 2 * dy
    d2 = 2 * dy - 2 * dx

    # Initial decision parameter
    p = 2 * dy - dx

    x = x0
    y = y0

    points_x = []
    points_y = []

    # Plot the first point
    points_x.append(x)
    points_y.append(y)

    # Repeat until reaching the endpoint
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


# Take user input
x0 = int(input("Enter x0: "))
y0 = int(input("Enter y0: "))
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

# Call the function
points_x, points_y = Bresenham_Line(x0, y0, x1, y1)

# Draw the line
plt.plot(points_x, points_y, 'ro-')
plt.title("Bresenham's Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.show()

# Display the pixels
print("Pixels:", list(zip(points_x, points_y)))
print("Total pixels:", len(points_x))