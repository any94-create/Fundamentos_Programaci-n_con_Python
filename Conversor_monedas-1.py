print ("Conversor de monedas")

print("*********Menu de Opciones*******")
print("1. Cordobas a Dolares")
print("2. Dolares a Cordobas")
print("3. Euros a Cordobas")
print("4. Cordobas a Euros")

opcion = int (input("Ingrese la opcion: "))

cantidad = float(input("ingrese la cantidad de dinero a convertir: "))
tipo_cambio = float(input("ingrese el tipo de cambio: "))

match opcion:
    case 1:
        print(f"La cantidad equivalente en  dolares es: {cantidad / tipo_cambio}")
    case 2:
        print(f"La cantidad equivalente en cordobas es: {cantidad * tipo_cambio}")
    case 3:
        print(f"La cantidad equivalente en cordobas es: {cantidad * tipo_cambio}")
    case 4:
        print(f"La cantidad equivalente de euros es: {cantidad / tipo_cambio}")
