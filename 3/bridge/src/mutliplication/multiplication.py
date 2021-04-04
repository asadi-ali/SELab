import abc


class Multiplication(abc.ABC):
    @abc.abstractmethod
    def multiply(self, a: int, b: int):
        pass
