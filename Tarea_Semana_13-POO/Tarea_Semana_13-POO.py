
#Semana 13
#Tarea: Conceptos fundamentales de interfaces gráficas de usuario
#Tarea: Creación de una Aplicación GUI Básica

#Importamos la librería  tkinter
import tkinter as tk
from tkinter import messagebox

def agregar_dato():
    dato = entry_dato.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entry_dato.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")
print("Se imprimió un mensaje en pantalla")
def limpiar_lista():
    lista_datos.delete(0, tk.END)

#Creamos la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")
root.geometry("400x300")

#Creamos widgets
label_titulo = tk.Label(root, text="Ingrese Información:")
label_titulo.pack(pady=5)

entry_dato = tk.Entry(root, width=40)
entry_dato.pack(pady=5)

btn_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

lista_datos = tk.Listbox(root, width=50, height=10)
lista_datos.pack(pady=5)

btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

#Ejecutamos la aplicación
root.mainloop()

