from Shape_form2.module1 import Shape


class Rectangle(Shape):
    def __init__(self, b:float, h:float):
        super().__init__()
        self.b = b
        self.h = h

    def compute_area(self) -> float:
        return self.b * self.h
    
    def compute_perimeter(self) -> float:
        return 2*self.b + 2*self.h
    

class Square(Rectangle):
    def __init__(self, l:float):
        super().__init__()
        self.l = l

    def compute_area(self) -> float:
        return self.l ** 2
    
    def compute_perimeter(self) -> float:
        return 4*self.l
