import abc

from src.mutliplication.multiplication_spec import MultiplicationSpec


class Power(abc.ABC):
    def __init__(self, multiplication: MultiplicationSpec):
        self.multiplication = multiplication

    @abc.abstractmethod
    def power(self, a: int, b: int):
        pass