# def suma(val1, val2, val3):
#     return val1 + val2 + val3

# resultado = suma(10, 20, 30)
# print(resultado)

# def suma(*args):  # Agrupa todos los argumentos en tupla
#     total = 0
#     print(args)
#     for valor in args:
#       total+=valor
#     return total

# resultado = suma(10, 20, 30, 40, 50, 60, 70)
# print(resultado)

# def usuarios_autenticados(**kargs): # Los agrupa en un diccionario
#     print(kargs)

# usuarios_autenticados(codi=True, facilito=False)

def combinacion(requerido, *args, **kargs): # valor requerido, tupla y un diccionario
    print(requerido)
    print(args)
    print(kargs)

combinacion("Valor requerido", 10, 20, valor_uno=True, valor_dos=False)