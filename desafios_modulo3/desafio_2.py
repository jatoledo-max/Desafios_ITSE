class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def es_triangulo(self):
        if self.lado1 + self.lado2 > self.lado3 and self.lado1 + self.lado3 > self.lado2 and self.lado2 + self.lado3 > self.lado1:
            return " "
        else:
            return "No es triangulo valido"
        

    def lado_mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            return "Lado 1 es el mayor"
        else:
            if self.lado2 > self.lado1 and self.lado2 > self.lado3:
                return "Lado 2 es el mayor"
            else:
                return "Lado 3 es el mayor"


    def tipo_de_triangulo(self):
            if self.lado1 == self.lado2 == self.lado3:
                return "Equilatero"
            elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                return "Isosceles"
            else:
                return "Escaleno"
    
triangulo1 = Triangulo(50,50,50)
triangulo2 = Triangulo(50,50,20)
triangulo3 = Triangulo(30,25,10)
print(triangulo1.es_triangulo())
print(triangulo1.lado_mayor())
print(triangulo2.lado_mayor())
print(triangulo3.lado_mayor())
print(triangulo1.tipo_de_triangulo())
print(triangulo2.tipo_de_triangulo())
print(triangulo3.tipo_de_triangulo())