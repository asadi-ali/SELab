from .shape import Shape


class Square(Shape):
    def __init__(self, length: int):
        self.length: int = length

    def compute_area(self) -> int:
        pass

    def set_length(self, length: int) -> None:
        pass

    def get_length(self) -> int:
        pass
