from src.power.power import Power


class RecursivePower(Power):
    def power(self, a: int, b: int):
        if b == 0:
            return 1

        return self.multiplication.multiply(self.power(a, b - 1), a)
