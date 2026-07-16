notas_estudiante = [90, 58, 77, 81, 92, 65, 87]

print("Las notas del estudiante son: ", notas_estudiante)
# Salida: las notas de los estudiantes

print("La cuarta nota es: ", notas_estudiante[3])
#Salida la cuarta nota es: 81

#forma normal
print ("aultima nota es: ", notas_estudiante[6])

#forma con indice negativo
print("La ultima nota es: ", notas_estudiante[-1])

# ACCEDER A RANGOS DE ELEMENTOS DE UNA TUPLA

print("Las tres primeras notas son: ", notas_estudiante[:3])
#Salida (90,58,77)

print("Las tres ultimas notas son: ", notas_estudiante[:-3])
# salida (92, 65, 87)

print("Las notas desde la segunda hasta la cuarta son: ", notas_estudiante[1:4])
# salida (58, 77, 81)

print(notas_estudiante[1:6:2])
# salida (58, 81, 65)

# CONTEO DE ELEMENTOS EN LA TUPLA

print("Numero de elementos en la tupla: ", len(notas_estudiante))
# salida numero de elemtos en la tupla 7

print("Indice de la nota 92: ", notas_estudiante.index(92))
# conocer indice de los elementos de la tupla

# Conocer tamaño de la tupla
print("Numero de veces que parece la nota 81 es: ",notas_estudiante.count(81))

# BUSQUEDA DE ELEMENTOS TUPLA OPERADOR IN

nota_a_buscar =77

if nota_a_buscar in notas_estudiante:
    print(f"La nota {nota_a_buscar} se encuentra en la tupla. ")
else:
    print(f"La nota {nota_a_buscar} no se encuentra en la tupla. ")
    
nota_a_buscar =40

if nota_a_buscar in notas_estudiante:
    print(f"La nota {nota_a_buscar} se encuentra en la tupla. ")
else:
    print(f"La nota {nota_a_buscar} no se encuentra en la tupla. ")
    
# FUSIÓN TUPLAS OPERADOR +

notas_estudiante = (90, 58, 77, 81, 92, 65, 87)
nuevas_notas= (75, 88)

notas_actualizadas = notas_estudiante + nuevas_notas
print("Las notas han sido actualizadas: ", notas_actualizadas)

# DUPLICADO DE TUPLAS

copia = notas_estudiante[:]
print(copia)
