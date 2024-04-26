import tkinter as tk
from e_pila import InterfazGraficaPila
from e_cola import InterfazGraficaCola
from e_lista_circular import InterfazGraficaListaCircular
from e_lista_simplemente_enlazada import InterfazGraficaListaSimplementeEnlazada
from e_lista_doblemente_enlazada import InterfazGraficaListaDoblementeEnlazada
from e_lista_circular_doble import InterfazGraficaListaCircularDoble
from e_arbol_busqueda import InterfazGraficaArbolBusquedaBinaria
class VentanaGeneral:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana General")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Ajustamos el tamaño de la ventana
        self.master.geometry("550x400")

        nombres_izquierda = ["Pila", "Cola", "Arbol binario", "Arbol de búsqueda"]
        nombres_derecha = ["Lista circular", "Lista circular doble", "Lista doblemente enlazada", "Lista simplemente enlazada"]

        # Creamos dos frames para organizar los botones
        self.frame_izquierda = tk.Frame(self.frame)
        self.frame_izquierda.pack(side=tk.LEFT, padx=20, pady=20)

        self.frame_derecha = tk.Frame(self.frame)
        self.frame_derecha.pack(side=tk.RIGHT, padx=20, pady=20)
        
        color_izq = "yellow"
        color_der = "yellow"

        # Creamos los botones para el lado izquierdo y los agregamos al frame izquierdo
        self.botones_izquierda = []
        for i, nombre in enumerate(nombres_izquierda):
            if i == 0:  # Para el primer botón
                boton = tk.Button(self.frame_izquierda, text=nombre, width=20, height=2, font=("Arial", 12), command=self.accion_boton_pila, bg=color_izq)
            elif i == 1:  # Para el segundo botón
                boton = tk.Button(self.frame_izquierda, text=nombre, width=20, height=2, font=("Arial", 12), command=self.accion_boton_cola, bg=color_izq)
            elif i == 2:  # Para el tercer botón
                boton = tk.Button(self.frame_izquierda, text=nombre, width=20, height=2, font=("Arial", 12), command=self.accion_boton_arbolbinario, bg=color_izq)
            elif i == 3:  # Para el cuarto botón
                boton = tk.Button(self.frame_izquierda, text=nombre, width=20, height=2, font=("Arial", 12), command=self.accion_boton_arbolbusqueda, bg=color_izq)
            else:
                boton = tk.Button(self.frame_izquierda, text=nombre, width=20, height=2, font=("Arial", 12))
            boton.pack(side=tk.TOP, padx=10, pady=10)
            self.botones_izquierda.append(boton)

        # Creamos los botones para el lado derecho y los agregamos al frame derecho
        self.botones_derecha = []
        for i, nombre in enumerate(nombres_derecha):
            if i == 0:  # Para el primer botón
                boton = tk.Button(self.frame_derecha, text=nombre, width=20, height=2, font=("Arial", 12), command=self.accion_boton_listacircular, bg=color_der)
            elif i == 1:  # Para el segundo botón
                boton = tk.Button(self.frame_derecha, text=nombre, width=20, height=2, font=("Arial", 12), command=self.accion_boton_listacirculardoble,bg=color_der )
            elif i == 2:  # Para el tercer botón
                boton = tk.Button(self.frame_derecha, text=nombre, width=22, height=2, font=("Arial", 12), command=self.accion_boton_listadoblementenlazada, bg=color_der)
            elif i == 3:  # Para el cuarto botón
                boton = tk.Button(self.frame_derecha, text=nombre, width=22, height=2, font=("Arial", 12), command=self.accion_boton_lspmntenlazada, bg=color_der)
            else:
                boton = tk.Button(self.frame_derecha, text=nombre, width=20, height=2, font=("Arial", 12))
            boton.pack(side=tk.TOP, padx=10, pady=10)
            self.botones_derecha.append(boton)

    # Función que se ejecutará al hacer clic en el primer botón de la lista de botones izquierda
    def accion_boton_pila(self):
        ventana_pila = tk.Toplevel()
        self.interfaz_actual = InterfazGraficaPila(ventana_pila)

    def accion_boton_cola(self):
        ventana_cola = tk.Toplevel()
        self.interfaz_actual = InterfazGraficaCola(ventana_cola)

    def accion_boton_arbolbinario(self):
        ventana_arbol = tk.Toplevel()
        # self.interfaz_actual = InterfazGraficaArbolBinario(ventana_arbol)

    def accion_boton_arbolbusqueda(self):
        ventana_arbol_busq = tk.Toplevel()
        self.interfaz_actual = InterfazGraficaArbolBusquedaBinaria(ventana_arbol_busq)

    def accion_boton_listacircular(self):
        ventana_lista_cir = tk.Toplevel()
        self.interfaz_actual = InterfazGraficaListaCircular(ventana_lista_cir)

    def accion_boton_listacirculardoble(self):
        ventana_lista_cir_doble = tk.Toplevel()
        self.interfaz_actual = InterfazGraficaListaCircularDoble(ventana_lista_cir_doble)

    def accion_boton_listadoblementenlazada(self):
        ventana_lista_doble = tk.Toplevel()
        self.interfaz_actual = InterfazGraficaListaDoblementeEnlazada(ventana_lista_doble)

    def accion_boton_lspmntenlazada(self):
        ventana_lista = tk.Toplevel()
        self.interfaz_actual = InterfazGraficaListaSimplementeEnlazada(ventana_lista)

def main():
    root = tk.Tk()
    app = VentanaGeneral(root)
    root.mainloop()

if __name__ == "__main__":
    main()
