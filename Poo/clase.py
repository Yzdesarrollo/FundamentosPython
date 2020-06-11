# class Usuario:
#     pass

# Pedro = Usuario()
# Rodriguez = Usuario()

# print(type(Pedro))

# class Usuario:
#     def saludo(self, nombre):
#         print('Hola, soy un usuario' + nombre)

# Pedro = Usuario()
# Rodriguez = Usuario()

# Pedro.saludo(' Pedro')
# Rodriguez.saludo(' Rodriguez')

# class Usuario:
#     def saludo(self, nombre):
#         return 'Hola, soy un usuario' + nombre

# Pedro = Usuario()
# Rodriguez = Usuario()

# print(Pedro.saludo(' Pedro'))
# print(Rodriguez.saludo(' Rodriguez'))

# class Usuario:
#     def saludo(self, nombre):
#         return 'Hola, soy un usuario' + nombre

#     def mostrar_username(self):
#         print(self.username)

# Pedro = Usuario()
# Pedro.username = 'Pedro'
# Pedro.correo = 'pedro@gmail.com'

# Rodriguez = Usuario()
# Rodriguez.username = 'Rodriguez'
# Rodriguez.correo = 'Rodriguez@gmail.com'

# Pedro.mostrar_username()
# Rodriguez.mostrar_username()

# class Usuario:
#     def saludo(self, nombre):
#         return 'Hola, soy un usuario' + nombre

#     def mostrar_username(self):
#         print(self.username)

#     def mostrar_nombre(self):
#         print(self.nombre)

#     def crear_nombre(self, nombre):
#         self.nombre = nombre

# Pedro = Usuario()
# Pedro.username = 'Pedro'
# Pedro.correo = 'pedro@gmail.com'

# Rodriguez = Usuario()
# Rodriguez.username = 'Rodriguez'
# Rodriguez.correo = 'Rodriguez@gmail.com'

# Pedro.crear_nombre('Andres')
# Pedro.mostrar_nombre()

class Usuario:

    def __init__(self, username='', correo='', nombre=''):
        self.username = username
        self.correo = correo
        self.nombre = nombre

    def saludo(self):
        return 'Hola, soy un usuario' + self.nombre

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)


Pedro = Usuario('dres', 'andres@gmail.com', ' Andres')
Rodriguez = Usuario()

resultado = Pedro.saludo()
print(resultado)
