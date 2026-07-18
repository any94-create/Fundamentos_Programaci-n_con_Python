def sum(a, b):
    return a + b

def res(a, b):
    return a - b

def mul(a, b): 
    return a * b

def div(a, b):
    
    if b == 0:
        raise ValueError("No puede dividir por 0")
    
    return a / b

