from src.mutliplication.multiplication import Multiplication


class RecursiveMultiplication(Multiplication):
    def multiply(self, a: int, b: int):
        if b == 0:
            return 0
        return a + self.multiply(a, b - 1)
