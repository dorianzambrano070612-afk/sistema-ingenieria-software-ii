import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from calculadora import sumar, restar, multiplicar, dividir


class TestFuncionales(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 3), 12)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)


class TestValidacion(unittest.TestCase):
    def test_dividir_entre_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_negativos(self):
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_decimales(self):
        self.assertAlmostEqual(sumar(0.1, 0.2), 0.3)


if __name__ == "__main__":
    unittest.main()