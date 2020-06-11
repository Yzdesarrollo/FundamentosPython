def mostrar_mensaje(mensaje):
    mensaje = mensaje.title() #Local

    def mostrar():
        print(mensaje)

    return mostrar

nueva_funcion = mostrar_mensaje('Hola esto es closures')
nueva_funcion()