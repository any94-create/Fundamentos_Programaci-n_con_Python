# # EJERCICIOS PRACTICOS
# #1RESUELVA CADA UNOS DE LOS ESCENARIOS

# mi_tupla = [10, 20, 30, 40, 50, 60, 70, 80]

# # ACCEDER AL PRIMER ELEMENTO
# print("El primer elemento de la tupla es: ", mi_tupla[0])

# # OBTENER LOS ÚLTIMOS CUATRO ELEMENTOS
# print("Sus ultimos cuatro elementos de la tupla son: ", mi_tupla[-4:])
 
# # ACCEDER A LOS ELEMENTOS DE LOS INDICES 3 AL 6 
# print(mi_tupla[3:7])

# # INCISO B

# factura = ['pan', 'huevos', 100, 1234]

# # TAMAÑO DE LA TUPLA

# print("El tamaño de su tupla es de: ", len(factura))

# # OBTENER EL INDICE DEL ELEMENTO HUEVOS

# elemento = 'huevos'
# indice = factura.index(elemento)
# print(f"El elemento {elemento} se encuentra en el indice: ", indice)

# # BUSCAR SI ECISTE EL ELEMENTO COCA COLA

# elemento_buscar = 'coca cola'
# if elemento_buscar in factura:
#     print(f"La palabra {elemento_buscar} se encuentra en la tupla. ")
# else:
#     print(f"La palabra {elemento_buscar} no se encuentra en la tupla. ")

# # encuentre el error en cada uno de los escenarios
# # a. el codigo intenta modificar una tupla

# # las tuplas son inmutables para solucionarlo usa una lista en lugar de una tupla utilizando corchetes
# colores = ["rojo", "verde", "azul"]
# colores[1] = "amarillo"
# print(colores)

# # opcion 2 onvertir la tupla a lista y luego volver a tupla

# colores = ("rojo", "verde", "azul")
# lista_colores = list(colores)  # Convierte a lista
# lista_colores[1] = "amarillo"  # Modifica
# colores = tuple(lista_colores)  # Convierte de vuelta a tupla
# print(colores)  # Resultado: ('rojo', 'amarillo', 'azul')

# # B. INTENTA IMPRIMIR LOS ELEMENTOS DE UNA TUPLA

# datos = ("Juan", 30, "Ingeniero")
# nombre, edad, profesion = datos #Asignando etiquetas a los elementos
# print(f"Nombre: {nombre}, Edad: {edad}, Profesion: {profesion}")

# # C. INTENTA IMPRIMIR ELEMENTOS DE LA TUPLA

# frutas = ["manzana", "pera", "naranja", "plátano", "uva"]
# print(frutas[4])
# print(frutas[-5])
# frutas[1:3] = ("kiwi", "mango")
# print(frutas)


# #----- NIVEL FACIL -----

# # 1. DIAS DE LA SEMANA Y MUESTRA EL TERCER DIA

# dias_semana = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')
# print("El tercer dia de la semana es: ", dias_semana[2])


# # CREA UNA TUPLA 10 NUMEROS ENTEROS, MUESTRE CUANTOS ELEMENTOS TIENE
# numeros_enteros = (2, 4, 6, 20, 12, 16, 22, 34, 56, 18)
# print("Su tupla tiene: ", len(numeros_enteros))


# cantidad = len(numeros_enteros)
# print(f"Su tupla tiene {cantidad} elementos")

# # CREA DOS TUPLAS CON 5 ELEMENTOS CON TIPOS DE DATOS VARIADO
# # FUSIONARLAS Y MOSTRARLAS EN PANTALLA

# tupla1 =('tomate', 'sal', 20, 'papaya', 18)
# tupla2 = ('carne', 15, 'pollo', 20, 'papa')
# total = tupla1 + tupla2
# print("Los elementos de su tupla son: ", total)

# # CREA TUPLA CON CADENA DE TEXTO Y VERIFIQUE SI EXISTE EN LA TUPLA

# elementos = ('mesa', 'silla', 'sofa', 'cama', 'comedor','ropero', 'chinero')
# print("------MUEBLES PARA EL HOGAR------")
# elemento_buscar = input("Ingrese la consulta sobre el mueble para el hogar que desee: ")

# if elemento_buscar in elementos:
#     print(f"El mueble {elemento_buscar} se encuentra en la tupla. ")
# else:
#     print(f"El mueble {elemento_buscar} no se encuentra en la tupla. ")
  
# # PIDA 1 NUMERO ENTERO POR TECLADO Y CUENTE CUANTAS VECES APARECE EL NUMERO

# tupla_numerica = (25, 38, 12, 5, 22, 69, 81,45, 12, 28) 

# numero = int(input("Ingrese un numero entero: "))

