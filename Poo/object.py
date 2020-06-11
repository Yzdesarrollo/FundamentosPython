# Primera forma de crear una clase
class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):         # Para no ver la direcion en memoria
        return self.nombre

class Pato(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

gato = Gato('Bigotes')
gato.edad = 5
pato = Pato('Lucas')

# print(gato) # <__main__.Gato object at 0x00000206C7A46CA0> direccion en memoria               
# print(pato) #  <__main__.Pato object at 0x00000206C7A84340>

print(gato.__dict__) # Visualizamos un diccionario con lo atributos de nuestro objeto
print(pato.__dict__)