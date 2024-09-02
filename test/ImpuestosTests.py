
import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from logic.logica import calcular_total_item , calcular_total_compra


class TestCalcularTotal(unittest.TestCase):


    def test_calcular_total_item_iva_19(self):
        total_impuestos, total_item = calcular_total_item(100, 2, 19)
        self.assertEqual(total_impuestos, 38)
        self.assertEqual(total_item, 238)
    
    def test_calcular_total_item_iva_5(self):
        total_impuestos, total_item = calcular_total_item(50, 3, 5)
        self.assertEqual(total_impuestos, 7.5)
        self.assertEqual(total_item, 157.5)
    
    def test_calcular_total_item_exento(self):
        total_impuestos, total_item = calcular_total_item(200, 1, "exento")
        self.assertEqual(total_impuestos, 0)
        self.assertEqual(total_item, 200)

    def test_calcular_total_item_inc_8(self):
        total_impuestos, total_item = calcular_total_item(100, 1, 8)
        self.assertEqual(total_impuestos, 8)
        self.assertEqual(total_item, 108)

    def test_calcular_total_item_precio_alto_iva_19(self):
        total_impuestos, total_item = calcular_total_item(1000, 10, 19)
        self.assertEqual(total_impuestos, 1900)
        self.assertEqual(total_item, 11900)

    def test_calcular_total_item_cantidad_alta_iva_5(self):
        total_impuestos, total_item = calcular_total_item(1, 10000, 5)
        self.assertEqual(total_impuestos, 500)
        self.assertEqual(total_item, 10500)

    def test_calcular_total_item_excluido(self):
        total_impuestos, total_item = calcular_total_item(150, 4, "excluido")
        self.assertEqual(total_impuestos, 0)
        self.assertEqual(total_item, 600)
    
    def test_calcular_total_item_error_precio_negativo(self):
        with self.assertRaises(ValueError):
            calcular_total_item(-100, 1, 19)
    
    def test_calcular_total_item_error_cantidad_negativa(self):
        with self.assertRaises(ValueError):
            calcular_total_item(100, -1, 19)
    
    def test_calcular_total_item_error_impuesto_tipo_incorrecto(self):
        with self.assertRaises(TypeError):
            calcular_total_item(100, 1, "diecinueve")
    
    # Pruebas para la función "Calcular total compra"
    
    def test_calcular_total_compra_iva_19_exento(self):
        items = [
            (100, 2, 19),  # IVA 19%
            (200, 1, "exento") # Exento
        ]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertEqual(total_impuestos, 38)
        self.assertEqual(total_compra, 438)
    
    def test_calcular_total_compra_iva_5_excluido(self):
        items = [
            (50, 3, 5),    # IVA 5%
            (150, 2, "excluido") # Excluido
        ]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertEqual(total_impuestos, 7.5)
        self.assertEqual(total_compra, 457.5)
    
    def test_calcular_total_compra_iva_19_exento(self):
        items = [
            (100, 1, 19),  # IVA 19%
            (200, 1, "exento") # Exento
        ]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertEqual(total_impuestos, 19)
        self.assertEqual(total_compra, 319)
    
    def test_calcular_total_compra_inc_8(self):
        items = [
            (100, 1, 8),   # INC 8%
            (150, 2, "exento") # Exento
        ]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertEqual(total_impuestos, 8)
        self.assertEqual(total_compra, 408)
    
    def test_calcular_total_compra_precio_alto_iva_19(self):
        items = [
            (5000, 2, 19), # IVA 19%
            (10000, 1, "exento") # Exento
        ]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertEqual(total_impuestos, 1900)
        self.assertEqual(total_compra, 21900)
    
    def test_calcular_total_compra_cantidad_alta_iva_5(self):
        items = [
            (1, 10000, 5),    # IVA 5%
            (2, 5000, 5) # IVA 5%
        ]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertEqual(total_impuestos, 150)
        self.assertEqual(total_compra, 16500)
    
    def test_calcular_total_compra_solo_exento(self):
        items = [
            (200, 3, "exento"),
            (150, 2, "exento")
        ]
        total_impuestos, total_compra = calcular_total_compra(items)
        self.assertEqual(total_impuestos, 0)
        self.assertEqual(total_compra, 900)
    
    def test_calcular_total_compra_error_precio_negativo(self):
        items = [
            (-100, 2, 19)
        ]
        with self.assertRaises(ValueError):
            calcular_total_compra(items)
    
    def test_calcular_total_compra_error_cantidad_negativa(self):
        items = [
            (100, -2, 19)
        ]
        with self.assertRaises(ValueError):
            calcular_total_compra(items)
    
    def test_calcular_total_compra_error_impuesto_tipo_incorrecto(self):
        items = [
            (100, 1, "diecinueve")
        ]
        with self.assertRaises(TypeError):
            calcular_total_compra(items)

if __name__ == '__main__':
    unittest.main()
