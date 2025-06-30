class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        

    def suma(self):
        suma = self.num1 + self.num2
        return suma
    
    def resta(self):
        resta = self.num1 - self.num2
        return resta
    
    def multi(self):
        multi = self.num1 * self.num2
        return multi

    def division(self):
        if self.num2 != 0: 
            division = self.num1 / self.num2
            return division
        else:
            return "No se puede dividir por 0"
        
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
        
prueba1 = Calculadora(num1, num2)

print(f"Suma: {prueba1.suma()}")
print(f"Resta: {prueba1.resta()}")
print(f"Multiplcado: {prueba1.multi()}")
print(f"Dividido: {prueba1.division()}")