#----------------------------- 1. REGISTRO DE TELEFONOS----------------------------------

class Telefono:
    
    def __init__(self, marca, modelo, precio):
        
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    
    def mostrar_informacion(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nPrecio: {self.precio} \n")
    
telefono1 = Telefono("Samsung", "S26 Ultra", 1,300)
telefono2 = Telefono("Iphone", "17 Pro Max", 1,600)
telefono3 = Telefono("Honor", "Magig 8 Lite", 420)

telefono1.mostrar_informacion()
telefono2.mostrar_informacion()
telefono3.mostrar_informacion()

#----------------------------- 2. CATALOGO DE LIBROS----------------------------------

class Libro:
    
    def __init__(self, titulo, autor, paginas):
        
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def mostrar(self):
        print(f"Titulo: {self.titulo} \nAutor: {self.autor} \nPaginas: {self.paginas} \n")
        
    def leer(self):
        print(f"El libro que leera es: {self.titulo}\n")

#  def leer(self):
        # Cambiamos el print por inputs para que realmente "lea" datos del usuario
        #print(f"--- Modificando los datos de: {self.titulo} ---")
        #self.titulo = input("Ingrese el nuevo título: ")
        #self.autor = input("Ingrese el nuevo autor: ")
        #self.paginas = input("Ingrese las nuevas páginas: ")
        #print()
    
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "471")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "96")


libro1.mostrar()
libro2.mostrar()

libro1.leer()
libro2.leer()


#----------------------------- 3. DATOS DE EMPLEADOS----------------------------------

class Empleado:
    
    def __init__(self, nombre, cargo, salario):
        
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    
    def mostrar_datos(self):
        print(f"Nombre Empleado: {self.nombre} \nCargo: {self.cargo} \nSalario: $ {self.salario} \n")
        
    
empleado1 = Empleado("Roberto Jose Lagos Calero", "Gerente", 1500)
empleado2 = Empleado("Elena Maria Rosales Cruz", "Secretaria", 900)
empleado3 = Empleado("Miguel Antonio Gonzales Tercero", "Conductor", 500)

empleado1.mostrar_datos()
empleado2.mostrar_datos()
empleado3.mostrar_datos()

#----------------------------- 4. ESTADO DE UNA COMPUTADORA ----------------------------------

class Computadora:
    
    def __init__(self, marca, ram, procesador):
        
        self.marca = marca
        self.ram = ram
        self.procesador = procesador
        self.encendida = False
    
    def encender(self):
        self.encendida =True
        print(f"La computadora marca: {self.marca} se ha encendido \n")
        
    def apagar(self):
        self.encendida =False
        print(f"La computadora marca: {self.marca} se ha apagado \n")


pc = Computadora("Lenovo", "16 GB", "Ryzen 7")


pc.encender()
pc.apagar()

#----------------------------- BLOQUE # 2 CONSTRUCTORES --------------------------------------
#----------------------------- 5. INFORMACIÓN DE VEHÍCULIOS ----------------------------------

class Vehiculo:
    
    def __init__(self, marca, modelo, año):
        
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar(self):
        print(f"Su vehiculo es:\nMarca: {self.marca} \nModelo: {self.modelo}\nAño: {self.año} \n")
        

vehiculo1 = Vehiculo("Toyota", "Corolla", 2025)
vehiculo2 = Vehiculo("Chevrolet", "ONIX", 2022)
vehiculo3 = Vehiculo("KIA", "Picanto", 2024)


vehiculo1.mostrar()
vehiculo2.mostrar()
vehiculo3.mostrar()

#----------------------------- 6. REGISTRO DE ESTUDIANTES ----------------------------------

class Estudiante:
    
    def __init__(self, nombre, carrera, promedio):
        
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} \nCarrera: {self.carrera}\nPromedio: {self.promedio} \n")
        

estudiante1 = Estudiante("Juan Carlos Rivera Munguia", "Administracion de empresa", "90%")

estudiante1.mostrar_informacion()

#----------------------------- 7. CONTROL DE PRODUCTOS ----------------------------------

class Producto:
    
    def __init__(self, nombre, precio, stock):
        
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar(self):
        print(f"Nombre: {self.nombre} \nPrecio: {self.precio}\nStock: {self.stock} \n")
        
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        
            print(f"Venta exitosa: Se vendieron {cantidad} unidades de {self.nombre}.")

        else:
            print(f"Error: No hay suficiente stock de {self.nombre}. Stock disponible: {self.stock}")
   

# 1. Registrar el producto
producto = Producto("Laptop", 800, 10)

# 2. Mostrar la información inicial
producto.mostrar()  # Stock: 10

# 3. Realizar una venta válida
producto.vender(3)  # Reduce el stock en 3

# 4. Mostrar el stock actualizado
producto.mostrar()  # Stock: 7

# 5. Intentar una venta sin stock suficiente
producto.vender(12) # Muestra error

#----------------------------- 8. MASCOTAS DE UNA VETERINARIA ----------------------------------
class Mascota:
    
    def __init__(self, nombre, especie, edad):
        
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def presentarse(self):
        print(f"Nombre: {self.nombre} \nEspecie: {self.especie}\nEdad: {self.edad} \n")
        
mascota = Mascota("Bambi", "Perro", 2)

mascota.presentarse()

#----------------------------- BLOQUE #3 ENCAPSULACIÓN ----------------------------------
#----------------------------- 9. CUENTA BANCARIA CONSULTA ----------------------------------

class Cuenta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        
    def consultar_saldo(self):
        return self.__saldo

cuenta1 = Cuenta_Bancaria("Ernesto Jose Reyes Lopez", 100000)

print(cuenta1.consultar_saldo()) 

#----------------------------- 10. CUENTA BANCARIA DEPOSITO ----------------------------------


