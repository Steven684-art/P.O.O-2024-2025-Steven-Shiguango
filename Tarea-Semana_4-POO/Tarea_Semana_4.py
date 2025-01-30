class Libro: #Creamos la clase libro
    def __init__(self, titulo, autor, editorial):  #Creamos un constructor  y iniciamos atributos
        self.titulo = titulo
        self.autor = autor
        self.isbn = editorial
        self.disponible = True  # Inicialmente, el libro está disponible

    def prestar(self):  #Creamos el metodo prestar
        if self.disponible:  #si esta disponible els verdadero luego pasara a falso
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado.")  #Imrpimimos que el libro esta prestado
            return True  #Retornamos un true, si es veradero volvera a estar disponible
        else:
            print(f"Libro '{self.titulo}' no disponible.")  # Si no esta disponible el libro, retorna un falso
            return False #Retornamos un false y si disponible es falso, nos mostrara el mismo mensaje

    def devolver(self):  #Creamos un metodo devolver
        if not self.disponible: #Si disponible es falso, luego sera veradero
            self.disponible = True
            print(f"Libro '{self.titulo}' devuelto.")  #Imprimimos que se devuelve
        else:
            print(f"Libro '{self.titulo}' ya está disponible.")

    def mostrar_info(self): #Creamos otro metodo que nos va a  mostrar la información del libro(título,autor,editorail y disponibilidad)
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Editorial: {self.isbn}")
        print(f"Disponibilidad: {'Disponible' if self.disponible else 'Prestado'}")  #Si disponible es true devuelve siponible si es false deuvuelve prestado



# Creamos un objeto y lo instanciamos con la clase Libro
libro1 = Libro("El tiempo", "Jorge","casa_saenz")

libro1.mostrar_info()  # Mostrar información inicial del libro
libro1.prestar()       # Prestar el libro
libro1.mostrar_info()  # Mostrar información después de prestar
libro1.devolver()      # Devolver el libro
libro1.mostrar_info()  # Mostrar información después de devolver
