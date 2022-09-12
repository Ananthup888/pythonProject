#sphere volume = 4/3*pi*r*r*r
import math
class Sphere:
    def __init__(self):
        self.r=int(input('Enter the radius'))
    def volume(self):
        v=(4/3)*math.pi*self.r**3
        print("Volume of sphere is=",round(v,3))
s1=Sphere()
s1.volume()