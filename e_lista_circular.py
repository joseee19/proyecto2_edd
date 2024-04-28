import tkinter as tk
from tkinter import simpledialog, messagebox

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            nuevo_nodo.siguiente = nuevo_nodo  # Puntero hacia sí mismo
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            nuevo_nodo.siguiente = nuevo_nodo  # Puntero hacia sí mismo
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_inicio(self):
        if self.esta_vacia():
            messagebox.showwarning("Lista vacía", "No se puede eliminar, la lista está vacía.")
            return None
        eliminado = self.cabeza.valor
        if self.cabeza.siguiente == self.cabeza:  # Solo hay un nodo en la lista
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente
        return eliminado

    def eliminar_final(self):
        if self.esta_vacia():
            messagebox.showwarning("Lista vacía", "No se puede eliminar, la lista está vacía.")
            return None
        eliminado = None
        if self.cabeza.siguiente == self.cabeza:  # Solo hay un nodo en la lista
            eliminado = self.cabeza.valor
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente != self.cabeza:
                actual = actual.siguiente
            eliminado = actual.siguiente.valor
            actual.siguiente = self.cabeza
        return eliminado

    def buscar(self, valor):
        if self.esta_vacia():
            return False
        actual = self.cabeza
        while True:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False

    def rotar_izquierda(self):
        if self.esta_vacia():
            messagebox.showwarning("Lista vacía", "No se puede rotar, la lista está vacía.")
            return
        self.cabeza = self.cabeza.siguiente

    def rotar_derecha(self):
        if self.esta_vacia():
            messagebox.showwarning("Lista vacía", "No se puede rotar, la lista está vacía.")
            return
        actual = self.cabeza
        while actual.siguiente != self.cabeza:
            actual = actual.siguiente
        self.cabeza = actual

    def mostrar(self):
        valores = []
        if not self.esta_vacia():
            actual = self.cabeza
            while True:
                valores.append(actual.valor)
                actual = actual.siguiente
                if actual == self.cabeza:
                    break
        return valores

class InterfazGraficaListaCircular:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lista Circular")

        self.lista = ListaCircular()

        self.canvas = tk.Canvas(ventana, width=350, height=250, bg='gray', highlightthickness=0)
        self.canvas.pack()

        self.btn_insertar_inicio = tk.Button(ventana, text="Insertar al inicio",width=43, height=2, command=self.insertar_inicio)
        self.btn_insertar_inicio.pack()

        self.btn_insertar_final = tk.Button(ventana, text="Insertar al final",width=43, height=2, command=self.insertar_final)
        self.btn_insertar_final.pack()

        self.btn_eliminar_inicio = tk.Button(ventana, text="Eliminar al inicio",width=43, height=2, command=self.eliminar_inicio)
        self.btn_eliminar_inicio.pack()

        self.btn_eliminar_final = tk.Button(ventana, text="Eliminar al final",width=43, height=2, command=self.eliminar_final)
        self.btn_eliminar_final.pack()


        self.btn_rotar_izquierda = tk.Button(ventana, text="Rotar a la izquierda",width=43, height=2, command=self.rotar_izquierda)
        self.btn_rotar_izquierda.pack()

        self.btn_rotar_derecha = tk.Button(ventana, text="Rotar a la derecha",width=43, height=2, command=self.rotar_derecha)
        self.btn_rotar_derecha.pack()

        self.btn_buscar = tk.Button(ventana, text="Buscar",width=43, height=2, command=self.buscar_valor)
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

    def rotar_izquierda(self):
        self.lista.rotar_izquierda()
        self.mostrar_lista()

    def rotar_derecha(self):
        self.lista.rotar_derecha()
        self.mostrar_lista()

    def mostrar_lista(self):
        self.canvas.delete("bloque")
        bloque_ancho = 40
        bloque_alto = 40
        x_inicial = 45
        y_inicial = 92
        separacion = 10
        for i, valor in enumerate(self.lista.mostrar()):
            x = x_inicial + (bloque_ancho + separacion) * i
            self.canvas.create_rectangle(x, y_inicial, x + bloque_ancho, y_inicial + bloque_alto, fill="lightblue", outline="yellow", tags="bloque")
            self.canvas.create_text(x + bloque_ancho / 2, y_inicial + bloque_alto / 2, text=valor, tags="bloque")

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = InterfazGraficaListaCircular(ventana_principal)
    ventana_principal.mainloop()
