#Semana 15
#Tarea: Conceptos fundamentales de manejo de eventos
#Aplicación GUI de Lista de Tareas


#Importamos tkinter (tk)
import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")

def marcar_completada():
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        task_listbox.delete(selected_index)
        task_listbox.insert(selected_index, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")

def eliminar_tarea():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

def agregar_tarea_enter(event):
    agregar_tarea()

def cerrar_ventana():
    root.destroy()

#Creamos la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

#Campo de entrada
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)
task_entry.bind("<Return>", agregar_tarea_enter)  #Agregamos tarea con Enter

#Lista de tareas
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

#Botones
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Añadir Tarea", command=agregar_tarea)
add_button.grid(row=0, column=0, padx=5)

complete_button = tk.Button(button_frame, text="Marcar como Completada", command=marcar_completada)
complete_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=eliminar_tarea)
delete_button.grid(row=0, column=2, padx=5)

close_button = tk.Button(root, text="Finalizar", command=cerrar_ventana)
close_button.pack(pady=10)

print("Código fuente ejecutándose...")

#Ejecutamos la aplicación
root.mainloop()
