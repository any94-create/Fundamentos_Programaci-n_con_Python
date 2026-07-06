#1. Mostrar los numeros del 1 al 10

print("Numeros del 1 al 10")

for i in range(1,11):
    print(i)

#2. Mostrar los numeros pares del 2 al 20

print("\nNumeros pares")

for i in range(2, 21, 2):
    print(i)    

    
    
#------------Recorrer listas--------------------------

print("\nLista de Frutas")

frutas = ['Manzana', 'Pera', 'Uva', 'Mango', 'Sandia']

for frutas in frutas:
    print(frutas)
    
#---------Mostrar posicion y elemento------

print("\n Posicion de cada fruta")

for i in range(len(frutas)):
    print("Posicion ", i, "->", frutas[i])
