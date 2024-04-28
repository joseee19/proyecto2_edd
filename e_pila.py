import tkinter as tk
from tkinter import simpledialog, messagebox


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self):
        if self.esta_vacia():
            messagebox.showinfo("¡ATENCIÓN!", "La pila está vacía.")
            return None
        else:
            dato_eliminado = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            return dato_eliminado


class InterfazGraficaPila:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Pila")

        self.pila = Pila()

        self.canvas = tk.Canvas(ventana, width=300, height=300, bg='white', highlightthickness=0)
        self.canvas.pack()

        self.btn_insertar = tk.Button(ventana, text="Insertar", width=43, height=2, command=self.insertar_elemento,
        bg="lightblue")
        self.btn_insertar.pack()

        self.btn_eliminar = tk.Button(ventana, text="Eliminar", width=43, height=2, command=self.eliminar_elemento,
        bg="lightblue")
        self.btn_eliminar.pack()

        self.bloques = []  # Lista para almacenar referencias a los bloques gráficos
        self.textos = []  # Lista para almacenar referencias a los textos gráficos

    def insertar_elemento(self):
        valor = simpledialog.askstring("Insertar en la pila", "Ingrese el valor a insertar en la pila:")
        if valor:
            self.pila.insertar(valor)
            self.mostrar_pila()

    def eliminar_elemento(self):
        dato_eliminado = self.pila.eliminar()
        if dato_eliminado is not None:
            self.mostrar_pila()

    def mostrar_pila(self):
        # Eliminar bloques y textos anteriores
        for bloque in self.bloques:
            self.canvas.delete(bloque)
        for texto in self.textos:
            self.canvas.delete(texto)

        self.bloques = []
        self.textos = []

        nodo_actual = self.pila.cabeza
        y = 50
        while nodo_actual:
            x0 = 50
            lado = 40
            # Crear bloque gráfico
            bloque = self.canvas.create_rectangle(x0, y, x0 + lado, y + lado, fill="yellow")
            self.bloques.append(bloque)  # Agregar referencia a la lista

            # Crear texto gráfico
            texto = self.canvas.create_text(x0 + lado / 2, y + lado / 2, text=str(nodo_actual.dato), font=("Arial", 12))
            self.textos.append(texto)  # Agregar referencia a la lista

            y += 40
            nodo_actual = nodo_actual.siguiente


def main():
    root = tk.Tk()
    app = InterfazGraficaPila(root)
    root.mainloop()


if __name__ == "__main__":
    main()
