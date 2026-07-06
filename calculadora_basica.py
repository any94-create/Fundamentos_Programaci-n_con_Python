print ("Calculadora de operaciones basicas")

numero1 = float (input ("Ingrese el primer numero: "))
numero2 = float (input ("Ingrese el segundo numero: "))
# Metodo isgigit
n1 = input("Ingrese el primer numero: ")

if n1.isdigit():
    numero1 = float(n1)

    n2 = input("Ingrese el segundo numero: ")

    if n2.isdigit():
        numero2 = float(n2)
    
        print("*********Menu de Opciones*******")
        print("1. Suma")
        print("2. Resta")
        print("3. multiplicacion")
        print("4. Division")
        print("5. Salir")

        opcion = int (input("Ingrese la opcion: "))

        match opcion:
            case 1:
                print(f"La suma de {numero1} + {numero2} es: {numero1 + numero2}")
            case 2:
                print(f"La resta de {numero1} - {numero2} es: {numero1 - numero2}")
            case 3:
                print(f"La multiplicacion de {numero1} * {numero2} es: {numero1 * numero2}")
            case 4:
                #valide la division entre 0
                if numero2 == 0:
                    print("El segundo numero no puede ser 0")
                else: 
                    print(f"La division de {numero1} / {numero2} es: {numero1 / numero2}")
            case 5:
                print("Saliendo del programa")
            case _:
                print("Opcion incorrecta")

    else:
        print("Valor incorrecto")
else:
    print("Valor incorrecto")