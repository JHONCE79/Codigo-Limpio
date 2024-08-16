import unittest
from datetime import datetime

class TestLiquidacion(unittest.TestCase):

    # Test Cases "Calcular total item" 

    # Regular Test Cases
    def testCalcularTotalItemRegular1(self):
        precio_unitario = 100
        cantidad = 2
        impuestos_aplicados = 0.19  # 19% IVA
        self.assertEqual(calcular_total_item(precio_unitario, cantidad, impuestos_aplicados))

    def testCalcularTotalItemRegular2(self):
        precio_unitario = 50
        cantidad = 5
        impuestos_aplicados = 0.05  # 5% IVA
        self.assertEqual(calcular_total_item(precio_unitario, cantidad, impuestos_aplicados))

    def testCalcularTotalItemRegular3(self):
        precio_unitario = 150
        cantidad = 1
        impuestos_aplicados = 0
        self.assertEqual(calcular_total_item(precio_unitario, cantidad, impuestos_aplicados))

    # Extraordinary Test Cases
    def testCalcularTotalItemExtraordinary1(self):
        precio_unitario = 1000000
        cantidad = 10
        impuestos_aplicados = 0.19
        self.assertEqual(calcular_total_item(precio_unitario, cantidad, impuestos_aplicados))

    def testCalcularTotalItemExtraordinary2(self):
        precio_unitario = 0.5
        cantidad = 1000
        impuestos_aplicados = 0.05
        self.assertEqual(calcular_total_item(precio_unitario, cantidad, impuestos_aplicados))

    def testCalcularTotalItemExtraordinary3(self):
        precio_unitario = 100
        cantidad = 0
        impuestos_aplicados = 0.19
        self.assertEqual(calcular_total_item(precio_unitario, cantidad, impuestos_aplicados))

    # Error Test Cases
    def testCalcularTotalItemError1(self):
        with self.assertRaises(TypeError):
            calcular_total_item("invalid", 2, 0.19)

    def testCalcularTotalItemError2(self):
        with self.assertRaises(TypeError):
            calcular_total_item(100, "invalid", 0.19)

    def testCalcularTotalItemError3(self):
        with self.assertRaises(TypeError):
            calcular_total_item(100, 2, "invalid")

    def testCalcularTotalItemError4(self):
        with self.assertRaises(ValueError):
            calcular_total_item(100, 2, -0.19)  # Negative tax rate


    # Test Cases "Calcular total compra" 

    # Regular Test Cases
    def testCalcularTotalCompraRegular1(self):
        items_comprados = [
            {"precio_unitario": 100, "cantidad": 2, "impuestos_aplicados": 0.19},
            {"precio_unitario": 50, "cantidad": 1, "impuestos_aplicados": 0.05}
        ]
        self.assertEqual(calcular_total_compra(items_comprados))

    def testCalcularTotalCompraRegular2(self):
        items_comprados = [
            {"precio_unitario": 20, "cantidad": 3, "impuestos_aplicados": 0},
            {"precio_unitario": 100, "cantidad": 1, "impuestos_aplicados": 0.19}
        ]
        self.assertEqual(calcular_total_compra(items_comprados))

    def testCalcularTotalCompraRegular3(self):
        items_comprados = [
            {"precio_unitario": 10, "cantidad": 10, "impuestos_aplicados": 0.19},
            {"precio_unitario": 5, "cantidad": 5, "impuestos_aplicados": 0.05}
        ]
        self.assertEqual(calcular_total_compra(items_comprados))

    # Extraordinary Test Cases
    def testCalcularTotalCompraExtraordinary1(self):
        items_comprados = [
            {"precio_unitario": 1000000, "cantidad": 1, "impuestos_aplicados": 0.19},
            {"precio_unitario": 50000, "cantidad": 10, "impuestos_aplicados": 0.05}
        ]
        self.assertEqual(calcular_total_compra(items_comprados))

    def testCalcularTotalCompraExtraordinary2(self):
        items_comprados = [
            {"precio_unitario": 0.5, "cantidad": 1000, "impuestos_aplicados": 0.19},
            {"precio_unitario": 10, "cantidad": 100, "impuestos_aplicados": 0.05}
        ]
        self.assertEqual(calcular_total_compra(items_comprados))

    def testCalcularTotalCompraExtraordinary3(self):
        items_comprados = []  # Empty shopping cart
        self.assertEqual(calcular_total_compra(items_comprados))

    # Error Test Cases
    def testCalcularTotalCompraError1(self):
        with self.assertRaises(TypeError):
            calcular_total_compra("invalid")

    def testCalcularTotalCompraError2(self):
        with self.assertRaises(TypeError):
            items_comprados = [
                {"precio_unitario": 100, "cantidad": 2, "impuestos_aplicados": 0.19},
                {"precio_unitario": 50, "cantidad": 1, "impuestos_aplicados": "invalid"}
            ]
            calcular_total_compra(items_comprados)

    def testCalcularTotalCompraError3(self):
        with self.assertRaises(TypeError):
            items_comprados = [
                {"precio_unitario": 100, "cantidad": 2, "impuestos_aplicados": 0.19},
                "invalid"
            ]
            calcular_total_compra(items_comprados)

    def testCalcularTotalCompraError4(self):
        with self.assertRaises(ValueError):
            items_comprados = [
                {"precio_unitario": 100, "cantidad": 2, "impuestos_aplicados": -0.19}
            ]
            calcular_total_compra(items_comprados)


# Ejecutar la prueba individualmente
"""""
if __name__ == '__main__':
    unittest.main()
"""""