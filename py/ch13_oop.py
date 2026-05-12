# Inheritance

class Shape:    # PARENT CLASS
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0
    
class Rectangle(Shape):    # CHILD CLASS
    def __init__(self, width, height):
        super().__init__("Rectangle")   # Call the parent class constructor
        self.width = width
        self.height = height
    
    def area(self):    # Override the parent class method
        return self.width * self.height

class Circle(Shape):    # CHILD CLASS
    def __init__(self, radius):
        super().__init__("Circle")   # Call the parent class constructor
        self.radius = radius

    def area(self):    # Override the parent class method
        return 3.14 * self.radius ** 2
    
class Square(Shape):    # CHILD CLASS
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2

# Create inherited 'name' attribute for Shape class
circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(4)

print(f"{circle.name} area: {circle.area()}")
print(f"{rectangle.name} area: {rectangle.area()}")
print(f"{square.name} area: {square.area()}")

#Polymorphism  

def print_area(shape):      #Takes a shape object as an argument
    print(f"{shape.name} area: {shape.area()}")

# Same method call, different behavior based on the object type
print_area(circle)        # Circle area: 78.5
print_area(rectangle)     # Rectangle area: 24
print_area(square)        # Square area: 16

# Or with a list of shapes
shapes = [Circle(3), Rectangle(4, 6), Square(4)]
for shape in shapes:
    print_area(shape)    # Polymorphic behavior: same method call, different output based on the shape type 
