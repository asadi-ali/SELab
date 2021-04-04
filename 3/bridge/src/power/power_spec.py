from src.power.power import Power


class PowerSpec(object):
    def __init__(self, power: Power):
        self._power = power

    def power(self, a: int, b: int):
        return self._power.power(a, b)
