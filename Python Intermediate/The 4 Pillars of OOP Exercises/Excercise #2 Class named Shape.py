from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be greater than zero.")
        self._radius = radius

    def calculate_area(self) -> float:
        return math.pi * self._radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self._radius


class Square(Shape):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Side length must be greater than zero.")
        self._side = side

    def calculate_area(self) -> float:
        return self._side ** 2

    def calculate_perimeter(self) -> float:
        return 4 * self._side


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be greater than zero.")
        self._width = width
        self._height = height

    def calculate_area(self) -> float:
        return self._width * self._height

    def calculate_perimeter(self) -> float:
        return 2 * (self._width + self._height)


def main() -> None:
    shapes: list[Shape] = [
        Circle(5),
        Square(4),
        Rectangle(3, 6)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__}")
        print("Area:", shape.calculate_area())
        print("Perimeter:", shape.calculate_perimeter())
        print("-" * 30)


if __name__ == "__main__":
    main()
