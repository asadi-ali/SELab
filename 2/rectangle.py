from .shape import Shape


class Rectangle(Shape):
    def __init__(self, height: int, width: int):
        self.height: int = height
        self.width: int = width

    def compute_area(self) -> int:
        return self.height * self.width

    def set_height(self, new_height) -> int:
        pass

    def get_height(self) -> int:
        pass
