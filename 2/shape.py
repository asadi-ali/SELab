import abc


class Shape(abc.ABC):

    @abc.abstractmethod
    def compute_area(self) -> int:
        pass
