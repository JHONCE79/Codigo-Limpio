import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from logic.logica import calcular_total_item, calcular_total_compra

import unittest
from logic.logica import calcular_total_item

class TestCalcularTotalItem(unittest.TestCase):
    
    # Casos normales
    def test_item_vehiculo_mayor_200cc(self):
        # Vehículo con cilindraje mayor a 200cc, impuesto del 8%
        total_impuestos, total_item = calcular_total_item(50000000, 1, 8)
        self.assertAlmostEqual(total_impuestos, 4000000)
        self.assertAlmostEqual(total_item, 54000000)
    
    def test_item_licor_menor_35_grados(self):
        # Licor con grado de alcohol menor al 35%, impuesto del 25%
        total_impuestos, total_item = calcular_total_item(100000, 2, 25)
        self.assertAlmostEqual(total_impuestos, 50000)
        self.assertAlmostEqual(total_item, 250000)

    def test_item_vino_bajo_alcohol(self):
    # Vino con grado de alcohol inferior al 14%, impuesto del 20%
        total_impuestos, total_item = calcular_total_item(30000, 5, 20)
        self.assertAlmostEqual(total_impuestos, 30000)
        self.assertAlmostEqual(total_item, 180000)


    # Casos excepcionales
    def test_item_licor_alto_con_alcohol(self):
        # Licor con grado de alcohol superior al 35%, impuesto del 40%
        total_impuestos, total_item = calcular_total_item(150000, 1, 40)
        self.assertAlmostEqual(total_impuestos, 60000)
        self.assertAlmostEqual(total_item, 210000)
    
    def test_item_bolsas_plasticas(self):
        # 10 bolsas plásticas, impuesto fijo de 66 COP por bolsa
        total_impuestos, total_item = calcular_total_item(0, 10, 'fijo')
        self.assertAlmostEqual(total_impuestos, 660)
        self.assertAlmostEqual(total_item, 660)

    def test_item_exento(self):
        # Artículo exento de impuestos
        total_impuestos, total_item = calcular_total_item(20000, 3, 'exento')
        self.assertAlmostEqual(total_impuestos, 0)
        self.assertAlmostEqual(total_item, 60000)

    # Casos de error
    def test_item_precio_negativo(self):
        with self.assertRaises(ValueError):
            calcular_total_item(-10000, 1, 19)
    
    def test_item_impuesto_negativo(self):
        with self.assertRaises(ValueError):
            calcular_total_item(10000, 1, -19)
    
    def test_item_precio_cero(self):
        with self.assertRaises(ValueError):
            calcular_total_item(0, 1, 19)
    
    def test_item_tipo_impuesto_invalido(self):
        with self.assertRaises(TypeError):
            calcular_total_item(10000, 1, "invalido")

    # Pruebas para calcular_total_compra

class TestCalcularTotalCompra(unittest.TestCase):
    
    # Casos normales
    def test_compra_multiples_items(self):
        items = [(50000, 2, 19), (150000, 1, 40), (30000, 3, 20)]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertAlmostEqual(total_impuestos, 99500)
        self.assertAlmostEqual(total_compra, 495500)
    
    def test_compra_bolsas_plasticas(self):
        items = [(10000, 1, 19), (0, 10, 'fijo')]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertAlmostEqual(total_impuestos, 2560)
        self.assertAlmostEqual(total_compra, 12560)

    def test_compra_exentos_y_gravados(self):
        items = [(100000, 1, 'exento'), (20000, 5, 5)]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertAlmostEqual(total_impuestos, 5000)
        self.assertAlmostEqual(total_compra, 200000)
    
    # Casos excepcionales
    def test_compra_solo_exentos(self):
        items = [(100000, 1, 'exento'), (50000, 2, 'exento')]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertAlmostEqual(total_impuestos, 0)
        self.assertAlmostEqual(total_compra, 200000)
    
    def test_compra_alta_cantidad_items(self):
        items = [(1000, 1000, 19), (500, 2000, 19)]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertAlmostEqual(total_impuestos, 85500)
        self.assertAlmostEqual(total_compra, 535500)
    
    def test_compra_multiples_impuestos(self):
        items = [(100000, 1, 19), (50000, 1, 25), (20000, 2, 5)]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertAlmostEqual(total_impuestos, 40500)
        self.assertAlmostEqual(total_compra, 230000)
    
    # Casos de error
    def test_compra_precio_negativo(self):
        items = [(-10000, 1, 19), (150000, 1, 40)]
        with self.assertRaises(ValueError):
            calcular_total_compra(items)
    
    def test_compra_cantidad_negativa(self):
        items = [(10000, -1, 19), (150000, 1, 40)]
        with self.assertRaises(ValueError):
            calcular_total_compra(items)
    
    def test_compra_tipo_impuesto_invalido(self):
        items = [(10000, 1, "invalido"), (150000, 1, 40)]
        with self.assertRaises(TypeError):
            calcular_total_compra(items)
    
    def test_compra_items_vacios(self):
        items = []
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertEqual(total_impuestos, 0)
        self.assertEqual(total_compra, 0)


if __name__ == '__main__':
    unittest.main()
