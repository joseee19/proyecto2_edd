import tkinter as tk
from tkinter import simpledialog

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def insertar(self, elemento):
        self.items.append(elemento)

    def eliminar(self):
        if not self.esta_vacia():
            return self.items.pop() and self.elemento.pop()


class InterfazGraficaPila:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Pila")

        self.pila = Pila()

        self.canvas = tk.Canvas(ventana, width=200, height=300, bg='white', highlightthickness=0)
        self.canvas.pack()

        self.btn_insertar = tk.Button(ventana, text="Insertar", command=self.insertar_elemento)
        self.btn_insertar.pack()

        self.btn_eliminar = tk.Button(ventana, text="Eliminar", command=self.eliminar_elemento)
        self.btn_eliminar.pack()

        self.bloques = []

    def insertar_elemento(self):
        valor = tk.simpledialog.askstring("Insertar en la pila", "Ingrese el valor a insertar en la pila:")
        if valor:
            self.pila.insertar(valor)
            self.mostrar_pila()

    def eliminar_elemento(self):
        if not self.pila.esta_vacia():
            self.pila.eliminar()
            self.mostrar_pila()

    def mostrar_pila(self):
        self.canvas.delete("bloque")
        self.bloques = []
        for i, valor in enumerate(self.pila.items):
            x0, y0 = 50, 50 + i * 40
            lado = 40
            self.canvas.create_rectangle(x0, y0, x0 + lado, y0 + lado, fill="skyblue", tags="bloque")
            self.canvas.create_text(x0 + lado/2, y0 + lado/2, text=str(valor), font=("Arial", 12))
