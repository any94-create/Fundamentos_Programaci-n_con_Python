# import pandas as pd


# df = pd.read_csv('data.csv')
# df = pd.read_excel('data.xlsx')

# exported_df = df.to_excel('exported_data.xlsx', index=False)

# CONSTRUCTORES

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # def mostrar_informacion(self):
    #     print(f"Nombre: {self.nombre}, Edad: {self.edad}")
        
    #     persona1.mostrar_informacion()
        
persona1 = Persona("Juan", 30)
persona2 = Persona("Maria",25)
persona3 = Persona("Jose", 38)
persona4 = Persona("Ana", 35)
print(persona1.nombre)
print(persona1.edad)
print(persona2.nombre)
print(persona2.edad)
print(persona3.nombre)
print(persona3.edad)
print(persona4.nombre)
print(persona4.edad)

