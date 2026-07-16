# EJERCICIOS PRACTICOS
#1RESUELVA CADA UNOS DE LOS ESCENARIOS

mi_tupla = [10, 20, 30, 40, 50, 60, 70, 80]

# ACCEDER AL PRIMER ELEMENTO
print("El primer elemento de la tupla es: ", mi_tupla[0])

# OBTENER LOS ÚLTIMOS CUATRO ELEMENTOS
print("Sus ultimos cuatro elementos de la tupla son: ", mi_tupla[-4:])
 
# ACCEDER A LOS ELEMENTOS DE LOS INDICES 3 AL 6 
print(mi_tupla[3:7])

# INCISO B

factura = ['pan', 'huevos', 100, 1234]

# TAMAÑO DE LA TUPLA

print("El tamaño de su tupla es de: ", len(factura))

# OBTENER EL INDICE DEL ELEMENTO HUEVOS

elemento = 'huevos'
indice = factura.index(elemento)
print(f"El elemento {elemento} se encuentra en el indice: ", indice)

# BUSCAR SI ECISTE EL ELEMENTO COCA COLA

elemento_buscar = 'coca cola'
if elemento_buscar in factura:
    print(f"La palabra {elemento_buscar} se encuentra en la tupla. ")
else:
    print(f"La palabra {elemento_buscar} no se encuentra en la tupla. ")

# encuentre el error en cada uno de los escenarios
# a. el codigo intenta modificar una tupla

# las tuplas son inmutables para solucionarlo usa una lista en lugar de una tupla utilizando corchetes
colores = ["rojo", "verde", "azul"]
colores[1] = "amarillo"
print(colores)

# opcion 2 onvertir la tupla a lista y luego volver a tupla

colores = ("rojo", "verde", "azul")
lista_colores = list(colores)  # Convierte a lista
lista_colores[1] = "amarillo"  # Modifica
colores = tuple(lista_colores)  # Convierte de vuelta a tupla
print(colores)  # Resultado: ('rojo', 'amarillo', 'azul')

# B. INTENTA IMPRIMIR LOS ELEMENTOS DE UNA TUPLA

datos = ("Juan", 30, "Ingeniero")
nombre, edad, profesion = datos #Asignando etiquetas a los elementos
print(f"Nombre: {nombre}, Edad: {edad}, Profesion: {profesion}")

# C. INTENTA IMPRIMIR ELEMENTOS DE LA TUPLA

frutas = ["manzana", "pera", "naranja", "plátano", "uva"]
print(frutas[4])
print(frutas[-5])
frutas[1:3] = ("kiwi", "mango")
print(frutas)


#----- NIVEL FACIL -----

# 1. DIAS DE LA SEMANA Y MUESTRA EL TERCER DIA

dias_semana = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')
print("El tercer dia de la semana es: ", dias_semana[2])


# CREA UNA TUPLA 10 NUMEROS ENTEROS, MUESTRE CUANTOS ELEMENTOS TIENE
numeros_enteros = (2, 4, 6, 20, 12, 16, 22, 34, 56, 18)
print("Su tupla tiene: ", len(numeros_enteros))


cantidad = len(numeros_enteros)
print(f"Su tupla tiene {cantidad} elementos")

# CREA DOS TUPLAS CON 5 ELEMENTOS CON TIPOS DE DATOS VARIADO
# FUSIONARLAS Y MOSTRARLAS EN PANTALLA

tupla1 =('tomate', 'sal', 20, 'papaya', 18)
tupla2 = ('carne', 15, 'pollo', 20, 'papa')
total = tupla1 + tupla2
print("Los elementos de su tupla son: ", total)

# CREA TUPLA CON CADENA DE TEXTO Y VERIFIQUE SI EXISTE EN LA TUPLA

elementos = ('mesa', 'silla', 'sofa', 'cama', 'comedor','ropero', 'chinero')
print("------MUEBLES PARA EL HOGAR------")
elemento_buscar = input("Ingrese la consulta sobre el mueble para el hogar que desee: ")

if elemento_buscar in elementos:
    print(f"El mueble {elemento_buscar} se encuentra en la tupla. ")
else:
    print(f"El mueble {elemento_buscar} no se encuentra en la tupla. ")
  
# PIDA 1 NUMERO ENTERO POR TECLADO Y CUENTE CUANTAS VECES APARECE EL NUMERO

tupla_numerica = (25, 38, 12, 5, 22, 69, 81,45, 12, 28) 

numero = int(input("Ingrese un numero entero: "))

print(f"Numero de veces que pareceel numero {numero} es: ",tupla_numerica.count(numero))
 
# PEDIR 5 DATOS POR TECLADO, ALMACENARLAR EN LA TUPLA 
# MOSTRAR TODOS LOS DATOS DE LA TUPLA EN PANTALLA

datos_tupla = []

for intento in range(1, 6):
    tupla = input(f"Ingrese 5 elementos 1 a la vez {intento}/5: ")
    datos_tupla.append(tupla)
    
# convertimos la lista a tupla
datos_tupla = tuple(datos_tupla)

print("\n Los datos ingresados son: ")
print(datos_tupla)

# PEDIR 8 NOMBRES ANIMALES POR TECLADO, ALMACENARLAR EN LA TUPLA 
# MOSTRAR POR PANTALLA CUANTAS VECES SE REPITIO CADA UNO

nombre_animales = []

for a in range(1, 9):
    animales = input(f"Ingrese 8 nombres de animales {a}/8: ")
    nombre_animales.append(animales)
    
# convertimos la lista a tupla
nombre_animales = tuple(nombre_animales)
print("NOMBRE DE LOS ANIMALES QUE INGRESO", nombre_animales)

elemento_buscar = input("\n Ingrese el nombre que desea contar: ")

repeticiones_animales = sum(1 for n in nombre_animales if n.lower () == elemento_buscar.lower())

print(f"EL nombre {elemento_buscar} se repite {repeticiones_animales} veces")
