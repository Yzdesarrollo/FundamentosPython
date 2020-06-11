diccionario = {} # Obtener un elemento del diccionario Mediante una llave

diccionario["nombre"] = "Carlos" # Para agregar una llave con su valor
print(diccionario)

diccionario.update[{"nombre":"Ramirez"}]
print(diccionario)

# valor = diccionario["nombre"]	 # Obtenemos un valor

# diccionario ["nombre"] = 90	# Si la llave existe dentro del diccionario
# 								# Entonces se reemplaza el valor
# 								# Si la llave no existe dentro del diccionario
# 								# Entonces se crea la llave
# 								# y se almacena el valor


# diccionario2 = {"a":1, "b":2, "c":3, "a":4} # No puden existir llaves duplicada
# # Y si lo hacemos la llave tomara el ultimo valor el cual se le asigno

# # resultado = "a" in diccionario2             # Si queremos saber si la llave existe dentro del diccionario sera un booleano.

# resultado = diccionario2.get("a")			# El metodo get nos retorna el valor y sino un none ponerle tambien un mensaje.

# resultado = diccionario2.setdefault("z", {}) # Si el elemento no existe lo creara en el diccionario

# # Para obtener todas las llaves del diccionario o los valores

# # resultado = diccionario2.keys()            # Retorna un objeto dict keys
# resultado = tuple(resultado) 				 # Convertir a tupla
# resultado = list(resultado) 
# print(resultado)

# # resultado = diccionario2.values()          # Retorna los valores de las llaves
# resultado = tuple(resultado) 				 # Convertir a tupla
# resultado = list(resultado) 
# # resultado = diccionario2.items()           # Retorna un objeto items y menciona las llaves y los valores
# resultado = tuple(resultado) 				 # Convertir a tupla
# resultado = list(resultado)

# print(len(diccionario2))				     # Menciona cuantos elementos hay en el diccionario
# print(diccionario2)
# print(diccionario)
# print(valor)
# print(resultado)

# # Eliminar una llave del diccionario
# del diccionario2 ["z"]

# Otro forma
# #diccionario2.pop("b")  
# valor = diccionario2.pop("b")       # Indica cuantos elementos han sido eliminados del dicccionario

# diccionario2 = {} # El diccionario vuelve a quedar vacio

# diccionario2.clear() # Otra forma de limpiar el diccionario

# print(valor)
# print(diccionario2)