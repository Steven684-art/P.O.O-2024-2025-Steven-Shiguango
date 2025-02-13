from abc import ABC, abstractmethod  #Importamos la clase abstracta
import math  #Importamos math


# Clase abstracta para las figuras
class Figura(ABC):  #Creamos figura como clase abstracta

    @abstractmethod  #Decoramos para que sea una clase abstracta
    def calcular_area(self):  #creamos el metodo calcular area y por el momento un pass por que no hacemos nada
        pass

    @abstractmethod #Volvemos a decorar el metodo
    def mostrar_datos(self):  #Creamos el metodo mostrar_datos  y de igual colocamos un pass
        pass

#La clase abstracta nos permite que sea obligatorio utilizar estos metodos (calcular_area, mostrar_datos)
# Creamos la calse circulo
class Circulo(Figura):  #Creamos la clase ciruclo y heredamos de la clase padre
    def __init__(self, radio):  #Iniciamos un construcor y colocamos los atributos
        self.radio = radio

    def calcular_area(self):  #Creamos el metodo abstracto y retornamos una operacion
        return math.pi * self.radio ** 2

    def mostrar_datos(self): #De igual manera utilizamos el metodo abstracto y retornamos la información
        return f"Círculo - Radio: {self.radio}, Área: {self.calcular_area():.2f}"


# Clase para el rectángulo
class Rectangulo(Figura): #Creamos otra clase hija y herdemaos de la clase padre
    def __init__(self, base, altura): #Creamos el constructor y colocamos los atributos
        self.base = base
        self.altura = altura

    def calcular_area(self): #Utilizamos el metodo para retornar las operaciones
        return self.base * self.altura

    def mostrar_datos(self): #Lo mismo con este metodo, para ver la información
        return f"Rectángulo - Base: {self.base}, Altura: {self.altura}, Área: {self.calcular_area():.2f}"


# Creamos la clase triangulo y herdamos de la clase padre
class Triangulo(Figura):
    def __init__(self, base, altura):   #Creamos el constructor y colocamos los atributos
        self.base = base
        self.altura = altura

    def calcular_area(self): #Utilizamos el metodo para retornar las operaciones
        return (self.base * self.altura) / 2

    def mostrar_datos(self): #Lo mismo con este metodo, para ver la información
        return f"Triángulo - Base: {self.base}, Altura: {self.altura}, Área: {self.calcular_area():.2f}"





#Instanciamos el objeto con la clase
figura1 = Circulo(2.54)
#Instanciamos un segundo objeto
figura2 = Rectangulo(5,10)


print(figura1.calcular_area()) #Imprimimos el area del circulo
print(figura1.mostrar_datos())  #Mostramos los datos

print(figura2.calcular_area()) #Imprimimos el area del rectangulo
print(figura2.mostrar_datos())  #Mostramos los datos

