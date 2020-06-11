# Las Tuplas son Inmutables no podemos modificar los elementos que almacena agregar o quitar elementos
# Solo la podemos consultar

tupla = (1,2,3,4,5,6,7,8,9,0)

# indices 
# elemento = tupla[4]
# print(elemento)

# indices negativos
# elemento = tupla[-1] # Mostrara el ultimo de la tupla
# print(elemento)

# sub = tupla[:] # tambien podemos usar los : como en las listas desde hasta con saltos de...
# print(sub)

# # Tupla 2
# tupla2 = (1,2,3,4)
# uno, dos, tres, cuatro = tupla2[0], tupla2[1], tupla2[2], tupla2[3] # Lo podemos hacer tambien = tupla2
# print(uno)
# print(dos)
# print(tres)
# print(cuatro)

# # Cuando tenemos mas elementos pero pocas variables

# tupla2 = (1,2,3,4,5,6)
# uno, dos, tres, *cuatro = tupla2  # La variable cuatro se convierte en una lista [4,5,6]

# print(uno)
# print(dos)
# print(tres)
# print(cuatro)

# # Lista y Tuplas
tupla3 = (1, 2, 3, 4, 5, 6)
lista  = [10, 20, 30, 40]

# # Para generar nuevas tuplas. Esta funcion nos va a regresar un objeto de tipo zip. Por eso debemos convertirlo
resultado = zip(tupla3, lista) # Podemos agregar nuevas tuplas y listas
# resultado = tuple(resultado)  # Convertir el objeto tipo zip a tupla.
resultado = list(resultado)  # Convertir el objeto tipo zip a lista.
print(resultado)


