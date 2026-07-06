#------------Recorrer listas--------------------------

print("\nLista de marca de celulares")

marca_celulares = ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Tecno', 'Redmi']

for marca_celulares in marca_celulares:
    print(marca_celulares)
    
#---------Mostrar posicion y elemento------

print("\nPosicion de cada marca")

for i in range(len(marca_celulares)):
    print("Posicion ", i, "->", marca_celulares[i])
    