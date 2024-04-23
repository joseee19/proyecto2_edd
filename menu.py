import tkinter as tk
from tkinter import messagebox, simpledialog
from e_pila import InterfazGraficaPila
from e_cola import InterfazGraficaCola
from e_lista_simplemente_enlazada import InterfazGraficaListaSimplementeEnlazada

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
            self.interfaz_actual = InterfazGraficaPila()
        elif opcion == "Cola":
            self.interfaz_actual = InterfazGraficaCola()
        elif opcion == "Lista simplemente ligada":
            self.interfaz_actual = InterfazGraficaListaSimplementeEnlazada()
        elif opcion == "Lista circular":
            messagebox.showinfo("Lista circular", "Función en construcción.")
        elif opcion == "Lista doblemente enlazada":
            messagebox.showinfo("Lista doblemente enlazada", "Función en construcción.")
        elif opcion == "Lista circular doble":
            messagebox.showinfo("Lista circular doble", "Función en construcción.")
        elif opcion == "Árbol binario":
            messagebox.showinfo("Árbol binario", "Función en construcción.")
        elif opcion == "Árbol de búsqueda":
            messagebox.showinfo("Árbol de búsqueda", "Función en construcción.")

# Crear la ventana principal de la aplicación
ventana_principal = tk.Tk()
app = InterfazGrafica(ventana_principal)
ventana_principal.mainloop()