import unittest


class PowerTest(unittest.TestCase):
    def test_standard_power_standard_multiplication(self):
        power = StandardPower(StandardMultiplication())
        self.assertEqual(625, power.power(5, 4))

    def test_standard_power_recursive_multiplication(self):
        power = StandardPower(RecursiveMultiplication())
        self.assertEqual(625, power.power(5, 4))

    def test_recursive_power_standard_multiplication(self):
        power = RecursivePower(StandardMultiplication())
        self.assertEqual(625, power.power(5, 4))

    def test_recursive_power_recursive_multiplication(self):
        power = RecursivePower(RecursiveMultiplication())
        self.assertEqual(625, power.power(5, 4))
