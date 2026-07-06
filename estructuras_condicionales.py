# edad = 15

# if edad < 18:
#     print("Usted es menor de edad") 
    
# if edad <= 18:
#     print("Usted es mayor de edad") 

# if edad < 18:
#     print("Usted es menor de edad") 
    
# else:
#     print("Usted es mayor de edad") 

#edad = int (input ("Ingrese edad: "))

# if edad >= 1 and edad <= 12:
#     print("Eres un niño") 
    
# elif edad >12 and edad <= 17:
#     print("Eres un adolescente")

# elif edad >= 18 and edad <= 59:
#     print("Eres un adulto")

# else:
#     print("Eres un anciano")

# if edad >=0 or edad > 100:
#     print("Edad incorrecta")

# else:
#     if edad >= 1 and edad <= 12:
#         print("Eres un niño") 
    
#     elif edad >12 and edad <= 17:
#         print("Eres un adolescente")

#     elif edad >= 18 and edad <= 59:
#         print("Eres un adulto")

#     else:
#         print("Eres un anciano")
        
# if edad >=0 or edad > 100:
#     print("Edad incorrecta")

# elif edad >= 1 and edad <= 12:
#     print("Eres un niño") 
    
# elif edad >12 and edad <= 17:
#     print("Eres un adolescente")

# elif edad >= 18 and edad <= 59:
#     print("Eres un adulto")

# else:
#    print("Eres un anciano")
   
   
# if edad >=0 or edad > 100:
#     print("Edad incorrecta")

# elif edad <= 12:
#     print("Eres un niño") 
# elif edad <= 17:
#     print("Eres un adolescente")
# elif edad <= 59:
#     print("Eres un adulto")
# else:
#    print("Eres un anciano")
 
#MATCH validacion de datos especificos
  
numero = int (input ("Ingrese un numero: "))

match numero:
    case 0:
        print("El numero ingresado es 0")
    case 5:
        print("El numero ingresado es 5")
    case _:
        print(f"El numero ingresado es : {numero}")
    