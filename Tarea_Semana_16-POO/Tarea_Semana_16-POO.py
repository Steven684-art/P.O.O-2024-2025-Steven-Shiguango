
#(Semana 16) Tarea: Manejadores de eventos

#Tarea: Aplicación GUI para Gestión de Tareas con Atajos de Teclado

#Importamos tkinter (tk)
import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        self.tasks = []

        #Entrada de texto
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.add_task())

        #Botones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Añadir Tarea", command=self.add_task).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Marcar como Completada", command=self.complete_task).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task).pack(side=tk.LEFT, padx=5)

        #Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

        #Atajos de teclado
        self.root.bind("<Key>", self.tecla_presionada_global)

    def tecla_presionada_global(self, event):
        print(f"Tecla presionada: {event.keysym}")
        if self.entry != self.root.focus_get():
            tecla = event.keysym.lower()
            if tecla == "c":
                print("Acción: Marcar tarea como completada")
                self.complete_task()
            elif tecla in ["d", "delete"]:
                print("Acción: Eliminar tarea")
                self.delete_task()
            elif tecla == "escape":
                print("Acción: Salir de la aplicación")
                self.root.quit()

    def add_task(self):
        task = self.entry.get().strip()
        print(f"Intentando añadir tarea: '{task}'")
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
            print("Tarea añadida correctamente.")
        else:
            print("Advertencia: intento de añadir tarea vacía.")
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()
            print(f"Tarea en posición {index} marcada como completada: {self.tasks[index]}")
        except IndexError:
            print("Advertencia: ninguna tarea seleccionada para completar.")
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            print(f"Eliminando tarea en posición {index}: {self.tasks[index]}")
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            print("Advertencia: ninguna tarea seleccionada para eliminar.")
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display = f"✓ {task['text']}" if task['completed'] else f"{task['text']}"
            self.task_listbox.insert(tk.END, display)
            if task['completed']:
                self.task_listbox.itemconfig(tk.END, fg="gray")

#Ejecutamos la aplicaión
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
