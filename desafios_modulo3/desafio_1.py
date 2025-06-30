class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def aprobado_o_desaprobado(self):
        if self.nota < 6:
            print("Desaprobado")
        else:
            print("Aprobado")

alumno1 = Estudiante("Javier", 5)
alumno1.mostrar_datos()
alumno1.aprobado_o_desaprobado()