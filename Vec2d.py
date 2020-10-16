import math
import numpy as np
class Vec2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def display(self):
        return {f'{self.x} {self.y}'} 

    def __add__(self,other):
        return Vec2d(float(self.x)+float(other.x),float(self.y)+float(other.y))
    def __sub__(self,other):
        return Vec2d(self.x-other.x,self.y-other.y)
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
