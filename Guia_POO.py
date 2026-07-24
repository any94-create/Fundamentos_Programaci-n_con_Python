#----------------------------- 1. REGISTRO DE TELEFONOS----------------------------------

class Telefono:
    
    def __init__(self, marca, modelo, precio):
        
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    
    def mostrar_informacion(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nPrecio: {self.precio} \n")
    
telefono1 = Telefono("Samsung", "S26 Ultra", "$1,300")
telefono2 = Telefono("Iphone", "17 Pro Max", "$1,600")
telefono3 = Telefono("Honor", "Magig 8 Lite", "$420")

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
        print(f"Nombre: {self.nombre} \nCargo: {self.cargo} \nSalario: {self.salario} \n")
        
    
empleado1 = Empleado("Roberto Jose Lagos Calero", "Gerente", "$1500")
empleado2 = Empleado("Elena Maria Rosales Cruz", "Secretaria", "$900")
empleado3 = Empleado("Miguel Antonio Gonzales Tercero", "Conductor", "$500")

empleado1.mostrar_datos()
empleado2.mostrar_datos()
empleado3.mostrar_datos()

#----------------------------- 4. ESTADO DE UNA COMPUTADORA ----------------------------------

