from src.mutliplication.multiplication import Multiplication


class MultiplicationSpec(object):
    def __init__(self, multiplication: Multiplication):
        self._multiplication = multiplication

    def multiply(self, a: int, b: int):
        return self._multiplication.multiply(a, b)
