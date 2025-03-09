
#Semana 12
# Tarea: Utilización de colecciones para la mejora de rendimiento
#Tarea: Sistema de Gestión de Biblioteca Digital

import json

#Clase libro
class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str, prestado=False):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = prestado

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "isbn": self.isbn,
            "prestado": self.prestado
        }

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f'Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}, Estado: {estado}'

#Clase usuario
class Usuario:
    def __init__(self, nombre: str, user_id: str):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def __str__(self):
        return f'Usuario: {self.nombre}, ID: {self.user_id}'

#Clase biblioteca
class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json'):
        self.archivo_json = archivo_json
        self.libros = self.cargar_libros()
        self.usuarios = {}
        self.historial_prestamos = []

    def cargar_libros(self):
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except FileNotFoundError:
            return {}

    def guardar_libros(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_libros()
        print(f'Libro añadido: {libro}')

    def prestar_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro and not libro.prestado:
            libro.prestado = True
            self.guardar_libros()
            print(f"Libro {isbn} prestado con éxito.")
        else:
            print("Libro no disponible para préstamo.")

    def devolver_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro and libro.prestado:
            libro.prestado = False
            self.guardar_libros()
            print(f"Libro {isbn} devuelto con éxito.")
        else:
            print("Error en la devolución del libro.")

    def mostrar_libros(self):
        for libro in self.libros.values():
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")

#Menú de funcionalidades
def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n Sistema de Gestión de Biblioteca Digital ")
        print("1. Añadir libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.añadir_libro(Libro(titulo, autor, categoria, isbn))
        elif opcion == '2':
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(isbn)
        elif opcion == '3':
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(isbn)
        elif opcion == '4':
            biblioteca.mostrar_libros()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    menu()

