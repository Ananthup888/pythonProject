#using class find the area of rectangles
class Rectangle:
    def readdata(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        a=self.length*self.breadth
        print('Area is',a)
rect1=Rectangle()
rect2=Rectangle()
rect3=Rectangle()
rect1.readdata(10,5)
rect2.readdata(12,7)
rect3.readdata(8,6)
rect1.area()
rect2.area()
rect3.area()
