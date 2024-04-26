import tkinter as tk
from e_pila import InterfazGraficaPila

class VentanaMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Menú")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Ajustamos el tamaño de la ventana
        self.master.geometry("300x200")

        self.label = tk.Label(self.frame, text="Estructura de Datos", font=("Arial", 14))
        self.label.pack(pady=20)

        self.boton_entrar = tk.Button(self.frame, text="Entrar", command=self.abrir_ventana_botones)
        self.boton_entrar.pack()

    def abrir_ventana_botones(self):
        # Cerramos la ventana de menú
        self.master.destroy()

        # Abrimos la ventana con botones
        root = tk.Tk()
        app = VentanaConBotones(root)
        root.mainloop()

class VentanaConBotones:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana con Botones")

        # Cambiamos el color de fondo de la ventana
        self.master.configure(bg="yellow")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Ajustamos el tamaño de la ventana
        self.master.geometry("500x400")

        # Creamos dos frames para organizar los botones
        self.frame_izquierda = tk.Frame(self.frame)
        self.frame_izquierda.pack(side=tk.LEFT, padx=20, pady=20)

        self.frame_derecha = tk.Frame(self.frame)
        self.frame_derecha.pack(side=tk.RIGHT, padx=20, pady=20)

        # Creamos los botones para el lado izquierdo y los agregamos al frame izquierdo
        self.botones_izquierda = []
        for i in range(4):
            nombre_boton = f"Botón {i+1}"
            if i == 0:
                nombre_boton = "Pila"
                # Asignamos una acción al primer botón
                comando_boton = self.pila
            elif i == 1:
                nombre_boton = "Cola"
            elif i == 2:
                nombre_boton = "Arbol binario"
            elif i == 3:
                nombre_boton = "Arbol de búsqueda"
            boton_texto = tk.StringVar(value=nombre_boton)
            boton = tk.Button(self.frame_izquierda, textvariable=boton_texto, width=20, height=2, font=("Arial", 12), command=comando_boton)
            boton.pack(side=tk.TOP, padx=10, pady=10)
            self.botones_izquierda.append(boton)

        # Creamos los botones para el lado derecho y los agregamos al frame derecho
        self.botones_derecha = []
        for i in range(4):
            nombre_boton = f"Botón {i+4}"
            if i == 0:
                nombre_boton = "Lista circular"
            elif i == 1:
                nombre_boton = "Lista circular doble"
            elif i == 2:
                nombre_boton = "Lista doblemente enlazada"
            elif i == 3:
                nombre_boton = "Lista simplemente enlazada"
            boton = tk.Button(self.frame_derecha, text=nombre_boton, width=20, height=2, font=("Arial", 12))
            boton.pack(side=tk.TOP, padx=10, pady=10)
            self.botones_derecha.append(boton)

    # Definimos la función que se ejecutará al hacer clic en el primer botón
    def pila(self):
        ventana_pila = tk.Toplevel()
        self.interfaz_actual = InterfazGraficaPila(ventana_pila)

def main():
    root = tk.Tk()
    app = VentanaMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
