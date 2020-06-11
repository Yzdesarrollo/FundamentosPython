# Ciclos

# # While
# numero = 123456789
# contador = 0

# while numero >= 1:
# 	contador +=1
# 	numero = numero / 10
# print('La cantidad de digitos del numero es ', contador) # es 9

# For
# numeros = [1,2,3,4,5,6,7,8,9,10]

# for number in numeros: # number 1,2,3...
# 	print(number)

# diccionario = {'a':1, 'b':2}

# for llave in diccionario:
# 	print(llave)

# valores = ((10, 20, 30), ['strings', 'strings'], (True, False, True))

# for valor1, valor2, valor3 in valores:
# 	print(valor1, valor2, valor3)

# Ej Suma de numeros del 1 al 6

# 1. Comenzar suma en cero antes del ciclo esto se le llama ACUMULADOR
# 2. Definiremos otra variable (i) donde comenzaremos en el valor de uno i = 1 CONTADOR SUMA = SUMA + i
# 3. Notaremos que el valor de la suma es 1 ya que suma=0+1 i = i + 1

# #N = 6 # Valor limite
# N = int(input('ingrese un numero\n')) # mostrar la suma de n numeros
# SUMA = 0 # Acumulador
# i = 1 # Contador

# while i<=N:
# 	SUMA = SUMA + i
# 	i = i + 1
# print('La suma de los numeros hasta ', N,'es: ',SUMA)

# # Tabla de multiplicar

# n = int(input('Ingrese la tabla que desea ver: \n'))
# i = 1 # Contador
# a = 10 # Acumulador
# while i <= a:
# 	print(n, 'X', i, '=', n*i)
# 	i = i + 1
# print('tabla de multiplicar del: ', n)

# # Generar los N primeros numeros de forma ascendente

# num = int(input('Ingrese un numero'))
# i = 1
# while i <= num:
# 	print(i)
# 	i = i + 1

# # Generar los N primeros numeros de forma ascendente

# num = int(input('Ingrese un numero'))
# i = n
# while i >= 1:
# 	print(i)
# 	i = i - 1


# contador = 5 # Ciclo infinito

# while contador:
# 	print("Dentro del ciclo: ", contador)
# 	contador += 1
# print("Fuera del ciclo", contador)


i = 5
while i < 5:
    print(i)
    i += 1
else:
    print('else:', i)





