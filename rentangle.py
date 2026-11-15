import matplotlib.pyplot as plt

x0=int(input("Enter x0: "))
y0=int(input("Enter y0: "))
x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))

# 4 corners in order
vx=[x0, x1, x1, x0]
vy=[y0, y0, y1, y1]

plot_x=[]
plot_y=[]

for i in range(4):
    xa=vx[i]
    ya=vy[i]
    xb=vx[(i+1)%4]    # last corner connects back to first
    yb=vy[(i+1)%4]

    dx=xb-xa
    dy=yb-ya
    steps=max(abs(dx),abs(dy))

    xinc=dx/steps
    yinc=dy/steps

    x=xa
    y=ya
    for j in range(steps+1):
        plot_x.append(round(x))
        plot_y.append(round(y))
        x+=xinc
        y+=yinc

plt.plot(plot_x,plot_y,'ro-')
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.grid(True)
plt.axis("equal")
plt.show()