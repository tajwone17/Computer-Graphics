import matplotlib.pyplot as plt

n=int(input("Enter number of corners: "))

vx=[]
vy=[]
for i in range(n):
    vx.append(int(input("Enter x"+str(i)+": ")))
    vy.append(int(input("Enter y"+str(i)+": ")))

plot_x=[]
plot_y=[]

for i in range(n):
    xa=vx[i]
    ya=vy[i]
    xb=vx[(i+1)%n]    # last corner connects back to first
    yb=vy[(i+1)%n]

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