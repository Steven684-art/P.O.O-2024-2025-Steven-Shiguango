#Clase Producto: representa un producto individual en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        #Constructor para inicializar los atributos del producto
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre  #Nombre del producto
        self.cantidad = cantidad  #Cantidad disponible en el inventario
        self.precio = precio  #Precio unitario del producto

    #Métodos Getters para acceder a los atributos del producto
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    #Métodos Setters para modificar los atributos del producto
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    #Metodo especial para representar un producto como cadena (string)
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


#Clase Inventario: administra una lista de productos
class Inventario:
    def __init__(self):
        #Constructor para inicializar la lista de productos
        self.productos = []

    #Metodo para añadir un producto al inventario
    def añadir_producto(self, producto):
        #Verifica si el ID ya existe en el inventario
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        #Si el ID es único, añade el producto
        self.productos.append(producto)
        print("Producto añadido exitosamente.")

    # Metodo para eliminar un producto del inventario usando su ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)  #Elimina el producto encontrado
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto con ese ID no encontrado.")  #Si no se encuentra, muestra un mensaje de error

    # Metodo para actualizar la cantidad o el precio de un producto por su ID
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                #Actualiza los valores solo si se proporciona un nuevo dato
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto con ese ID no encontrado.")  #Si no se encuentra, muestra un mensaje de error

    #Metodo para buscar productos por nombre (pueden existir nombres similares)
    def buscar_producto(self, nombre):
        #Busca productos cuyo nombre contenga el texto ingresado (sin importar mayúsculas/minúsculas)
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("Resultados de búsqueda:")
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")  # Si no hay coincidencias, muestra un mensaje

    #Metodo para mostrar todos los productos en el inventario
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")  #Si no hay productos, muestra un mensaje
        else:
            print("Inventario:")
            for p in self.productos:
                print(p)  #Imprime cada producto utilizando el metodo __str__ de la clase Producto


#Interfaz de usuario en la consola
def menu():
    #Creamos una instancia de la clase Inventario
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
                #Solicita los datos del producto al usuario
                id_producto = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                #Crea una instancia de Producto y la añade al inventario
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                #Maneja errores en caso de que el usuario introduzca datos inválidos
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

                #Convierte las entradas solo si el usuario introdujo datos
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None

                #Actualiza el producto en el inventario
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