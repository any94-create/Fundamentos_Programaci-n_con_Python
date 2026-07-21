# Definimosun diccionario para la simulación de una cuenta bancaria

cuenta {
    "saldo":10000
    "pin":4321
}

# Muestra el menu principal

def menu():
  print("\nBIENVENIDO AL CAJERO AUTOMATICO\n")
  print("1. CONSULTAR SALDO")
  print("2. DESPOSITO")
  print("3. RETIRO")
  print("4. SALIR")

  # Esto solicita al usuario que ingrese una opción y almacena la entrada en la variable choice
  choice = input("Por favor, seleccione una opción (1-4): ")

  # devuelve la opción elegida por el usuario a quien realiza la llamada.
  return opcion

  # FUNCION PARA CONSULTAR EL SALDO

  def consulta_saldo(): 

    # Esto recupera el saldo del diccionario de la cuenta y lo imprime en una cadena formateada.
    print(f"Su saldo actual es: ${cuenta["saldo"]}") 

  # DEPOSITO

  def depositar_dinero(): 
    cantidad = float(input("Ingrese la cantidad a depositar: ")) 
    if cantidad > 0: 
        cuenta["saldo"] += cantidad # Si el importe es positivo, lo suma al saldo.
        # Imprime un mensaje de confirmación con el nuevo saldo.
        print(f"${cantidad} ha sido depositada. Su nuevo saldo es: ${cuenta["saldo"]}") 
    else: 
        print("Cantidad no válida. Ingrese un número positivo.")   

    # RETIRO

     def retirar_dinero():
      # solicita al usuario que ingrese la cantidad a retirar y convierte la entrada a un número flotante.
      cantidad = float(input("Ingrese la cantidad a retirar: ")) 

      # Esto comprueba si la cantidad es positiva.
      if cantidad > 0:

        # Si la cantidad es menor o igual que el saldo actual, se resta la cantidad del saldo.
          if cantidad <= cuenta"saldo":

            # Esto resta el importe del saldo.
              cuenta["saldo"] -= cantidad

              # Imprime un mensaje de confirmación con el nuevo saldo.
              print(f"${cantidad} ha sido retirado. Su nuevo saldo es: ${cantidad["saldo"]}")
          else:
            # Si el monto excede el saldo actual, imprime un mensaje de error
              print("Fondos insuficientes. Su saldo actual es: ${cantidad["saldo"]}")
      else:
          print("Cantidad no válida. Introduzca un número positivo.")

 # Función principal para hacer funcionar el cajero automático

def run_atm(): 
    # Solicitar al usuario que ingrese el PIN 
    pin = input("Por favor, ingrese su PIN: ") 
    
    # Comprobar si el PIN ingresado es correcto 
    if pin == cuenta["pin"]:
        #  Esto inicia un bucle infinito para mantener el cajero automático en funcionamiento hasta que el usuario decida salir.
        while True: 
            # llma al menu para mostrar el menú y obtener la elección del usuario.
            opcion = menu() 
            if opcion == '1': 
                consulta_saldo() 
            elif opcion == '2': 
                depositar_dinero() 
            elif opcion == '3': 
                retirar_dinero() 
            elif opcion == '4': 
                print("Gracias por usar el cajero automático. ¡Adiós!") 
                break 
            else: 
                print("Opción no válida. Por favor, seleccione una opción válida (1-4).") 
    else: 
        print("PIN incorrecto. Por favor, inténtelo de nuevo.") 

ejecutar_cajero automático() 
