#Calculadora de edad
print("CALCULADORA DE EDAD")
año_nacimiento = int (input ("Ingrese su año de nacimiento: "))
año_actual = int (input ("Ingrese el año en que esta: "))

if año_actual > año_nacimiento:
    print("Ingrese un año de nacimiento valido")
    
elif año_nacimiento == año_actual:
   print("Posiblemente acabas de nacer")
else:
    print (f"Su edad aproximada es： {año_actual - año_nacimiento}")
