# cursos = ['python','java','javascript','php','c#','kotlin','Node','Dart']
# # curso = cursos[0] # Se puede usar numeros negativos

# # Si quiero listar los 3 primeros cursos de la lista tambien puedo omitir el cero(Solo cuando es cero)
# # sub = cursos[0:3] # Sublista Desde(indice):Hasta(conteo normal) desde python hasta javascript 
# # sub = cursos[3:7] # Sublista Desde(indice):Hasta(conteo normal) desde php hasta Node
# # sub = cursos[5:]  # Apartir de listar los siguientes
# # sub = cursos[:]   # Listar todos los elementos
# # sub = cursos[1:7:2] # En saltos de 2 en 2
# sub = cursos[::-1]  # El inverso de la lista.
# print(sub)

# numeros = [10, 5, 7, 2, 1]
# numeros[0]= 111     # Indexacion de un elemento o cambio
# print("Contenido de la lista: ", numeros)
# longitud = len(numeros)
# del numeros[1]
# numeros.append(500) # Agregar los elementos a la lista
# print('Contenido de la lista despues de eliminar: ', numeros)
# print('longitud de la lista es: ', longitud)
# print(numeros[-1])
# print(numeros[-2])

# miLista = []

# for i in range (5):
#     miLista.append (i + 1)

# print(miLista)

# miLista = [8, 10, 6, 2, 4]
# miLista.reverse()   # Organiza la lista
# print(miLista)

# miLista = [10, 8, 6, 4, 2]
# nuevaLista = miLista[1:3] # Sublista o rodaja
# print(nuevaLista)

# miLista = [10, 8, 6, 4, 2]
# nuevaLista = miLista[1:-1]
# print(nuevaLista)

miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[-1:1]
print(nuevaLista)