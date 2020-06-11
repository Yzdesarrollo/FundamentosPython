#print('Cual es tu nombre?')
nombre = input('Cual es tu nombre?\n')

#print('Cual es tu edad?')
edad = int(input('Cual es tu edad?\n'))       # Convertir a entero

#print('Cual es tu peso?')
peso = float(input('Cual es tu peso?\n')) 	  # Convertir a float

#print('Estas autorizado?')
autorizado = input('Estas autorizado (si/no)?\n') == 'si'

print('Hola', nombre)
print('Edad', edad)
print('Peso', peso)
print('Autorizado', autorizado)