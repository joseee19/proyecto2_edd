import tkinter as tk
from tkinter import messagebox
from e_pila import InterfazPila

class InterfazGrafica:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Software Educativo - Estructuras de Datos")

        self.frame_menu = tk.Frame(ventana)
        self.frame_menu.pack()

        self.etiqueta_seleccion = tk.Label(self.frame_menu, text="Seleccione una estructura de datos:")
        self.etiqueta_seleccion.grid(row=0, column=0)

        self.opciones = ["Pila", "Cola", "Lista simplemente ligada", "Lista circular", "Lista doblemente ligada", "Lista circular doble", "Árbol binario", "Árbol de búsqueda"]

        self.menu = tk.OptionMenu(self.frame_menu, tk.StringVar(), *self.opciones, command=self.mostrar_interfaz)
        self.menu.grid(row=0, column=1)

        self.interfaz_actual = None

    def mostrar_interfaz(self, opcion):
        if opcion == "Pila":
            self.interfaz_actual = InterfazPila(self.ventana)
        elif opcion == "Cola":
            messagebox.showinfo("Cola", "Función en construcción.")
        # Aquí se agregarían las otras opciones de estructuras de datos

# Crear la ventana principal de la aplicación
ventana_principal = tk.Tk()
app = InterfazGrafica(ventana_principal)
ventana_principal.mainloop()