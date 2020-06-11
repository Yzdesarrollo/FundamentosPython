class Animal:
   def comer(self):
       print('Comiendo') 

   def domir(self):
       print('Durmiendo')

class Mascota:
    def fecha_adopcion(self, fecha):
      self.fecha_adopcion = fecha  

class Perro(Animal, Mascota):          # Clase Padre ya que perro hereda de Animal
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print('Ladrando')
    
    def dormir(self):
        print(self.nombre, 'esta durmiendo!')
        Animal.domir(self)
        print('No molestar')

class Gato(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    def ronronear(self):
        print('Ronroneando')

perro1 = Perro('Firulais')
perro1.domir()
