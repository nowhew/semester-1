# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width : int, height : int):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        
        if not isinstance(width, int):
            raise TypeError("width must be an int")
        if not isinstance(height, int):
            raise TypeError("height must be an int")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        
        self.width = width
        self.height = height

    def is_square(self) -> bool:
        """
        Returns if the Rectangle is as square
        """
        return self.width == self.height

    def area(self) -> int:
        """
        Returns the area of the Rectangle
        """
        return self.width * self.height

    def perimeter(self) -> int:
        """
        Returns the perimeter of the Rectangle
        """
        return 2*self.width + 2*self.height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
