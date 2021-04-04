from src.power.power import Power


class StandardPower(Power):
    def power(self, a: int, b: int):
        res = 1
        for i in range(b):
            res = self.multiplication.multiply(res, a)
        return res
