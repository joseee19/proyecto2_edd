import tkinter as tk
from tkinter import simpledialog, messagebox


class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def insertar(self, elemento):
        self.items.append(elemento)

    def eliminar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            messagebox.showinfo("¡ATENCIÓN!", "La cola está vacía.")


class InterfazGraficaCola:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Cola")

        self.cola = Cola()

        self.canvas = tk.Canvas(ventana, width=300, height=300, bg='white', highlightthickness=0)
        self.canvas.pack()

        self.btn_insertar = tk.Button(ventana, text="Insertar",width=43, height=2, command=self.insertar_elemento,
        bg="lightblue")
        self.btn_insertar.pack()

        self.btn_eliminar = tk.Button(ventana, text="Eliminar",width=43, height=2, command=self.eliminar_elemento,
        bg="lightblue")
        self.btn_eliminar.pack()

        self.bloques = []  # Lista para almacenar referencias a los bloques gráficos
        self.textos = []  # Lista para almacenar referencias a los textos gráficos

    def insertar_elemento(self):
        valor = tk.simpledialog.askstring("Insertar en la cola", "Ingrese el valor a insertar en la cola:")
        if valor is not None:
            self.cola.insertar(valor)
            self.mostrar_cola()

    def eliminar_elemento(self):
        self.cola.eliminar()
        self.mostrar_cola()

    def mostrar_cola(self):
        # Eliminar bloques y textos anteriores
        for bloque in self.bloques:
            self.canvas.delete(bloque)
        for texto in self.textos:
            self.canvas.delete(texto)

        self.bloques = []
        self.textos = []

        for i, valor in enumerate(self.cola.items):
            x0, y0 = 50, 50 + i * 40
            lado = 40
            # Crear bloque gráfico
            bloque = self.canvas.create_rectangle(x0, y0, x0 + lado, y0 + lado, fill="skyblue")
            self.bloques.append(bloque)  # Agregar referencia a la lista de bloques

            # Crear texto gráfico
            texto = self.canvas.create_text(x0 + lado / 2, y0 + lado / 2, text=str(valor), font=("Arial", 12))
            self.textos.append(texto)  # Agregar referencia a la lista de textos


def main():
    root = tk.Tk()
    app = InterfazGraficaCola(root)
    root.mainloop()


if __name__ == "__main__":
    main()
