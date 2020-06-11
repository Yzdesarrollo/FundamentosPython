texto = "curso de Python 3"

resultado = texto.capitalize()  # Pone la primera letra en Mayuscula

resultado = texto.swapcase()    # Pone las letras que estan minusculas las pone en mayuscula y viceversa

resultado = texto.upper() 		# Pone todas las letras en mayusculas 

resultado = texto.lower() 		# Pone todas las letras en minusculas

resultado = texto.title()		# Pone la primera letra de cada palabra en Mayuscula Formato de titulo Curso De Python 3

resultado = texto.replace("Python", "Java", 1)	# Remplaza palabras La 1ra es la que se quiere reemplazar y la segunda la nueva y si que quiero que se reemplace pongo 1 si quiero que se reemplace una sola vez.

resultado = texto.strip()       # Quita los espacios

print(resultado.isupper())      # Si queremos saber si hay mayusculas retorna un valor booleano
print(resultado.islower())		# Si queremos saber si hay minusculas retorna un valor booleano

print(resultado)

# Otros formatos
curso = "Python"
version = "3"

# resultado = "Curso de %s %s" %(curso, version)  # Reemplaza las varibles
# Otra forma
# resultado = "Curso de {} {}".format(curso, version)
# # O tambien
# resultado = "Curso de {a} {b}".format(a=curso, b=version)


print(resultado)