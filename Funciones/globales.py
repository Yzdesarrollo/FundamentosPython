animal= 'León' # Variables globales las que estan fuera de la funcion.

def mostrar_animal():
    global animal # Variables globales dentro de una funcion.
    animal = 'Ballena' # Variables locales variable que solo se puede acceder dentro de la funcion 
    print(animal)

mostrar_animal()
print(animal)