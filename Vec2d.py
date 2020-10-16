import math
import numpy as np
class Vec2d:
    def __init__(self,x:float,y:float):
        self.x=x
        self.y=y

    def display(self):
        return {f'{self.x} {self.y}'} 


    def __add__(self, other):
        if isinstance(other,self.__class__):
            return Vec2d(self.x + other.x , self.y + other.y)
        return Vec2d(self.x + other,self.y + other)
    
    def __sub__(self, other):
        if isinstance(other,self.__class__):
            return Vec2d(self.x - other.x , self.y - other.y)
        return Vec2d(self.x - other,self.y - other)
    
    def __mul__(self, other):
        if isinstance(other,self.__class__):
            return Vec2d(self.x * other.x , self.y * other.y)
        return Vec2d(self.x * other,self.y * other)
    
    def __truediv__(self, other):
        if isinstance(other,self.__class__):
            return Vec2d(self.x / other.x , self.y / other.y)
        return Vec2d(self.x / other, self.y / other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __eq__(self, other):
        if isinstance(other,self.__class__):
            return Vec2d(self.x == other.x and  self.y == other.y)
        return Vec2d(self.x == other, self.y == other)
    def normalize(vec):
        vec_length = length(vec)
        if vec_length < 0.00001:
            return Vec2d(0, 1)
        return Vec2d(vec.x / vec_length, vec.y / vec_length)    
def dot(self,other):
    return self.x * other.x + self.y * other.y

def angle_between(self,other):
    return math.acos(dot(self,other))
def length(self):  
    return math.sqrt( self.x**2 + self.y**2 )
    def distance(self,other):
        return (other-self).length()
    def  __str__(self):   
        return (f'Vec2d({self.x},{self.y}')
    def tuple(self): return (self.x,self.y)
    
    def norm(self):
        return Vec2d(self.x/self.length(),self.y/self.length())
    def scale(self,s):
        return Vec2d(self.x*s,self.y*s)
    #def norms(self): 
    #    return self.scale(1.0/self.length())

    def scalevec(self,other):
         return Vec2d(self.x*other.x,self.y*other.y)

a=Vec2d(1,1).normalize()
b=Vec2d(1,1).normalize()

print(angle_between(a,b))
