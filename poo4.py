class Animal:
    pass

    def __init__(self, nombre, edad, color, raza):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.raza = raza
        
# animal1 = Animal("Bambi", 3, "negro", "doberman")
# animal2 = Animal("Mylo", 1, "chocolate", "siberiano")
# animal3 = Animal("Galleta", 1, "Manchada", "terrier")
# animal4 = Animal("Romeo", 2, "cafe", "doberman pincher")
# animal5 = Animal("Bobby", 8, "blanco", "salchicha")

#print(animal1.nombre)
# print(animal1.edad)
# print(animal1.color)
# print(animal1.raza)

# print(animal2.nombre)
# print(animal2.edad)
# print(animal2.color)
# print(animal2.raza)

# print(animal3.nombre)
# print(animal3.edad)
# print(animal3.color)
# print(animal3.raza)

# print(animal4.nombre)
# print(animal4.edad)
# print(animal4.color)
# print(animal4.raza)

# print(animal5.nombre)
# print(animal5.edad)
# print(animal5.color)
# print(animal5.raza)


# print("Los datos de su primer animal es\n")
# print(f"El nombre de la mascota es: {animal1.nombre}\nTiene: {animal1.edad} años\nEs color: {animal1.color}\nEs raza: {animal1.raza}\n")

# print("\nLos datos de su segundo animal es\n")
# print(f"El nombre de la mascota es: {animal2.nombre}\nTiene: {animal2.edad} años\nEs color: {animal2.color}\nEs raza: {animal2.raza}")

# print("\nLos datos de su tercer animal es\n")
# print(f"El nombre de la mascota es: {animal3.nombre}\nTiene: {animal3.edad} años\nEs color: {animal3.color}\nEs raza: {animal3.raza}")

# print("\nLos datos de su pcuarto animal es\n")
# print(f"El nombre de la mascota es: {animal4.nombre}\nTiene: {animal4.edad} años\nEs color: {animal4.color}\nEs raza: {animal4.raza}")

# print("\nLos datos de su quinto animal es\n")
# print(f"El nombre de la mascota es: {animal5.nombre}\nTiene: {animal5.edad} años\nEs color: {animal5.color}\nEs raza: {animal5.raza}")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nColor: {self.color} \nRaza: {self.raza}")
    
perro = Animal("Leyla", 2, "negro", "salchicha")
gato = Animal("Minino", 1, "blanco", "angora")
conejo = Animal("Bolita", 3,"cafe","frances")
chocoyo = Animal("Lolita", 3, "Verde con amarillo", "")
ardilla = Animal("Querubin", 1, "blanco con negro", "")

perro.mostrar_informacion()
gato.mostrar_informacion()
conejo.mostrar_informacion()
chocoyo.mostrar_informacion()
ardilla.mostrar_informacion()