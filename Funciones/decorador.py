#a, b, c
#a(b) -> c

def decorador(funcion):
    # pass no hace nada
    def nueva_funcion():
        print('Podemos agregar codigo antes')
        funcion()
        print('Podemos agregar codigo despues')
    return nueva_funcion

@decorador
def funcion_a_decorar():
    print('Este es ua funcion a decorar')

funcion_a_decorar()
