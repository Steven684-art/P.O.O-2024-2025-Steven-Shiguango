
#(Semana 11) Tarea: Fundamentos de colecciones

#Tarea: Sistema Avanzado de Gestión de Inventario


import json


class Producto:

    #Clase que representa un producto en el inventario.

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  #ID único
        self.nombre = nombre  #Nombre del producto
        self.cantidad = cantidad  #Cantidad disponible en inventario
        self.precio = precio  #Precio del producto

    def actualizar_cantidad(self, nueva_cantidad):
        #Actualiza la cantidad del producto
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        #Actualiza el precio del producto
        self.precio = nuevo_precio

    def __str__(self):
        #Retorna una representación en cadena del producto
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
     #Clase que gestiona el inventario de productos.


    def __init__(self):
        self.productos = {}  #Diccionario para almacenar productos con su ID como clave
        self.archivo = "inventario.json"  # Nombre del archivo de almacenamiento
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        #Agrega un nuevo producto al inventario.
        if producto.id_producto in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        #Elimina un producto del inventario por su ID.
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        #Actualiza la cantidad y/o el precio de un producto existente.
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_inventario(self):
        #Muestra todos los productos en el inventario.
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_en_archivo(self):
        #Guarda el inventario en un archivo JSON.
        with open(self.archivo, "w") as f:
            json.dump({id_prod: vars(prod) for id_prod, prod in self.productos.items()}, f, indent=4)

    def cargar_desde_archivo(self):
        #Carga los productos del archivo JSON al iniciar el programa.
        try:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                self.productos = {id_prod: Producto(**prod) for id_prod, prod in datos.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}


#Interfaz de usuario

def menu():
    #Muestra el menú de opciones y gestiona la interacción con el usuario.
    inventario = Inventario()
    while True:
        print("\n Menú de Inventario ")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Mostrar inventario")
        print("5. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            #Solicita los datos para agregar un producto
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            #Solicita el ID del producto a eliminar
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            #Solicita los datos para actualizar un producto
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje vacío si no cambia): ")
            precio = input("Ingrese nuevo precio (deje vacío si no cambia): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)

        elif opcion == "4":
            #Muestra los productos en el inventario
            inventario.mostrar_inventario()

        elif opcion == "5":
            #Guarda el inventario y sale del sistema
            inventario.guardar_en_archivo()
            print("Inventario guardado. Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
