import unittest
from datetime import datetime
import modulo_liquidacion # Asumimos que tenemos modulo 

class TestLiquidacion(unittest.TestCase):

    # Test Cases "Calcular total item" 

    # Regular Test Cases
    def test_calcular_total_item_regular_1(self):
        precio_unitario = 100
        cantidad = 2
        impuestos_aplicados = 0.19  # 19% IVA
        self.assertEqual(modulo_liquidacion.calcular_total_item(precio_unitario, cantidad, impuestos_aplicados), 238)

    def test_calcular_total_item_regular_2(self):
        precio_unitario = 50
        cantidad = 5
        impuestos_aplicados = 0.05  # 5% IVA
        self.assertEqual(modulo_liquidacion.calcular_total_item(precio_unitario, cantidad, impuestos_aplicados), 262.5)

    def test_calcular_total_item_regular_3(self):
        precio_unitario = 150
        cantidad = 1
        impuestos_aplicados = 0
        self.assertEqual(modulo_liquidacion.calcular_total_item(precio_unitario, cantidad, impuestos_aplicados), 150)

    # Extraordinary Test Cases
    def test_calcular_total_item_extraordinary_1(self):
        precio_unitario = 1000000
        cantidad = 10
        impuestos_aplicados = 0.19
        self.assertEqual(modulo_liquidacion.calcular_total_item(precio_unitario, cantidad, impuestos_aplicados), 11900000)

    def test_calcular_total_item_extraordinary_2(self):
        precio_unitario = 0.5
        cantidad = 1000
        impuestos_aplicados = 0.05
        self.assertEqual(modulo_liquidacion.calcular_total_item(precio_unitario, cantidad, impuestos_aplicados), 525)

    def test_calcular_total_item_extraordinary_3(self):
        precio_unitario = 100
        cantidad = 0
        impuestos_aplicados = 0.19
        self.assertEqual(modulo_liquidacion.calcular_total_item(precio_unitario, cantidad, impuestos_aplicados), 0)

    # Error Test Cases
    def test_calcular_total_item_error_1(self):
        with self.assertRaises(TypeError):
            modulo_liquidacion.calcular_total_item("invalid", 2, 0.19)

    def test_calcular_total_item_error_2(self):
        with self.assertRaises(TypeError):
            modulo_liquidacion.calcular_total_item(100, "invalid", 0.19)

    def test_calcular_total_item_error_3(self):
        with self.assertRaises(TypeError):
            modulo_liquidacion.calcular_total_item(100, 2, "invalid")

    def test_calcular_total_item_error_4(self):
        with self.assertRaises(ValueError):
            modulo_liquidacion.calcular_total_item(100, 2, -0.19)  # Negative tax rate


    # Test Cases "Calcular total compra" 

    # Regular Test Cases
    def test_calcular_total_compra_regular_1(self):
        items_comprados = [
            {"precio_unitario": 100, "cantidad": 2, "impuestos_aplicados": 0.19},
            {"precio_unitario": 50, "cantidad": 1, "impuestos_aplicados": 0.05}
        ]
        self.assertEqual(modulo_liquidacion.calcular_total_compra(items_comprados), 286.25)

    def test_calcular_total_compra_regular_2(self):
        items_comprados = [
            {"precio_unitario": 20, "cantidad": 3, "impuestos_aplicados": 0},
            {"precio_unitario": 100, "cantidad": 1, "impuestos_aplicados": 0.19}
        ]
        self.assertEqual(modulo_liquidacion.calcular_total_compra(items_comprados), 119)

    def test_calcular_total_compra_regular_3(self):
        items_comprados = [
            {"precio_unitario": 10, "cantidad": 10, "impuestos_aplicados": 0.19},
            {"precio_unitario": 5, "cantidad": 5, "impuestos_aplicados": 0.05}
        ]
        self.assertEqual(modulo_liquidacion.calcular_total_compra(items_comprados), 134.25)

    # Extraordinary Test Cases
    def test_calcular_total_compra_extraordinary_1(self):
        items_comprados = [
            {"precio_unitario": 1000000, "cantidad": 1, "impuestos_aplicados": 0.19},
            {"precio_unitario": 50000, "cantidad": 10, "impuestos_aplicados": 0.05}
        ]
        self.assertEqual(modulo_liquidacion.calcular_total_compra(items_comprados), 1595000)

    def test_calcular_total_compra_extraordinary_2(self):
        items_comprados = [
            {"precio_unitario": 0.5, "cantidad": 1000, "impuestos_aplicados": 0.19},
            {"precio_unitario": 10, "cantidad": 100, "impuestos_aplicados": 0.05}
        ]
        self.assertEqual(modulo_liquidacion.calcular_total_compra(items_comprados), 695)

    def test_calcular_total_compra_extraordinary_3(self):
        items_comprados = []  # Empty shopping cart
        self.assertEqual(modulo_liquidacion.calcular_total_compra(items_comprados), 0)

    # Error Test Cases
    def test_calcular_total_compra_error_1(self):
        with self.assertRaises(TypeError):
            modulo_liquidacion.calcular_total_compra("invalid")

    def test_calcular_total_compra_error_2(self):
        with self.assertRaises(TypeError):
            items_comprados = [
                {"precio_unitario": 100, "cantidad": 2, "impuestos_aplicados": 0.19},
                {"precio_unitario": 50, "cantidad": 1, "impuestos_aplicados": "invalid"}
            ]
            modulo_liquidacion.calcular_total_compra(items_comprados)

    def test_calcular_total_compra_error_3(self):
        with self.assertRaises(TypeError):
            items_comprados = [
                {"precio_unitario": 100, "cantidad": 2, "impuestos_aplicados": 0.19},
                "invalid"
            ]
            modulo_liquidacion.calcular_total_compra(items_comprados)

    def test_calcular_total_compra_error_4(self):
        with self.assertRaises(ValueError):
            items_comprados = [
                {"precio_unitario": 100, "cantidad": 2, "impuestos_aplicados": -0.19}
            ]
            modulo_liquidacion.calcular_total_compra(items_comprados)

if __name__ == '__main__':
    unittest.main()