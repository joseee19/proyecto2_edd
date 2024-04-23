import tkinter as tk
from tkinter import simpledialog, messagebox

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaSimplementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_inicio(self):
        if self.esta_vacia():
            messagebox.showwarning("Lista vacía", "No se puede eliminar, la lista está vacía.")
            return None
        eliminado = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        return eliminado

    def eliminar_final(self):
        if self.esta_vacia():
            messagebox.showwarning("Lista vacía", "No se puede eliminar, la lista está vacía.")
            return None
        elif self.cabeza.siguiente is None:
            eliminado = self.cabeza.valor
            self.cabeza = None
            return eliminado
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente:
                actual = actual.siguiente
            eliminado = actual.siguiente.valor
            actual.siguiente = None
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

class InterfazGraficaListaSimplementeEnlazada:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lista Simplemente Enlazada")

        self.lista = ListaSimplementeEnlazada()

        self.canvas = tk.Canvas(ventana, width=200, height=300, bg='white', highlightthickness=0)
        self.canvas.pack()

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
        self.canvas.delete("nodo")
        y = 50
        for valor in self.lista.mostrar():
            self.canvas.create_text(100, y, text=valor, font=("Arial", 12), tags="nodo")
            y += 30

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = InterfazGraficaListaSimplementeEnlazada(ventana_principal)
    ventana_principal.mainloop()