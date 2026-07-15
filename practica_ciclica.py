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

#3. Tabla de multiplicar

# Pedir un número al usuario
numero = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar del {numero}:")

# Bucle del 1 al 10 para mostrar la tabla
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
# Adivina el numero secreto
numero_secreto = 7
total_intentos = 3

print("¡Bienvenido al juego del número secreto! \n")

print("Tiene 3 intentos para adivinar el numero oculto \n")

#Bucle para controlar los intentos

for intentos_restantes in range(3, 0, -1):
# Solicitar el número al usuario
    intento = int(input(f"Te quedan {intentos_restantes} intentos. Ingresa tu número: "))
    
    # Verificar si acertó
    if intento == numero_secreto:
        print("¡Felicidades! ¡Adivinaste el número secreto!")
        break

    else:
        # Si aún le quedan intentos, mostrar mensaje de fallo
        if intentos_restantes > 1:
            print("Incorrecto, ¡intenta de nuevo!\n")

else:
    # Este bloque ejecuta solo si el bucle terminó normalmente sin un 'break'
    print(f"\nTe quedaste sin intentos. El número secreto era {numero_secreto}.")
    
#Calculadora de operaciones basicas infinitas

while True:
    # Desplegar el menú de opciones por pantalla
    print("--- CALCULADORA DE OPERACIONES BÁSICAS ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1-5): ")
   #print()  # Espacio en blanco para orden

    # Validar si el usuario decide salir del ciclo infinito
    if opcion == "5":
        print("¡Hasta luego!")
        break
        
    # Verificar que sea una opción válida antes de pedir los números
    if opcion in ["1", "2", "3", "4"]:
        # Pedir los 2 números al usuario y convertirlos a flotantes
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        # Evaluar la operación seleccionada
        if opcion == "1":
            resultado = num1 + num2
            print(f"\nResultado de la suma: {num1} + {num2} = {resultado}\n")
        elif opcion == "2":
            resultado = num1 - num2
            print(f"\nResultado de la resta: {num1} - {num2} = {resultado}\n")
        elif opcion == "3":
            resultado = num1 * num2
            print(f"\nResultado de la multiplicación: {num1} * {num2} = {resultado}\n")
        elif opcion == "4":
            # Validación simple para evitar la división por cero
            if num2 != 0:
                resultado = num1 / num2
                print(f"\nResultado de la división: {num1} / {num2} = {resultado}\n")
            else:
                print("\nError: No se puede dividir entre cero.\n")
    else:
        print("Opción no válida. Por favor, intenta de nuevo.\n")