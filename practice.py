import matplotlib.pyplot as plt

def bresenham_cricle(xc,yc,r):
    x=0
    y=r
    p=3-2*r
    points_x=[]
    points_y=[]
    pixelsB=[]  
    octants = [[] for _ in range(8)]
  
    while x<=y:
        points=[
                (xc+x,yc+y),
                (xc-x,yc+y),
                (xc+x,yc-y),
                (xc-x,yc-y),
                (xc+y,yc+x),
                (xc-y,yc+x),
                (xc+y,yc-x),
                (xc-y,yc-x)
                ]
        for i in range(8):
            octants[i].append(points[i])
            pixelsB.append(points[i])
            points_x.append(points[i][0])
            points_y.append(points[i][1])
        if p<0:
            p=p+4*x+6
        else:
            p=p+4*(x-y)+10
            y=y-1

        x=x+1
    return points_x,points_y,octants,pixelsB


def midPoint(xc,yc,r):
    points_x=[]
    points_y=[]
    pixels=[]  
    x=0
    y=r
    p=1-r
    while x<=y:
        points=[
                (xc+x,yc+y),
                (xc-x,yc+y),
                (xc+x,yc-y),
                (xc-x,yc-y),
                (xc+y,yc+x),
                (xc-y,yc+x),
                (xc+y,yc-x),
                (xc-y,yc-x)
                ]
        for i in range(8):
            points_x.append(points[i][0])
            points_y.append(points[i][1])
            pixels.append(points[i])
        x=x+1    
        if p<0:
            p=p+2*x+1
        else:
            p=p+2*(x-y)+1
            y=y-1    
    return points_x,points_y,pixels    
x=int(input("Enter x"))
y=int(input("Enter y"))
ro=int(input("ENter radius"))
points_x,points_y,pixelsM=midPoint(x,y,ro)

print(pixelsM)

points_x,points_y,octants,pixelsB=bresenham_cricle(x,y,ro)
for i in range(8):
    print("Octant",i+1,octants[i])
print(points_x)
print(points_y)
uniqueM=set(pixelsM)

total_pixels_m=len(pixelsM)
total_pixels_B=len(pixelsB)
common=pixelsM & pixelsB
dif=pixelsM^pixelsB

plt.plot(points_x,points_y,"ro")
plt.grid(True)
plt.axis("equal")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()