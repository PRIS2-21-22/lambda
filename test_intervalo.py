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

if __name__ == '__main__':
    unittest.main()

#print(constantes.probemos + "ANTES")
#print(constantes.bien)
#prueba = intervalo(primer_interv_x=1, primer_interv_y=2, segundo_interv_x=4, segundo_interv_y=5)
#print(prueba)
#print(prueba.antes())
#print(constantes.mal)
#prueba2 = intervalo(primer_interv_x=4, primer_interv_y=6, segundo_interv_x=1, segundo_interv_y=3)
#print(prueba2)
#print(prueba2.antes())
#print("\n")