import os


class Producto:
    "Clase que representa un producto en el inventario."

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_string(line):
        """Convierte una línea del archivo en un objeto Producto."""
        try:
            id_producto, nombre, cantidad, precio = line.strip().split(',')
            return Producto(int(id_producto), nombre, int(cantidad), float(precio))
        except ValueError:
            print(f"Error: No se pudo procesar la línea -> {line}")
            return None


class Inventario:
    """Clase que maneja la lista de productos y la persistencia en archivo."""

    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()
    #Cargar desde archivo
    def cargar_desde_archivo(self):
        """Carga productos desde el archivo de texto si existe."""
        if not os.path.exists(self.archivo):
            open(self.archivo, "w").close()  # Crea el archivo vacío si no existe

        try:
            with open(self.archivo, "r") as f:
                lineas = f.readlines()
                self.productos = [Producto.from_string(line) for line in lineas if
                                  Producto.from_string(line) is not None]
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al acceder al archivo: {e}")
            self.productos = []
    #Guardar en arcivo
    def guardar_en_archivo(self):
        """Guarda los productos en el archivo de texto."""
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos:
                    f.write(str(producto) + "\n")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    # Metodo para añadir un producto al inventario
    def añadir_producto(self, producto):
        """Añade un producto al inventario y lo guarda en el archivo."""
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto añadido exitosamente.")

    # Metodo para eliminar un producto del inventario usando su ID
    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto con ese ID no encontrado.")

    #Metodo para actualizar la cantidad o el precio de un producto por su ID
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad o el precio de un producto."""
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto con ese ID no encontrado.")

    #Metodo para buscar productos por nombre (pueden existir nombres similares)
    def buscar_producto(self, nombre):
        """Busca productos por nombre."""
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("Resultados de búsqueda:")
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    # Metodo para mostrar todos los productos en el inventario
    def mostrar_productos(self):
        """Muestra todos los productos del inventario."""
        if not self.productos:
            print("El inventario está vacío.") #Si no hay productos, muestra un mensaje
        else:
            print("Inventario:")
            for p in self.productos:
                print(p) #Imprime cada producto utilizando el metodo __str__ de la clase Producto

#Interfaz de usuario en la consola
def menu():
    """Menú interactivo del sistema de gestión de inventarios."""
    # Creamos una instancia de la clase Inventario
    inventario = Inventario()
    while True:
        #Imprime el menú de opciones
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        #Solicita al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            #Opción para añadir un producto
            try:
                #Solicita los datos del producto al uario
                id_producto = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Entrada no válida. Por favor, intente de nuevo.")

        elif opcion == "2":
            #Opción para eliminar un producto
            try:
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Error: Entrada no válida. Por favor, intente de nuevo.")

        elif opcion == "3":
            #Opción para actualizar un producto
            try:
                id_producto = int(input("Ingrese el ID del producto a actualizar: "))
                print("Ingrese los nuevos valores (deje en blanco si no desea cambiar):")
                nueva_cantidad = input("Nueva cantidad: ")
                nuevo_precio = input("Nuevo precio: ")
                # Convierte las entradas solo si el usuario introdujo datos
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None
                # Actualiza el producto en el inventario
                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("Error: Entrada no válida. Por favor, intente de nuevo.")

        elif opcion == "4":
            #Opción para buscar productos por nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            #Opción para mostrar todos los productos
            inventario.mostrar_productos()

        elif opcion == "6":
            #Opción para salir del sistema
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            #Mensaje de error si el usuario selecciona una opción no válida
            print("Opción no válida. Por favor, intente de nuevo.")

#Punto de entrada del programa
if __name__ == "__main__":
    #Llama a la función del menú para iniciar el sistema
    menu()
