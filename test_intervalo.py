import unittest
import constantes
from intervalo import intervalo

class test_intervalo(unittest.TestCase):

    def test_antes_bien(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=2, segundo_interv_x=4, segundo_interv_y=5)
        self.assertTrue(prueba.antes(), constantes.bien)

    def test_antes_mal(self):
        prueba = intervalo(primer_interv_x=4, primer_interv_y=6, segundo_interv_x=1, segundo_interv_y=3)
        self.assertFalse(prueba.antes(), constantes.mal)

    def test_igual_bien(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=3, segundo_interv_x=1, segundo_interv_y=3)
        self.assertTrue(prueba.igual(), constantes.bien)

    def test_igual_mal(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=3, segundo_interv_x=2, segundo_interv_y=3)
        self.assertFalse(prueba.igual(), constantes.mal)

    def test_encuentra_bien(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=3, segundo_interv_x=3, segundo_interv_y=6)
        self.assertTrue(prueba.encuentra(), constantes.bien)

    def test_encuentra_mal(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=3, segundo_interv_x=2, segundo_interv_y=6)
        self.assertFalse(prueba.encuentra(), constantes.mal)

    def test_solapa_bien(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=3, segundo_interv_y=10)
        self.assertTrue(prueba.solapa(), constantes.bien)

    def test_solapa_mal(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=6, segundo_interv_y=10)
        self.assertFalse(prueba.solapa(), constantes.mal)

    def test_durante_bien(self):
        prueba = intervalo(primer_interv_x=4, primer_interv_y=8, segundo_interv_x=1, segundo_interv_y=10)
        self.assertTrue(prueba.durante(), constantes.bien)

    def test_durante_mal(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=6, segundo_interv_y=10)
        self.assertFalse(prueba.durante(), constantes.mal)

    def test_comienza_bien(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=1, segundo_interv_y=10)
        self.assertTrue(prueba.comienza(), constantes.bien)

    def test_comienza_mal(self):
        prueba = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=3, segundo_interv_y=5)
        self.assertFalse(prueba.comienza(), constantes.mal)

    def test_finaliza_bien(self):
        prueba = intervalo(primer_interv_x=4, primer_interv_y=10, segundo_interv_x=3, segundo_interv_y=10)
        self.assertTrue(prueba.finaliza(), constantes.bien)

    def test_finaliza_mal(self):
        prueba = intervalo(primer_interv_x=6, primer_interv_y=9, segundo_interv_x=6, segundo_interv_y=10)
        self.assertFalse(prueba.finaliza(), constantes.mal)


if __name__ == '__main__':
    unittest.main()