# class Circulo:
#     def __init__(self, radio):
#         self.radio = radio  # Es una variable de instancia

# circulo_a = Circulo(10)
# circulo_b = Circulo(20)

# print(circulo_a.radio)
# print(circulo_b.radio)

class Circulo:
    pi = 3.14159265         # Es una variable de clase
    def __init__(self, radio):
        self.radio = radio  # Es una variable de instancia

circulo_a = Circulo(10)
circulo_b = Circulo(20)

# print(circulo_a.pi)
# print(circulo_b.pi)

print(Circulo.pi)