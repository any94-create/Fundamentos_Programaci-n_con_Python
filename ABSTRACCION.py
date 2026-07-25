# ----- se utiliza a traves de una libreria

from abc import ABC, abstractmethod

class Trabajador(ABC):
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    @abstractmethod
    def trabajo():
        pass


class Secretaria(Trabajador):
    def __init__(self, nombre, edad, salario, antiguedad):
        super().__init__(nombre, edad, salario)
        self.antiguedad = antiguedad


    def trabajo():
        pass

class Chofer(Trabajador):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad, salario)

trabajador1 = Trabajador("Elena", 25, 12000, "5 años")

trabajador1.trabajo()