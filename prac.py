import matplotlib.pyplot as plt

x0=int(input("Enter x0: "))
y0=int(input("Enter y0: "))
x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))

dx=x1-x0
dy=y1-y0
d1=2*dy
d2=2*dy-2*dx
p=2*dy-dx

x=x0
y=y0
plot_x=[]
plot_y=[]
plot_x.append(x)
plot_y.append(y)

while x<x1:
    x+=1

    if p<0:
        p+=d1
    else:
        p+=d2   
        y+=1
    plot_x.append(x)
    plot_y.append(y)     


plt.plot(plot_x,plot_y,'ro-')
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.grid(True)
plt.axis("equal")
plt.show()