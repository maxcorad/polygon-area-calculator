class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = self.width * 2 + self.height * 2
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = (self.width**2 + self.height**2)**.5
        return self.diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            line = self.width * "*" + "\n"
            picture = self.height * line
            return picture

    def get_amount_inside(self, other):
        return (self.width // other.width) * (self.height // other.height)


class Square:
    def __init__(self, side):
        self.set_side(side)
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, width):
        self.set_side(width)
    
    def set_length(self, length):
        self.set_side(length)
    
    def __str__(self):
        return f"Square(side={self.width})"
