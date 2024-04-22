import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def insertar(self, elemento):
        self.items.append(elemento)

    def eliminar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def buscar(self, elemento):
        return elemento in self.items

class InterfazPila:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Pila")

        self.pila = Pila()

        self.frame_botones = tk.Frame(ventana)
        self.frame_botones.pack()

        self.btn_insertar = tk.Button(self.frame_botones, text="Insertar", command=self.insertar_elemento)
        self.btn_insertar.grid(row=0, column=0)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar", command=self.eliminar_elemento)
        self.btn_eliminar.grid(row=0, column=1)

        self.btn_buscar = tk.Button(self.frame_botones, text="Buscar", command=self.buscar_elemento)
        self.btn_buscar.grid(row=0, column=2)

        self.btn_ver_grafico = tk.Button(self.frame_botones, text="Ver gráficamente", command=self.ver_grafico)
        self.btn_ver_grafico.grid(row=0, column=3)

    def insertar_elemento(self):
        valor = tk.simpledialog.askstring("Insertar en la pila", "Ingrese el valor a insertar en la pila:")
        if valor:
            self.pila.insertar(valor)
            messagebox.showinfo("Insertar en la pila", f"Se ha insertado el valor {valor} en la pila.")

    def eliminar_elemento(self):
        elemento_eliminado = self.pila.eliminar()
        if elemento_eliminado is not None:
            messagebox.showinfo("Eliminar de la pila", f"Se ha eliminado el valor {elemento_eliminado} de la pila.")
        else:
            messagebox.showwarning("Eliminar de la pila", "La pila está vacía.")

    def buscar_elemento(self):
        valor = tk.simpledialog.askstring("Buscar en la pila", "Ingrese el valor a buscar en la pila:")
        if valor:
            if self.pila.buscar(valor):
                messagebox.showinfo("Buscar en la pila", f"El valor {valor} está en la pila.")
            else:
                messagebox.showinfo("Buscar en la pila", f"El valor {valor} no está en la pila.")

    def ver_grafico(self):
        if self.pila.esta_vacia():
            messagebox.showinfo("Ver gráficamente", "La pila está vacía.")
        else:
            valores = self.pila.items
            plt.figure(figsize=(4, 2))
            plt.barh(range(len(valores)), valores, color='skyblue')
            plt.gca().axes.get_yaxis().set_visible(False)  # Ocultar ejes y etiquetas de eje y
            plt.show()

# Crear la ventana principal de la aplicación
ventana_principal = tk.Tk()
app = InterfazPila(ventana_principal)
ventana_principal.mainloop()