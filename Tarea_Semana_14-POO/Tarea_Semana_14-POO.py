
#Tarea: Creación de una Aplicación de Agenda Personal

#Importamos tkinter (tk)
import tkinter as tk
from tkinter import ttk, messagebox
#Importamos tkcalendar
from tkcalendar import DateEntry  #Importación de DateEntry para la selección de fecha


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        #Frame para la entrada de datos
        self.frame_inputs = ttk.Frame(root, padding="10")
        self.frame_inputs.grid(row=0, column=0, sticky="ew")

        #Etiqueta y entrada para la fecha con DateEntry
        ttk.Label(self.frame_inputs, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame_inputs, width=12, background='darkblue', foreground='white',
                                    borderwidth=2, date_pattern='dd/mm/yyyy')
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        #Etiqueta y entrada para la hora
        ttk.Label(self.frame_inputs, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
        self.time_entry = ttk.Entry(self.frame_inputs, width=10)
        self.time_entry.grid(row=0, column=3, padx=5, pady=5)

        #Etiqueta y entrada para la descripción
        ttk.Label(self.frame_inputs, text="Descripción:").grid(row=0, column=4, padx=5, pady=5)
        self.desc_entry = ttk.Entry(self.frame_inputs, width=30)
        self.desc_entry.grid(row=0, column=5, padx=5, pady=5)

        #Botón para agregar eventos
        self.add_button = ttk.Button(self.frame_inputs, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=0, column=6, padx=5, pady=5)

        #Frame para mostrar los eventos
        self.frame_events = ttk.Frame(root, padding="10")
        self.frame_events.grid(row=1, column=0, sticky="nsew")

        #Tabla para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_events, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(expand=True, fill='both')

        #Frame para botones de acción
        self.frame_actions = ttk.Frame(root, padding="10")
        self.frame_actions.grid(row=2, column=0, sticky="ew")

        #Botón para eliminar eventos
        self.delete_button = ttk.Button(self.frame_actions, text="Eliminar Evento Seleccionado",
                                        command=self.delete_event)
        self.delete_button.pack(side="left", padx=5, pady=5)

        #Botón para salir de la aplicación
        self.exit_button = ttk.Button(self.frame_actions, text="Salir", command=root.quit)
        self.exit_button.pack(side="right", padx=5, pady=5)

    def add_event(self):
        #Añadimos un nuevo evento a la tabla si los campos son válidos
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Entrada inválida", "Por favor, complete todos los campos.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def delete_event(self):
        #Eliminamos el evento seleccionado después de confirmar la acción
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selección inválida", "Por favor, seleccione un evento para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de que desea eliminar este evento?")
        if confirm:
            self.tree.delete(selected_item)

print("El código se esta ejecutando")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
