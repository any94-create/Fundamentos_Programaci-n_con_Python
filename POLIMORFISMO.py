# ------ definimos metodos con el mismo nombre con comportamientos diferentes vendedor, contrato profesional, fijo -----

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_salario(self):
        pass

class Empleado_fijo(Empleado):
    def __init__(self, salario_mensual):
        super().__init__()
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual

class Vendedor(Empleado):
    def __init__(self, salario_base, venta, comision):
        super().__init__(self.nombre)
        self.salario_base = salario_base
        self.ventas = venta
        self.comision = comision

    def calcular_salario(self):
        return self.salario_base + (self.ventas * self.comision)

class Contrato_Profesional(Empleado):
    def __init__(self, cant_horas, valor_hora_trabajada):
        super().__init__(self.nombre)
        self.cant_horas = cant_horas
        self.valor_hora_trabajada = valor_hora_trabajada

    def calcular_salario(self):
        return self.cant_horas * self.valor_hora_trabajada

empleados = [
            Empleado_fijo("Jose Calero", 8500),
            Vendedor("Ernesto Gomez", 8500, 30000, 0.05),
            Contrato_Profesional("Carlos Martinez", 180, 80)
]

for emp in empleados:
    print(f"El salario de {emp.nombre} es: {emp.salario()}")
       
