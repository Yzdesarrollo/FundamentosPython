class Triangulo:

    numero = 2

    @staticmethod           # Paso 1
    def area(base, altura): # Paso 2 pasar los parametros a la funcion
        return (base * altura) /  Triangulo.numero

resultado = Triangulo.area(10, 20)
print(resultado)
