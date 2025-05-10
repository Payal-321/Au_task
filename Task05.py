class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def perimeter(self):
        p=2*(self.length+self.width)
        print("the Rectangle is:",p)
    def Area(self):
        Area=self.length*self.width
        print("the area is:",Area)
my_Rectangle=Rectangle(3,4)
my_Rectangle.perimeter()
my_Rectangle.Area()