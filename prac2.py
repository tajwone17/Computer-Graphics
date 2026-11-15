import numpy as np
import math
import matplotlib.pyplot as plt

def translation(tx,ty):
    return np.array([
        [1,0,tx],
        [0,1,ty],
        [0,0,1]
    ])
def scaling(sx,sy):
    return np.array([
            [sx,0,0],
            [0,sy,0],
            [0,0,1]
        ])
def rotation(angle):
    a=math.radians(angle)
    return np.array([
            [math.cos(a),-math.sin(a),0],
            [math.sin(a),math.cos(a),0],
            [0,0,1]
        ])
def shearing_x(sx):
     return np.array([
                [1,sx,0],
                [0,1,0],
                [0,0,1]
            ])
def shearing_y(sy):
     return np.array([
                [1,0,0],
                [sy,1,0],
                [0,0,1]
            ])
def shearing_both(sx,sy):
     return np.array([
                [1,sx,0],
                [sy,1,0],
                [0,0,1]
            ])            
def reflecting_x():
    return np.array([
                    [1,0,0],
                    [0,-1,0],
                    [0,0,1]
                ])
def reflecting_y():
    return np.array([
                    [-1,0,0],
                    [0,1,0],
                    [0,0,1]
                ])
def reflecting_origin():
    return np.array([
                    [-1,0,0],
                    [0,-1,0],
                    [0,0,1]
                ])
def reflecting_xy():
    return np.array([
                    [0,1,0],
                    [1,0,0],
                    [0,0,1]
                ])

def draw(title,n,M,p):
    new=M@p
    print(title)
    plt.subplot(3,4,n)
    x1=list(new[0])+[new[0][0]]
    y1=list(new[1])+[new[1][0]]
    x2=list(p[0])+[p[0][0]]
    y2=list(p[1])+[p[1][0]]
    plt.plot(x1,y1,'r-o',label="New")
    plt.plot(x2,y2,'b-o',label="Original")    
    plt.grid(True)
print("Enter 3 points: ")
x=[]
y=[]
for i in range(3):
    x.append(float(input("Enter x co-ordinate: ")))
    y.append(float(input("Enter y co-ordinate: ")))
p=np.array([x,y,[1,1,1]])    
# Scaling
sx = float(input("Enter tx: "))
sy = float(input("Enter ty: "))
a=float(input("Enter angle: "))
draw("Scaling",1,scaling(sx,sy),p)
draw( "Rotation",4, rotation(a), p)
plt.show()