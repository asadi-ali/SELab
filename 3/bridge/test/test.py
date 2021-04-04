import unittest

from src.mutliplication.multiplication_spec import MultiplicationSpec
from src.mutliplication.recursive_multiplication import RecursiveMultiplication
from src.mutliplication.standard_multiplication import StandardMultiplication
from src.power.power_spec import PowerSpec
from src.power.recursive_power import RecursivePower
from src.power.standard_power import StandardPower


class PowerTest(unittest.TestCase):
    def test_standard_power_standard_multiplication(self):
        multiplication_spec = MultiplicationSpec(StandardMultiplication())
        power_spec = PowerSpec(StandardPower(multiplication_spec))
        self.assertEqual(625, power_spec.power(5, 4))

    def test_standard_power_recursive_multiplication(self):
        multiplication_spec = MultiplicationSpec(RecursiveMultiplication())
        power_spec = PowerSpec(StandardPower(multiplication_spec))
        self.assertEqual(625, power_spec.power(5, 4))

    def test_recursive_power_standard_multiplication(self):
        multiplication_spec = MultiplicationSpec(StandardMultiplication())
        power_spec = PowerSpec(RecursivePower(multiplication_spec))
        self.assertEqual(625, power_spec.power(5, 4))

    def test_recursive_power_recursive_multiplication(self):
        multiplication_spec = MultiplicationSpec(RecursiveMultiplication())
        power_spec = PowerSpec(RecursivePower(multiplication_spec))
        self.assertEqual(625, power_spec.power(5, 4))
