class Animal: #Creamos la clase animal
    def __init__(self, nombre):  #Creamos el constructor y utilizamos el polimorfismo
        self.__nombre = nombre

    def get_nombre(self):  #Creamos el metodo get para ver el nombre
        return self.__nombre

    def set_nombre(self, nombre): #Creamos el metodo set para editar
        self.__nombre = nombre

    def hacer_sonido(self):  #Creamos el metodo para hacer el sonido
        print("El animal hace un sonido distinto.")


class Perro(Animal):  #Creamos la clase perro y va a heredar de animal los metodos
    def __init__(self, nombre, raza):  #Creamos el constructor y agregamos un nuevo atributo
        super().__init__(nombre)  #Con el metodo super traemos el nombre de la clase animal
        self.__raza = raza  #Encapsulamos el atributo raza

    def get_raza(self): # Creamos un metodo get de raza para visualizar
        return self.__raza

    def set_raza(self, raza): #Creamos el metodo set de raza para editar
        self.__raza = raza

    def hacer_sonido(self):  #Creamos el metodo y sobreescribimos la acción que realiza
        print(f"El perro {self.get_nombre()} ladra. guau guau !!") #Imprimimos que ladra


# Crear instancias de las clases
animal_distinto = Animal("Animal distinto")
perro = Perro("Tobby", "Labrador")

# Probar la funcionalidad de las clases
print(animal_distinto.get_nombre())  # Salida: "Animal distinto"
#Llamamos a nuestr objeto y llamamos un metodo
animal_distinto.hacer_sonido()  # Salida: "El animal hace un sonido genérico."

print(perro.get_nombre()) #Visualizamos con el metodo get asi este encapsulado el atributo nombre
print(perro.get_raza())  # Salida: "Labrador"
perro.hacer_sonido()  # Salida: "El perro tobby ladra."
