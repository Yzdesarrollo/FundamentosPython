# break

titulo = 'Curso de Python 3'

# for caracter in titulo: # Para dividir los caracteres de la frase
#   print(caracter)

# for caracter in titulo:   # No muestra lo que esta de la letra P en adelante
#   if caracter == 'P':	  # cumple estrictamente la condicion
#   	break 
#   print(caracter)


for caracter in titulo:   # Muestra lo de mas,  menos la letra P
  if caracter == 'P':	    # cumple y salta la condicion
  	continue
  print(caracter)