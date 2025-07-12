from Shape_form2.module1 import Shape


class Triangle(Shape):
    def __init__(self, b:float, h:float):
        super().__init__()
        self.b = b
        self.h = h

    def compute_area(self) -> float:
        return (self.b * self.h) / 2
    
    
class Equilateral(Triangle):
    pass

class Isosceles(Triangle):
    pass

class Scalene(Triangle):
    pass

class TriRectangle(Triangle):
    pass