#Datos mascota
print("DATOS DE UNA MASCOTA")

Nombre_mascota = input ("Ingrese el nombre de la mascota: ")
print (f"Nombre_mascota: {Nombre_mascota}")

Edad = int(input("Ingrese la edad de la mascota: "))
print (f"La edad de su mascota es: {Edad}")

Peso = float(input("Ingrese el peso: "))
print (f"El peso de su mascota es: {Peso} kg")

Vacunado = (input ("Su mascota esta vacunada si o no: "))
if Vacunado == "si":
     print("Su mascota esta vacunada") 
    
else:
     print("Su mascota no esta vacunada") 