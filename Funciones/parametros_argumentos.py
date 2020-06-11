def crear_usuario(nombre, apellido, edad):
    return {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_completo': "{} {}".format(nombre, apellido),
        'edad': edad
    }

usuario1 = crear_usuario("Pedro", "Martinez", 16)
print(usuario1["nombre"])
print(usuario1["apellido"])
print(usuario1["edad"])