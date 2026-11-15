import matplotlib.pyplot as plt

def elipse(xc,yc,a,b):
    points_x=[]
    points_y=[]
    quadrant=[[]for _ in range(4)]
    a2=a*a
    b2=b*b
    x=0
    y=b
    # region 1
    p=b2-a2*b+0.25*a2
    while 2*b2*x<2*a2*y:
        points=[
            (xc+x,yc+y),
            (xc-x,yc+y),
            (xc-x,yc-y),
            (xc+x,yc-y)
        ]
        for i in range(4):
           quadrant.append(points[i])
           points_x.append(points[i][0])
           points_y.append(points[i][1])
        x=x+1

        if p<0:
            p=p+b2+2*b2*x
        else:
            y=y-1
            p=p+b2+2*b2*x-2*a2*y    
           
    # region2
    p=b2*(x+.5)**2+a2*(y-1)**2-a2*b2
    while y>=0:
        points=[
            (xc+x,yc+y),
            (xc-x,yc+y),
            (xc-x,yc-y),
            (xc+x,yc-y)
        ]
        for i in range(4):
            quadrant.append(points[i])
            points_x.append(points[i][0])
            points_y.append(points[i][1])
        y=y-1
    
        if p>0:
            p=p+a2-2*a2*y
        else:
            x=x+1
            p=p+a2+2*b2*x-2*a2*y    
           
    return points_x,points_y

xc=int(input("Enter Center X"))
yc=int(input("Enter Center y"))
a=int(input())
b=int(input())        
points_x,points_y=elipse(xc,yc,a,b)
plt.plot(points_x, points_y, 'ro')
plt.title("Midpoint Ellipse Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.show()