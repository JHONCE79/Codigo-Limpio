import unittest

class TestImpuestos(unittest.TestCase):

    # Test Cases "Calcular total item" 

    # Regular Test Cases
    def test_CalcularTotalItemRegular1(self):
        precio_unitario = 100
        cantidad = 2
        impuestos_aplicados = 0.19  # 19% IVA
        self.assertEqual(calcular_total_item(precio_unitario, cantidad, impuestos_aplicados))

    def test_CalcularTotalItemRegular2(self):
        precio_unitario = 50
        cantidad = 5
        impuestos_aplicados = 0.05  # 5% IVA
        self.assertEqual(calcular_total_item(precio_unitario, cantidad, impuestos_aplicados))

    def test_CalcularTotalItemRegular3(self):
        precio_unitario = 150
        cantidad = 1
        impuestos_aplicados = 0
        self.assertEqual(calcular_total_item(precio_unitario, cantidad, impuestos_aplicados))

    # Extraordinary Test Cases
    def test_CalcularTotalItemExtraordinary1(self):
        precio_unitario = 10000000000
        cantidad = 10
        impuestos_aplicados = 0.19
        self.assertEqual(calcular_total_item(precio_unitario, cantidad, impuestos_aplicados))

    def test_CalcularTotalItemExtraordinary2(self):
        precio_unitario = 0.5
        cantidad = 100000000000
        impuestos_aplicados = 0.05
        self.assertEqual(calcular_total_item(precio_unitario, cantidad, impuestos_aplicados))

    def test_CalcularTotalItemExtraordinary3(self):
        precio_unitario = 100
        cantidad = 0
        impuestos_aplicados = 0.19
        self.assertEqual(calcular_total_item(precio_unitario, cantidad, impuestos_aplicados))

    # Error Test Cases
    def test_CalcularTotalItemError1(self):
        with self.assertRaises(TypeError):
            calcular_total_item("invalid", 2, 0.19)

    def test_CalcularTotalItemError2(self):
        with self.assertRaises(TypeError):
            calcular_total_item(100, "invalid", 0.19)

    def test_CalcularTotalItemError3(self):
        with self.assertRaises(TypeError):
            calcular_total_item(100, 2, "invalid")

    def test_CalcularTotalItemError4(self):
        with self.assertRaises(ValueError):
            calcular_total_item(100, 2, -0.19)  # Negative


    # Test Cases "Calcular total compra" 

    # Regular Test Cases
    def test_CalcularTotalCompraRegular1(self):
        items_comprados = [
            {"precio_unitario": 100, "cantidad": 2, "impuestos_aplicados": 0.19},
            {"precio_unitario": 50, "cantidad": 1, "impuestos_aplicados": 0.05}
        ]
        self.assertEqual(calcular_total_compra(items_comprados))

    def test_CalcularTotalCompraRegular2(self):
        items_comprados = [
            {"precio_unitario": 20, "cantidad": 3, "impuestos_aplicados": 0},
            {"precio_unitario": 100, "cantidad": 1, "impuestos_aplicados": 0.19}
        ]
        self.assertEqual(calcular_total_compra(items_comprados))

    def test_CalcularTotalCompraRegular3(self):
        items_comprados = [
            {"precio_unitario": 10, "cantidad": 10, "impuestos_aplicados": 0.19},
            {"precio_unitario": 5, "cantidad": 5, "impuestos_aplicados": 0.05}
        ]
        self.assertEqual(calcular_total_compra(items_comprados))

    # Extraordinary Test Cases
    def test_CalcularTotalCompraExtraordinary1(self):
        items_comprados = [
            {"precio_unitario": 1000000, "cantidad": 1, "impuestos_aplicados": 0.19},
            {"precio_unitario": 50000, "cantidad": 10, "impuestos_aplicados": 0.05}
        ]
        self.assertEqual(calcular_total_compra(items_comprados))

    def test_CalcularTotalCompraExtraordinary2(self):
        items_comprados = [
            {"precio_unitario": 0.5, "cantidad": 1000, "impuestos_aplicados": 0.19},
            {"precio_unitario": 10, "cantidad": 100, "impuestos_aplicados": 0.05}
        ]
        self.assertEqual(calcular_total_compra(items_comprados))

    def test_CalcularTotalCompraExtraordinary3(self):
        items_comprados = []  # Vacio
        self.assertEqual(calcular_total_compra(items_comprados))

    # Error Test Cases
    def test_CalcularTotalCompraError1(self):
        with self.assertRaises(TypeError):
            calcular_total_compra("invalid")

    def test_CalcularTotalCompraError2(self):
        with self.assertRaises(TypeError):
            items_comprados = [
                {"precio_unitario": 100, "cantidad": 2, "impuestos_aplicados": 0.19},
                {"precio_unitario": 50, "cantidad": 1, "impuestos_aplicados": "invalid"}
            ]
            calcular_total_compra(items_comprados)

    def test_CalcularTotalCompraError3(self):
        with self.assertRaises(TypeError):
            items_comprados = [
                {"precio_unitario": 100, "cantidad": 2, "impuestos_aplicados": 0.19},
                "invalid"
            ]
            calcular_total_compra(items_comprados)

    def test_CalcularTotalCompraError4(self):
        with self.assertRaises(ValueError):
            items_comprados = [
                {"precio_unitario": 100, "cantidad": 2, "impuestos_aplicados": -0.19}
            ]
            calcular_total_compra(items_comprados)

if __name__ == '__main__':
    unittest.main()