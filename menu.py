import tkinter as tk
from tkinter import messagebox, simpledialog
from e_pila import InterfazGraficaPila
from e_cola import InterfazGraficaCola
from e_lista_circular import InterfazGraficaListaCircular
from e_lista_simplemente_enlazada import InterfazGraficaListaSimplementeEnlazada
from e_lista_doblemente_enlazada import InterfazGraficaListaDoblementeEnlazada
from e_lista_circular_doble import InterfazGraficaListaCircularDoble
# from e_arbol_binario import InterfazGraficaArbolBinario
from e_arbol_busqueda import InterfazGraficaArbolBusquedaBinaria

class InterfazGrafica:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Software Educativo - Estructura de Datos")

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
            ventana_pila = tk.Toplevel()
            self.interfaz_actual = InterfazGraficaPila(ventana_pila)
        elif opcion == "Cola":
            ventana_cola = tk.Toplevel()
            self.interfaz_actual = InterfazGraficaCola(ventana_cola)
        elif opcion == "Lista simplemente ligada":
            ventana_lista = tk.Toplevel()
            self.interfaz_actual = InterfazGraficaListaSimplementeEnlazada(ventana_lista)
        elif opcion == "Lista circular":
            ventana_lista_cir = tk.Toplevel()
            self.interfaz_actual = InterfazGraficaListaCircular(ventana_lista_cir)
        elif opcion == "Lista doblemente ligada":
            ventana_lista_doble = tk.Toplevel()
            self.interfaz_actual = InterfazGraficaListaDoblementeEnlazada(ventana_lista_doble)
        elif opcion == "Lista circular doble":
            ventana_lista_cir_doble = tk.Toplevel()
            self.interfaz_actual = InterfazGraficaListaCircularDoble(ventana_lista_cir_doble)
        elif opcion == "Árbol binario":
            ventana_arbol = tk.Toplevel()
            # self.interfaz_actual = InterfazGraficaArbolBinario(ventana_arbol)
        elif opcion == "Árbol de búsqueda":
            ventana_arbol_busq = tk.Toplevel()
            self.interfaz_actual = InterfazGraficaArbolBusquedaBinaria(ventana_arbol_busq)


ventana_principal = tk.Tk()
app = InterfazGrafica(ventana_principal)
ventana_principal.mainloop()