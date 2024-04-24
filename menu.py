import tkinter as tk
from tkinter import messagebox, simpledialog
from e_pila import InterfazGraficaPila
from e_cola import InterfazGraficaCola
from e_lista_simplemente_enlazada import InterfazGraficaListaSimplementeEnlazada
from e_lista_circular import InterfazGraficaListaCircular
from e_lista_doblemente_enlazada import InterfazGraficaListaDoblementeEnlazada

class InterfazGrafica:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Software Educativo - Estructuras de Datos")

        self.frame_menu = tk.Frame(ventana)
        self.frame_menu.pack()

        self.etiqueta_seleccion = tk.Label(self.frame_menu, text="Seleccione una estructura de datos:")
        self.etiqueta_seleccion.grid(row=0, column=0)

        self.opciones = ["Pila", "Cola", "Lista simplemente ligada", "Lista circular",
                         "Lista doblemente enlazada", "Lista circular doble", 
                         "Árbol binario", "Árbol de búsqueda"]

        self.menu = tk.OptionMenu(self.frame_menu, tk.StringVar(), *self.opciones, command=self.mostrar_interfaz)
        self.menu.grid(row=0, column=1)

        self.interfaz_actual = None

    def mostrar_interfaz(self, opcion):
        if self.interfaz_actual:
            self.interfaz_actual.destroy()  # Cerrar la ventana actual si existe

        if opcion == "Pila":
            self.interfaz_actual = InterfazGraficaPila(self.ventana)
        elif opcion == "Cola":
            self.interfaz_actual = InterfazGraficaCola(self.ventana)
        elif opcion == "Lista simplemente ligada":
            self.interfaz_actual = InterfazGraficaListaSimplementeEnlazada(self.ventana)
        elif opcion == "Lista circular":
            self.interfaz_actual = InterfazGraficaListaCircular(self.ventana)
        elif opcion == "Lista doblemente enlazada":
            self.interfaz_actual = InterfazGraficaListaDoblementeEnlazada(self.ventana)

# Crear la ventana principal de la aplicación
ventana_principal = tk.Tk()
app = InterfazGrafica(ventana_principal)
ventana_principal.mainloop()