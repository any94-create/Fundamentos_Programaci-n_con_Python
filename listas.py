# 1.Crear una lista de calificaciones
#calificaciones = [85, 90, 78, 92,88]

#print("Lista inicial: ")
#print(calificaciones)

#lista = ['Ana', 'Patricia', 32, 'Nicaraguense']
#print("Mis datos personales:")

#  Operador de asignacion aumentada utilizado para acumuladores y bucles
# lista += ['Bambi']


#lista.append ('Bambi')

#extend permite agregar una lista a la lista inicial
#lista.extend (['Bambi'])

#insert agrega un elemento en una posicion determinada
#lista.insert (-1,'Bambi')
#print(lista)

nombres = ['Julio', 'Maria', 'Carlos']
#print("\n Nombres Originales")
#print(nombres)

#nombres = ['Julio']
#print("\n Nombres")
#print(nombres)

#nombres.remove ['Julio']
#print(nombres)

#print(nombres[2])
#print(nombres[-1])

#La funcion sum () con un generador
# Contar cuantos valores contiene una lista sin variables intermediarias

total = sum( 1 for _ in nombres)
print(total)

# funcion len Contar cuantos valores contiene una lista
#total_elementos = len(nombres)
#print(total_elementos)


#count cuenta cuantas veces se repite un valor especifico
#numeros = [1, 2, 1, 4, 5, 6, 3, 1]
#repeticiones = numeros.count()
#print(repeticiones)