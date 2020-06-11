# range

# for valor in range(10): # rango de numeros de 0 al 9 la secuencia siempre inicia en cero
# 	print(valor)

# for rango in range(-10,11): # (Empieza en, termina en) en este caso
# 							# Empieza en -10 y termina en 10 no se tiene encuenta al 11.
# 	print(rango)

# for impares in range(1,101,2):  # (empieza,termina,saltos de 2 en 2)
# 	print(impares)

lista = [1,2,3,4,5,6]

# for indice in range(len(lista)):  # Menciona el indice con su respectivo valor
# 	print("indice", indice, "valor:", lista[indice])

# for indice, valor in enumerate(lista):  # Menciona el indice con su respectivo valor
# 	print("indice", indice, "valor:", valor)

# for i in range(1, 10):
# 	print('El valor de i es actualmente', i)

# print('Intruccion de ruptura break:')

# for i in range(1,6):
# 	if i ==3:
# 		break
# 	print('Dentro del ciclo. ', i)
# print('Fuera del ciclo')


# print('Intruccion de ruptura continue:')

# for i in range(1,6):
# 	if i ==3:
# 		continue
# 	print('Dentro del ciclo. ', i)
# print('Fuera del ciclo')