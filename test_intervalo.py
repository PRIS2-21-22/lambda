import unittest
import constantes
from intervalo import intervalo

class test_intervalo(unittest.TestCase):

    def test_antes_bien(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=2, segundo_interv_x=4, segundo_interv_y=5)
        self.assertTrue(prueba.antes(), "Debería ser True")

    def test_antes_mal(self):
        prueba = intervalo(primer_interv_x=4, primer_interv_y=6, segundo_interv_x=1, segundo_interv_y=3)
        self.assertFalse(prueba.antes(), "Debería ser False")
    
    def test_igual_bien(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=3, segundo_interv_x=1, segundo_interv_y=3)
        self.assertTrue(prueba.igual(), "Debería ser True")

    def test_igual_mal(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=3, segundo_interv_x=2, segundo_interv_y=3)
        self.assertFalse(prueba.igual(), "Debería ser False")

    def test_encuentra_bien(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=3, segundo_interv_x=3, segundo_interv_y=6)
        self.assertTrue(prueba.encuentra(), "Debería ser True")
    
    def test_encuentra_mal(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=3, segundo_interv_x=2, segundo_interv_y=6)
        self.assertFalse(prueba.encuentra(), "Debería ser False")

    def test_solapa_bien(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=3, segundo_interv_y=10)
        self.assertTrue(prueba.solapa(), "Debería ser True")
    
    def test_solapa_mal(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=6, segundo_interv_y=10)
        self.assertFalse(prueba.solapa(), "Debería ser False")

    def test_durante_bien(self):
        prueba = intervalo(primer_interv_x=4, primer_interv_y=8, segundo_interv_x=1, segundo_interv_y=10)
        self.assertTrue(prueba.durante(), "Debería ser True")
    
    def test_durante_mal(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=6, segundo_interv_y=10)
        self.assertFalse(prueba.durante(), "Debería ser False")

    def test_comienza_bien(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=1, segundo_interv_y=10)
        self.assertTrue(prueba.comienza(), "Debería ser True")

    def test_comienza_mal(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=3, segundo_interv_y=5)
        self.assertFalse(prueba.comienza(), "Debería ser False")

    def test_finaliza_bien(self):
        prueba = intervalo(primer_interv_x=4, primer_interv_y=10, segundo_interv_x=3, segundo_interv_y=10)
        self.assertTrue(prueba.finaliza(), "Debería ser True")
    
    def test_finaliza_mal(self):
        prueba = intervalo(primer_interv_x=6, primer_interv_y=9, segundo_interv_x=6, segundo_interv_y=10)
        self.assertFalse(prueba.finaliza(), "Debería ser False")
    

if __name__ == '__main__':
    unittest.main()

