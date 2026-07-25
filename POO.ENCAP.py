class Persona:

             # self permite acceder a los valores o los metodos
    def __init__(self, nombre, edad, sexo, altura, peso): 
        self.nombre =  nombre
        self.edad = edad
        self.sexo = sexo
        self.altura = altura
        self.peso = peso

    def presentarse(self):
        pass  


persona1 = Persona() #instanciar una clase -atributos
