import matplotlib.pyplot as plt


# Bresenham's Circle Drawing Algorithm
def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    p = 3 - 2 * r

    pixels = []

    while x <= y:
        points = [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ]

        for point in points:
            pixels.append(point)

        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y = y - 1

        x = x + 1

    return pixels


# Midpoint Circle Drawing Algorithm
def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    pixels = []

    while x <= y:
        points = [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ]

        for point in points:
            pixels.append(point)

        x = x + 1

        if p < 0:
            p = p + 2 * x + 1
        else:
            y = y - 1
            p = p + 2 * (x - y) + 1

    return pixels


# Taking user input
xc = int(input("Enter center x-coordinate: "))
yc = int(input("Enter center y-coordinate: "))
r = int(input("Enter radius: "))

if r < 0:
    print("Radius cannot be negative.")

else:
    # Calling both functions
    b_pixels = bresenham_circle(xc, yc, r)
    m_pixels = midpoint_circle(xc, yc, r)

    # Display Bresenham pixels
    print("\n===== BRESENHAM CIRCLE =====")
    print("Generated pixels:", len(b_pixels))
    print("Pixel coordinates:", b_pixels)

    # Display Midpoint pixels
    print("\n===== MIDPOINT CIRCLE =====")
    print("Generated pixels:", len(m_pixels))
    print("Pixel coordinates:", m_pixels)

    # Convert to sets to compare unique coordinates
    b_set = set(b_pixels)
    m_set = set(m_pixels)

    common = b_set & m_set
    b_only = b_set - m_set
    m_only = m_set - b_set
    different = b_set ^ m_set

    # Display comparison
    print("\n===== COMPARISON =====")
    print("Bresenham total generated:", len(b_pixels))
    print("Midpoint total generated:", len(m_pixels))

    print("Bresenham unique pixels:", len(b_set))
    print("Midpoint unique pixels:", len(m_set))

    print("Common pixels:", len(common))
    print("Bresenham-only pixels:", len(b_only))
    print("Midpoint-only pixels:", len(m_only))
    print("Total different pixels:", len(different))

    print("\nCommon coordinates:", sorted(common))
    print("Bresenham-only coordinates:", sorted(b_only))
    print("Midpoint-only coordinates:", sorted(m_only))

    # Draw both circles
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(
        [p[0] for p in b_pixels],
        [p[1] for p in b_pixels],
        'ro'
    )
    plt.title("Bresenham Circle")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.axis("equal")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(
        [p[0] for p in m_pixels],
        [p[1] for p in m_pixels],
        'bo'
    )
    plt.title("Midpoint Circle")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.axis("equal")
    plt.grid(True)

    plt.tight_layout()
    plt.show()