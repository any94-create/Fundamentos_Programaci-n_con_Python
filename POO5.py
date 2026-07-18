# METODOS DENTRO DE CLASES

class Persona:
    def saludar(self):
        print("Hola, soy una persona")
        
    def despedida(self):
        print("Adios, hasta luego")
    
    def presentarse(self):
        print("Me llamo HUan y tengo 30 años")
    
person1 = Persona()
person2 = Persona()
person3 = Persona()

person1.saludar()
person2.presentarse()
person3.despedida()

class Banco:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.__cantidad = cantidad
        
    def get_cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, cantidad_nueva):
        self.__cantidad = cantidad_nueva
        
    # def mostrar_saldo(self):
    #     return self.__cantidad

banco1 = Banco("Banco de Espana", 100000)

print(banco1.get_cantidad())
banco1.__cantidad = 50000
print(banco1.get_cantidad())


# UTILIZAR PROGRAMACION ORIENTADA A OBJETOS
# CREAR UNA CLASE PARA UN CAJERO AUTOMATICO, UN CLIENTE
#QUE PERMITA MOSTRAR EL SALDO, DEPOSITAR Y RETIRAR DINERO