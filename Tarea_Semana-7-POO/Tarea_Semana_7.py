#Ejercicios de los métodos constructor y destructor

class Persona:  #Creamos la clase persona
 def __init__(self, nombre, edad):  #Creamos el constructor en el  cual vamos a colocar atributos

  self.nombre = nombre
  self.edad = edad
  print(f"Nueva persona creada: {self.nombre}")  #Imprimimos que una nueva persona se creo

 def __del__(self):  #Creamos el destructor que va a eliminar a la persona cuando lo utilicemos

  print(f"{self.nombre} fue eliminado")

 def presentarse(self):  #Creamos un metodo para presentarse

  print(f"Hola, soy {self.nombre} y tengo {self.edad} años")  #Imprimimos la presentación


#Uso de la clase

#Creamos dos objetos y colocamos los parámetros de la clase persona
persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)

#Usamos el metodo
persona1.presentarse()
persona2.presentarse()









