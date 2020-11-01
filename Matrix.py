import numpy as np
import math
from Vec2d import Vec2d

def RotMatrix(angle):
    c,s=math.cos(angle),math.sin(angle)
    return [[c,-s],[s,c]]
    

def multiply_matrix_point(mat,point):
   return Vec2d(mat[0][0]*point.x + mat[0][1]*point.y ,mat[1][0]*point.x + mat[1][1]*point.y )



rotation=RotMatrix(np.radians(90))
print(f"Rotation matrix -> {rotation}")

b=Vec2d(1,3)
print(f"Vector b -> {b}")

c=multiply_matrix_point(rotation,b)

print(f"Rotation applied on vector {c}")

Centre=Vec2d(2,3)
d=c+Centre
print(f"Centre Translation {d}")
