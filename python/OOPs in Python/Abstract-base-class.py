from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle:
    type = "Rectangle"
    side = 4
    def __init__(self):
        self.length = 6
        self.breath = 7

    def printarea(self):
        return self.breath * self.length

rect1 = Rectangle()
print(rect1.printarea())