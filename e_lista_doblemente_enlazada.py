import tkinter as tk
from tkinter import simpledialog, messagebox

class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_final(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def eliminar_inicio(self):
        if self.esta_vacia():
            messagebox.showwarning("Lista vacía", "No se puede eliminar, la lista está vacía.")
            return None
        eliminado = self.cabeza.valor
        if self.cabeza.siguiente is None:
            self.cabeza = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        return eliminado

    def eliminar_final(self):
        if self.esta_vacia():
            messagebox.showwarning("Lista vacía", "No se puede eliminar, la lista está vacía.")
            return None
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        eliminado = actual.valor
        if actual.anterior:
            actual.anterior.siguiente = None
        else:
            self.cabeza = None
        return eliminado

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(actual.valor)
            actual = actual.siguiente
        return valores

class InterfazGraficaListaDoblementeEnlazada:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lista Doblemente Enlazada")

        self.lista = ListaDoblementeEnlazada()

        self.canvas = tk.Canvas(ventana, width=200, bg='white', highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(ventana, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame_colocar = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_colocar, anchor=tk.NW)

        self.btn_insertar_inicio = tk.Button(ventana, text="Insertar al inicio", command=self.insertar_inicio)
        self.btn_insertar_inicio.pack()

        self.btn_insertar_final = tk.Button(ventana, text="Insertar al final", command=self.insertar_final)
        self.btn_insertar_final.pack()

        self.btn_eliminar_inicio = tk.Button(ventana, text="Eliminar al inicio", command=self.eliminar_inicio)
        self.btn_eliminar_inicio.pack()

        self.btn_eliminar_final = tk.Button(ventana, text="Eliminar al final", command=self.eliminar_final)
        self.btn_eliminar_final.pack()

        self.btn_buscar = tk.Button(ventana, text="Buscar", command=self.buscar_valor)
        self.btn_buscar.pack()

        self.bloques = []

    def insertar_inicio(self):
        valor = simpledialog.askstring("Insertar al inicio", "Ingrese el valor a insertar al inicio:")
        if valor:
            self.lista.insertar_inicio(valor)
            self.mostrar_lista()

    def insertar_final(self):
        valor = simpledialog.askstring("Insertar al final", "Ingrese el valor a insertar al final:")
        if valor:
            self.lista.insertar_final(valor)
            self.mostrar_lista()

    def eliminar_inicio(self):
        eliminado = self.lista.eliminar_inicio()
        if eliminado is not None:
            messagebox.showinfo("Elemento eliminado", f"Se eliminó el elemento: {eliminado}")
            self.mostrar_lista()

    def eliminar_final(self):
        eliminado = self.lista.eliminar_final()
        if eliminado is not None:
            messagebox.showinfo("Elemento eliminado", f"Se eliminó el elemento: {eliminado}")
            self.mostrar_lista()

    def buscar_valor(self):
        valor = simpledialog.askstring("Buscar", "Ingrese el valor a buscar:")
        encontrado = self.lista.buscar(valor)
        if encontrado:
            messagebox.showinfo("Elemento encontrado", f"El valor {valor} está en la lista.")
        else:
            messagebox.showinfo("Elemento no encontrado", f"El valor {valor} no está en la lista.")

    def mostrar_lista(self):
        for widget in self.frame_colocar.winfo_children():
            widget.destroy()

        for valor in self.lista.mostrar():
            tk.Label(self.frame_colocar, text=str(valor)).pack()

        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

