#1. Suma los numeros del 1 al 10 usando ciclo for y 1 acumulador

# print("Suma de los numeros del 1 al 10")

# suma = 0

# for numero in range(1,11): #suma del 1 al 10
#     suma += numero
# print(suma) #Imprime 55
    
# #2. Numeros pares del 2 al 20

# print("Numeros pares del 2 al 20")

# for pares in range (2, 21, 2):
#     print (pares)
    
# # while 1. promedio de notas
    
# #Paso 1: Inicialice una variable para la sumatoria de notas y el iterador del while
 
# suma_notas = 0   # Acumulador para sumar las calificaciones
# contador = 1     # Variable iteradora del while para contar las 5 vueltas

# # Paso 2: Crear el ciclo while, pedir nota, acumular e incrementar

# while contador <= 5:
#     nota = float(input(f"Ingrese la nota {contador}: "))  # Pide la nota
#     suma_notas += nota                                    # Acumula la nota
#     contador += 1                                         # Incrementa el iterador
    
# # Paso 3: Calcular el promedio y mostrar el resultado

# promedio = suma_notas / 5
# print(f"Su promedio es: {promedio}")

#2. Numeros pares


# print("¡Bienvenido al juego del número secreto! \n Tiene 3 intentos para adivinar el numero oculto \n")

# numero_secreto = 7

# intento = int(input("Te quedan 3 intentos. Ingrese un numero: "))

# while intento != numero_secreto: 
#     print("Incorrecto. !Intenta de nuevo¡ \n")
    
#     intento = int(input("Te quedan 2 intentos. Ingrese un numero: "))

# #while intento != numero_secreto:
#     print("Incorrecto. !Intenta de nuevo¡ \n")
     
#     intento = int(input("Te queda 1 intento. Ingrese un numero: "))
#     print("Te quedaste sin intentos. El número secreto era: 7")    

# print("¡Adivinaste el número oculto!")


print("¡Bienvenido al juego del número secreto! \n Tiene 3 intentos para adivinar el numero oculto \n")

numero_secreto = 7
total_intentos = 3

numero = int(input("Te quedan 3 intentos. Ingrese un numero: "))
if numero != numero_secreto and total_intentos == 3:
    print("Incorrecto. !Intenta de nuevo¡ \n")

    numero = int(input("Te quedan 2 intentos. Ingrese un numero: "))
elif numero != numero_secreto and total_intentos == 2:
    print("Incorrecto. !Intenta de nuevo¡ \n")
    
elif numero != numero_secreto and total_intentos == 1:
    numero = int(input("Te queda 1 intento. Ingrese un numero: "))
    
elif numero > total_intentos:  
    print("Te quedaste sin intentos. El número secreto era: 7 \n")    
    
else:
    numero == numero_secreto
    print("¡Adivinaste el número oculto!")