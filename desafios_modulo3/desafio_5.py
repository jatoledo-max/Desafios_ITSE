class Cliente():

    def __init__(self, nombre, cantidad):
        self.__nombre = nombre
        self.__cantidad = cantidad

    def depositar(self, monto):
        if monto > 0:
            self.__cantidad += monto
            print(f"Deposito exitoso! Saldo actual: ${self.__cantidad}")
        else:
            print("Monto invalido")

    def extraer(self, monto):
        if monto > 0 and monto <= self.__cantidad:
            self.__cantidad -= monto
            print(f"Extraccion exitosa! Saldo actual: ${self.__cantidad}")
        elif monto > self.__cantidad:
            print("No se puede extraer esa cantidad")
        else:
            print("Monto invalido para extraccion")

    def get_total(self):
        return self.__cantidad


    def mostrar_datos(self):
        print(f"Titutar: {self.__nombre} - Saldo: ${self.__cantidad}")


class Banco():
    def __init__(self, cliente1, cliente2, cliente3):
        self.__cliente1 = cliente1
        self.__cliente2 = cliente2
        self.__cliente3 = cliente3

    def operar(self):
        print("\n--- Operaciones del dia ---")
        self.__cliente1.depositar(1500)
        self.__cliente2.depositar(2500)
        self.__cliente3.depositar(3500)

        self.__cliente1.extraer(150)
        self.__cliente2.extraer(250)
        self.__cliente3.extraer(350)

    def deposito_total(self):
        total = (self.__cliente1.get_total() + self.__cliente2.get_total() + self.__cliente3.get_total())
        print(f"\n >>> Total de dinero en el banco: ${total}")

if __name__ == "__main__":
    cliente1 = Cliente("Josefa", 0)
    cliente2 = Cliente("Luis", 0)
    cliente3 = Cliente("Carlos", 0)

    banco = Banco(cliente1, cliente2, cliente3)

    banco.operar()

    banco.deposito_total()

    print("\n --- Saldos individuales ---")
    cliente1.mostrar_datos()
    cliente2.mostrar_datos()
    cliente3.mostrar_datos()