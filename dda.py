import matplotlib.pyplot as plt

def DDA_Line(x0, y0, x1, y1):

    # Calculate dx and dy
    dx = x1 - x0
    dy = y1 - y0

    # Calculate steps
    steps = max(abs(dx), abs(dy))

    # Calculate increments
    xinc = dx / steps
    yinc = dy / steps

    # Initialize starting point
    x = x0
    y = y0

    points_x = []
    points_y = []

    # Generate points
    for i in range(0, steps + 1):
        points_x.append(round(x))
        points_y.append(round(y))

        x = x + xinc
        y = y + yinc

    return points_x, points_y


# Take user input
x0 = int(input("Enter x0: "))
y0 = int(input("Enter y0: "))
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

# Call the function
points_x, points_y = DDA_Line(x0, y0, x1, y1)

# Plot the line
plt.plot(points_x, points_y, 'ro-')
plt.title("DDA Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()