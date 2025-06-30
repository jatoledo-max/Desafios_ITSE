class Contacto():
    def __init__(self, nombre, telefono, email):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_telefono(self):
        return self.__telefono
    
    def set_telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono
    
    def get_email(self):
        return self.__email
    
    def set_email(self, nuevo_email):
        self.__email = nuevo_email

    def mostrar_contacto(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Telefono: {self.__telefono}")
        print(f"e-mail: {self.__email}")


c1 = Contacto("Javier", "3855702807", "javier.toledo1713@gmail.com")

# Modificado CON decoradores
print(c1.nombre)
c1.nombre = "Carlos"
print(c1.nombre)

# Modificado SIN decoradores
print(c1.get_telefono())
c1.set_telefono("3855000222")
print(c1.get_telefono())

class Agenda:
    def __init__(self):
        self.contactos = []

    def crear_contacto(self, nombre, telefono, email):
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto {nombre} creado!")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None
    
    def borrar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            print(f"Contacto {nombre} borrado!")
        else:
            print("Contacto no existente!")

    def editar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            print("Pone espacio y 'enter' si no quieres modificar un dato.")
            nuevo_telefono = input("Ingresa el nuevo telefono: ")
            nuevo_email = input("Ingresa el nuevo email: ")
            if nuevo_telefono:
                contacto.telefono = nuevo_telefono
            if nuevo_email:
                contacto.email = nuevo_email
            print("Datos actualizados!")
        else:
            print("Contacto no encontrado")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda esta vacia!. ")
        else:
            for contacto in self.contactos:
                print("------------")
                contacto.mostrar_contacto()

    def menu(self):
        while True:
            print("\n --- AGENDA ---")
            print("1. Crear contacto")
            print("2. Borrar contacto")
            print("3. Editar contacto")
            print("4. Ver lista de contactos")
            print("5. Buscar contacto")
            print("6. SALIR")

            opcion = input("Elija una opcion: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                telefono = input("Telefono: ")
                email = input("Email: ")
                self.crear_contacto(nombre, telefono, email)
            elif opcion == "2":
                nombre = input("Nombre del contacto a eliminar: ")
                self.borrar_contacto(nombre)
            elif opcion == "3":
                nombre = input("Nombre del contacto a editar: ")
                self.editar_contacto(nombre)
            elif opcion == "4":
                self.listar_contactos()
            elif opcion == "5":
                nombre = input("Nombre a buscar: ")
                contacto = self.buscar_contacto(nombre)
                if contacto:
                    contacto.mostrar_contaco()
                else:
                    print("Contacto no existente!")
            elif opcion == "6":
                print("Agenda cerrada!")
                break
            else:
                print("Opcion invalida!")

if __name__ == "__main__":
    mi_agenda = Agenda()
    mi_agenda.menu()