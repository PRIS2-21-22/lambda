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