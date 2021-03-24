import constantes

class intervalo:
    
    def __init__(self,x,y,i,j):
        self.x = x
        self.y = y

        self.i = i
        self.j = j

    def antes(self):       
        if (self.y < self.i): 
            return True
        return False

    def __str__(self):
        return "Intervalo 1 => x: {}, y: {}; Intervalo 2 => i: {}, j: {}".format(self.x, self.y, self.i, self.j)

    def igual(self):
        if(self.x == self.i and self.y == self.j):
            return True
        return False
    
    def encuentra(self):
        if(self.y == self.i):
            return True
        return False
    
    def solapa(self):
        if(self.y > self.i):
            return True
        return False
    
    def durante(self):
        if(self.x > self.i and self.y < self.j):
            return True
        return False

    def comienza(self):
        if(self.x == self.i and self.y < self.j):
            return True
        return False
    
    def finaliza(self):
        if(self.x > self.i and self.y == self.j):
            return True
        return False



print(constantes.probemos + "ANTES")
print(constantes.bien)
prueba = intervalo(x=1, y=2, i=4, j=5)
print(prueba)
print(prueba.antes())
print(constantes.mal)
prueba2 = intervalo(x=4, y=6, i=1, j=3)
print(prueba2)
print(prueba2.antes())
print("\n")

print(constantes.probemos + "IGUAL")
print(constantes.bien)
prueba = intervalo(x=1, y=3, i=1, j=3)
print(prueba)
print(prueba.igual())
print(constantes.mal)
prueba2 = intervalo(x=1, y=3, i=2, j=3)
print(prueba2)
print(prueba2.igual())
print("\n")

print(constantes.probemos + "ENCUENTRA")
print(constantes.bien)
prueba = intervalo(x=1, y=3, i=3, j=6)
print(prueba)
print(prueba.encuentra())
print(constantes.mal)
prueba2 = intervalo(x=1, y=3, i=2, j=6)
print(prueba2)
print(prueba2.encuentra())
print("\n")

print(constantes.probemos + "SOLAPA")
print(constantes.bien)
prueba = intervalo(x=1, y=5, i=3, j=10)
print(prueba)
print(prueba.solapa())
print(constantes.mal)
prueba2 = intervalo(x=1, y=5, i=6, j=10)
print(prueba2)
print(prueba2.solapa())
print("\n")

print(constantes.probemos + "DURANTE")
print(constantes.bien)
prueba = intervalo(x=4, y=8, i=1, j=10)
print(prueba)
print(prueba.durante())
print(constantes.mal)
prueba2 = intervalo(x=1, y=5, i=6, j=10)
print(prueba2)
print(prueba2.durante())
print("\n")

print(constantes.probemos + "COMIENZA")
print(constantes.bien)
prueba = intervalo(x=1, y=5, i=1, j=10)
print(prueba)
print(prueba.comienza())
print(constantes.mal)
prueba2 = intervalo(x=1, y=5, i=3, j=5)
print(prueba2)
print(prueba2.comienza())
print("\n")

print(constantes.probemos + "FINALIZA")
print(constantes.bien)
prueba = intervalo(x=4, y=10, i=3, j=10)
print(prueba)
print(prueba.solapa())
print(constantes.mal)
prueba2 = intervalo(x=6, y=9, i=6, j=10)
print(prueba2)
print(prueba2.solapa())
print("\n")



#Probando para que funcione sonar

#print("Hello world 2")