palabra_prohibida = ['pizza', 'coca cola']

while True:
  palabra = input("Ingrese una palabra: ")
  palabra = palabra.lower() # Convierte las mayusculas 

  if not palabra: 
    print("No ha ingresado ninguna palabra. Por favor, intente de nuevo.")
    continue 

  if palabra in palabra_prohibida:
    print(f"Usted ha ingresado una palabra prohibida: {palabra}")
    break 
