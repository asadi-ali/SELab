from .shape import Shape


class Square(Shape):
    def __init__(self, length: int):
        self.length: int = length

    def compute_area(self) -> int:
        return self.length * self.length

    def set_length(self, length: int) -> None:
        self.length = length

    def get_length(self) -> int:
        return self.length
