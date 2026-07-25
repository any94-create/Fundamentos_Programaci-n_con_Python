# class Transporte:

#     def __init__(self, tipo, capacidad, velocidad):
#         self.tipo = tipo
#         self.capacidad = capacidad
#         self.velocidad = velocidad

#     def mostrar_datos(self):
#         print(f"Tipo: {self.tipo}, Capacidad: {self.capacidad}, Velocidad: {self.velocidad}")


# class Bus(Transporte):
#     def __init__(self, tipo, capacidad, velocidad, uso):
#         super.__init__(tipo, capacidad, velocidad)
#         self.uso = uso

#     def mostrar_datos(self):
#         print(f"Uso: {self.uso}")

# class Barco(Transporte):
#     def __init__(self, tipo, capacidad, velocidad, tamaño):
#         super.__init__(tipo, capacidad,velocidad,tamaño)
#         self.tamaño = tamaño    

#     def mostrar_informacion(self):
#         print(f"Tamaño: {self.tamaño}")


# #=----------------HERENCIAS MULTIPLES---------------------------

# class Persona:
#         def __init__(self, nombre, edad):
#             self.nombre = nombre
#             self.edad = edad

#         def saludar(self):
#             return f"Hola, mi nombre es {self.nombre} y tengo {self.edad}"

# class Empleado:
#     def __init__(self, salario):
#         self.salario = salario

#     def mostrar_informacion(self):
#         return f"Mi salario es: {self.salario}"

# ----------------------------------------------------------------------

class Supermercado:
    def __init__(self, area, ubicacion):
        self.area = area
        self.ubicacion = ubicacion

    def datos(self):
        return f"Hola esta en el area de: {self.area}, Ubicacion: {self.ubicacion}"

class Abarrotes:
    def __init__(self, granos_basicos):
        self.granos_basicos = granos_basicos

    def mostrar (self):
        return f"{self.granos_basicos}"

class Lacteos(Supermercado, Abarrotes):
    def __init__(self, area, ubicacion, granos_basicos, caducidad):
        Supermercado().__init__(area, ubicacion)
        Abarrotes().__init__(granos_basicos)        
        self.caducidad =caducidad

    def mostrar_datos(self):
        super().mostrar_datos()
        print (f"{self.caducidad}")
    
