from abc import ABC

from src.mutliplication.multiplication import Multiplication


class StandardMultiplication(Multiplication):
    def multiply(self, a: int, b: int):
        return a * b
