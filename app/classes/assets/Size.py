

class Size:

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value: int):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value: int):
        self.__height = value
