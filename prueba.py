import tkinter as tk
from e_pila import InterfazGraficaPila
class VentanaGeneral:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana General")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Ajustamos el tamaño de la ventana
        self.master.geometry("500x400")

        nombres_izquierda = ["Pila", "Cola", "Arbol binario", "Botón D"]
        nombres_derecha = ["Botón E", "Botón F", "Botón G", "Botón H"]

        # Creamos dos frames para organizar los botones
        self.frame_izquierda = tk.Frame(self.frame)
        self.frame_izquierda.pack(side=tk.LEFT, padx=20, pady=20)

        self.frame_derecha = tk.Frame(self.frame)
        self.frame_derecha.pack(side=tk.RIGHT, padx=20, pady=20)

        # Creamos los botones para el lado izquierdo y los agregamos al frame izquierdo
        self.botones_izquierda = []
        for i, nombre in enumerate(nombres_izquierda):
            if i == 0:  # Para el primer botón
                boton = tk.Button(self.frame_izquierda, text=nombre, width=20, height=2, font=("Arial", 12), command=self.accion_boton_pila)
            else:
                boton = tk.Button(self.frame_izquierda, text=nombre, width=20, height=2, font=("Arial", 12))
            boton.pack(side=tk.TOP, padx=10, pady=10)
            self.botones_izquierda.append(boton)

        # Creamos los botones para el lado derecho y los agregamos al frame derecho
        self.botones_derecha = []
        for i, nombre in enumerate(nombres_derecha):
            boton = tk.Button(self.frame_derecha, text=nombre, width=20, height=2, font=("Arial", 12))
            boton.pack(side=tk.TOP, padx=10, pady=10)
            self.botones_derecha.append(boton)

    # Función que se ejecutará al hacer clic en el primer botón de la lista de botones izquierda
    def accion_boton_pila(self):
        ventana_pila = tk.Toplevel()
        self.interfaz_actual = InterfazGraficaPila(ventana_pila)

def main():
    root = tk.Tk()
    app = VentanaGeneral(root)
    root.mainloop()

if __name__ == "__main__":
    main()
