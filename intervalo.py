import constantes

class intervalo:
    
    def __init__(self,primer_interv_x,primer_interv_y,segundo_interv_x,segundo_interv_y):
        """Metodo constructor con el que creamos dos intervalo dando el principio y fin de cada uno"""       
        self.primer_x = primer_interv_x
        self.primer_y = primer_interv_y

        self.segundo_x = segundo_interv_x
        self.segundo_y = segundo_interv_y

    def antes(self):
        """Funcion que comprueba si el primer intervalo termina antes de empezar el segundo"""       
        if (self.primer_y < self.segundo_x): 
            return True
        return False

    def __str__(self):
        """Metodo magico que nos imprime los valores iniciales y finales de nuestros intervalos"""
        return "Intervalo 1 => x: {}, y: {}; Intervalo 2 => x: {}, y: {}".format(self.primer_x, self.primer_y, self.segundo_x, self.segundo_y)

    def igual(self):
        """Funcion que comprueba si el primer intervalo y el segundo son iguales"""
        if(self.primer_x == self.segundo_x and self.primer_y == self.segundo_y):
            return True
        return False
    
    def encuentra(self):
        """Funcion que comprueba si el segundo intervalo empieza justo al final del primero"""
        if(self.primer_y == self.segundo_x):
            return True
        return False
    
    def solapa(self):
        """Funcion que comprueba si el final del primer intervalo sobrepasa al principio del segundo"""
        if(self.primer_y > self.segundo_x):
            return True
        return False
    
    def durante(self):
        """Funcion que comprueba si el primer intervalo ocurre dentro del segundo intervalo"""
        if(self.primer_x > self.segundo_x and self.primer_y < self.segundo_y):
            return True
        return False

    def comienza(self):
        """Funcion que comprueba si el primer intervalo coincide con el comienzo del segundo"""
        if(self.primer_x == self.segundo_x and self.primer_y < self.segundo_y):
            return True
        return False
    
    def finaliza(self):
        """Funcion que comprueba si el primer intervalo coincide con el final del segundo"""
        if(self.primer_x > self.segundo_x and self.primer_y == self.segundo_y):
            return True
        return False



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

#print(constantes.probemos + "IGUAL")
#print(constantes.bien)
#prueba = intervalo(primer_interv_x=1, primer_interv_y=3, segundo_interv_x=1, segundo_interv_y=3)
#print(prueba)
#print(prueba.igual())
#print(constantes.mal)
#prueba2 = intervalo(primer_interv_x=1, primer_interv_y=3, segundo_interv_x=2, segundo_interv_y=3)
#print(prueba2)
#print(prueba2.igual())
#print("\n")

#print(constantes.probemos + "ENCUENTRA")
#print(constantes.bien)
#prueba = intervalo(primer_interv_x=1, primer_interv_y=3, segundo_interv_x=3, segundo_interv_y=6)
#print(prueba)
#print(prueba.encuentra())
#print(constantes.mal)
#prueba2 = intervalo(primer_interv_x=1, primer_interv_y=3, segundo_interv_x=2, segundo_interv_y=6)
#print(prueba2)
#print(prueba2.encuentra())
#print("\n")

#print(constantes.probemos + "SOLAPA")
#print(constantes.bien)
#prueba = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=3, segundo_interv_y=10)
#print(prueba)
#print(prueba.solapa())
#print(constantes.mal)
#prueba2 = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=6, segundo_interv_y=10)
#print(prueba2)
#print(prueba2.solapa())
#print("\n")

#print(constantes.probemos + "DURANTE")
#print(constantes.bien)
#prueba = intervalo(primer_interv_x=4, primer_interv_y=8, segundo_interv_x=1, segundo_interv_y=10)
#print(prueba)
#print(prueba.durante())
#print(constantes.mal)
#prueba2 = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=6, segundo_interv_y=10)
#print(prueba2)
#print(prueba2.durante())
#print("\n")

#print(constantes.probemos + "COMIENZA")
#print(constantes.bien)
#prueba = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=1, segundo_interv_y=10)
#print(prueba)
#print(prueba.comienza())
#print(constantes.mal)
#prueba2 = intervalo(primer_interv_x=1, primer_interv_y=5, segundo_interv_x=3, segundo_interv_y=5)
#print(prueba2)
#print(prueba2.comienza())
#print("\n")

#print(constantes.probemos + "FINALIZA")
#print(constantes.bien)
#prueba = intervalo(primer_interv_x=4, primer_interv_y=10, segundo_interv_x=3, segundo_interv_y=10)
#print(prueba)
#print(prueba.finaliza())
#print(constantes.mal)
#prueba2 = intervalo(primer_interv_x=6, primer_interv_y=9, segundo_interv_x=6, segundo_interv_y=10)
#print(prueba2)
#print(prueba2.finaliza())
#print("\n")



#Probando para que funcione sonar

#print("Hello world 2")