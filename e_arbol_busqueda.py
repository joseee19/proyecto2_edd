import tkinter as tk
from tkinter import simpledialog, messagebox

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBusquedaBinaria:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
        # Ignora el valor si ya está en el árbol

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.valor = self._encontrar_min_valor(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.valor)
        return nodo

    def _encontrar_min_valor(self, nodo):
        min_valor = nodo.valor
        while nodo.izquierda is not None:
            min_valor = nodo.izquierda.valor
            nodo = nodo.izquierda
        return min_valor

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        if valor == nodo.valor:
            return nodo
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

class InterfazGraficaArbolBusquedaBinaria:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Árbol de Búsqueda Binaria")

        self.arbol = ArbolBusquedaBinaria()

        self.canvas = tk.Canvas(ventana, width=800, height=500, bg='lightblue', highlightthickness=0)
        self.canvas.pack()

        self.btn_insertar = tk.Button(ventana, text="Insertar", width=43, height=2,command=self.insertar_valor)
        self.btn_insertar.pack()

        self.btn_eliminar = tk.Button(ventana, text="Eliminar", width=43, height=2,command=self.eliminar_valor)
        self.btn_eliminar.pack()

        self.btn_buscar = tk.Button(ventana, text="Buscar",width=43, height=2, command=self.buscar_valor)
        self.btn_buscar.pack()

    def insertar_valor(self):
        valor = simpledialog.askinteger("Insertar valor", "Ingrese el valor a insertar:")
        if valor is not None:
            self.arbol.insertar(valor)
            self.mostrar_arbol()

    def eliminar_valor(self):
        valor = simpledialog.askinteger("Eliminar valor", "Ingrese el valor a eliminar:")
        if valor is not None:
            self.arbol.eliminar(valor)
            self.mostrar_arbol()

    def buscar_valor(self):
        valor = simpledialog.askinteger("Buscar valor", "Ingrese el valor a buscar:")
        if valor is not None:
            nodo_resaltado = self.arbol.buscar(valor)
            if nodo_resaltado:
                messagebox.showinfo("Valor encontrado", f"El valor {valor} está en el árbol.")
                self.mostrar_arbol(nodo_resaltado)  # Mostrar el árbol con el nodo buscado resaltado
            else:
                messagebox.showinfo("Valor no encontrado", f"El valor {valor} no está en el árbol.")

    def mostrar_arbol(self, nodo_resaltado=None):
        self.canvas.delete("nodo")
        self._mostrar_arbol_recursivo(self.arbol.raiz, 400, 50, 125, nodo_resaltado)

    def _mostrar_arbol_recursivo(self, nodo, x, y, espacio, nodo_resaltado=None):
        if nodo is not None:
            color = "white"
            if nodo_resaltado and nodo_resaltado.valor == nodo.valor:
                color = "yellow"  # Cambiar color del círculo del nodo buscado
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=color, outline="black", tags="nodo")
            self.canvas.create_text(x, y, text=str(nodo.valor), tags="nodo")
            if nodo.izquierda is not None:
                self.canvas.create_line(x-20, y+20, x-espacio+20, y+100, arrow=tk.LAST, tags="nodo")
                self._mostrar_arbol_recursivo(nodo.izquierda, x-espacio, y+100, espacio//2, nodo_resaltado)
            if nodo.derecha is not None:
                self.canvas.create_line(x+20, y+20, x+espacio-20, y+100, arrow=tk.LAST, tags="nodo")
                self._mostrar_arbol_recursivo(nodo.derecha, x+espacio, y+100, espacio//2, nodo_resaltado)

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = InterfazGraficaArbolBusquedaBinaria(ventana_principal)
    ventana_principal.mainloop()