# print(f"Numero de veces que pareceel numero {numero} es: ",tupla_numerica.count(numero))
 
# # PEDIR 5 DATOS POR TECLADO, ALMACENARLAR EN LA TUPLA 
# # MOSTRAR TODOS LOS DATOS DE LA TUPLA EN PANTALLA

# datos_tupla = []

# for intento in range(1, 6):
#     tupla = input(f"Ingrese 5 elementos 1 a la vez {intento}/5: ")
#     datos_tupla.append(tupla)
    
# # convertimos la lista a tupla
# datos_tupla = tuple(datos_tupla)

# print("\n Los datos ingresados son: ")
# print(datos_tupla)

# # PEDIR 8 NOMBRES ANIMALES POR TECLADO, ALMACENARLAR EN LA TUPLA 
# # MOSTRAR POR PANTALLA CUANTAS VECES SE REPITIO CADA UNO

# nombre_animales = []

# for a in range(1, 9):
#     animales = input(f"Ingrese 8 nombres de animales {a}/8: ")
#     nombre_animales.append(animales)
    
# # convertimos la lista a tupla
# nombre_animales = tuple(nombre_animales)
# print("NOMBRE DE LOS ANIMALES QUE INGRESO", nombre_animales)

# elemento_buscar = input("\n Ingrese el nombre que desea contar: ")

# repeticiones_animales = sum(1 for n in nombre_animales if n.lower () == elemento_buscar.lower())

# print(f"EL nombre {elemento_buscar} se repite {repeticiones_animales} veces")

# # N numero y n cantidad de numeros

# num = int(input("Ingrese la cantidad de numeros: "))

# # pide los n numeros y los guarda

# lista_num = []
# for i in range(num):
#     enteros = int(input(f"Ingrese el numero {i+1}: "))
#     lista_num.append(enteros)
# tupla_entero = tuple(lista_num)

# # recorrer y separar en par e impar

# tupla_par = ()
# tupla_impar = ()

# for enteros in tupla_entero:
#     if enteros % 2 == 0:
#         tupla_par += (enteros,)
#     else:
#         tupla_impar += (enteros,)

# # mostrar 3 tuplas en pantalla

# print("\n--- Resultados ---")
# print("Tupla entero:", tupla_entero)
# print("Tupla de pares:", tupla_par)
# print("Tupla de impares:", tupla_impar)
    


# NIVEL DIFICIL


n = int(input("Ingrese la cantidad de tuplas a crear (N): "))
todas_las_tuplas = []

# 2. Llenar cada tupla con 5 datos
for i in range(n):
    print(f"\n--- Ingrese 5 Datos para la cantidad de Tuplas {i + 1} ---")
    datos_lista = []
    for j in range(5):
        dato = input(f"  Ingrese el dato {j + 1}: ")
        datos_lista.append(dato)
    
    # Convertimos la lista de 5 datos en tupla y la guardamos
    todas_las_tuplas.append(tuple(datos_lista))

# 3. Menú interactivo de opciones
while True:
    print("\n========= MENÚ DE OPCIONES =========")
    print("a) Mostrar una tupla específica")
    print("b) Buscar un valor en una tupla")
    print("c) Mostrar tamaño de una tupla")
    print("d) Fusionar todas las tuplas")
    print("e) Salir")
    
    opcion = input("Seleccione una opción: ").lower().strip()
    
    if opcion == 'a':
        idx = int(input(f"Ingrese el número de tupla a mostrar (1 a {n}): ")) - 1
        if 0 <= idx < n:
            print(f"Tupla {idx + 1}: {todas_las_tuplas[idx]}")
        else:
            print("Error: Número de tupla fuera de rango.")
            
    elif opcion == 'b':
        valor = input("Ingrese el valor que desea buscar: ")
        encontrado = False
        for i, tupla in enumerate(todas_las_tuplas):
            if valor in tupla:
                print(f"¡Encontrado! El valor '{valor}' está en la Tupla {i + 1}")
                encontrado = True
        if not encontrado:
            print(f"El valor '{valor}' no se encuentra en ninguna tupla.")
            
    elif opcion == 'c':
        idx = int(input(f"Ingrese el número de tupla (1 a {n}): ")) - 1
        if 0 <= idx < n:
            # Siempre será 5 según la instrucción, pero usamos len() como pide el ejercicio
            print(f"El tamaño de la Tupla {idx + 1} es: {len(todas_las_tuplas[idx])} elementos")
        else:
            print("Error: Número de tupla fuera de rango.")
            
    elif opcion == 'd':
        tupla_fusionada = ()
        for tupla in todas_las_tuplas:
            tupla_fusionada += tupla
        print("Resultado de fusionar todas las tuplas:")
        print(tupla_fusionada)
        
    elif opcion == 'e':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")