class intervalo:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def antes(self):       
        if (self.x < self.y): 
            return True
        return False

    def __str__(self):
        return "x: {}, y: {}".format(self.x, self.y)

print("Probemos con un x < y")
prueba = intervalo(x=1, y=2)
print(prueba)
print(prueba.antes())
print("Probemos con un y < x")
prueba2 = intervalo(x=4, y=2)
print(prueba2)
print(prueba2.antes())

#Probando para que funcione sonar

#print("Hello world 2")