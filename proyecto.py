import tkinter as tk

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

        self.etiqueta_estado = tk.Label(ventana, text="")
        self.etiqueta_estado.pack()

        self.frame_botones = tk.Frame(ventana)
        self.frame_botones.pack()

        self.btn_insertar = tk.Button(self.frame_botones, text="Insertar", command=self.insertar_elemento)
        self.btn_insertar.grid(row=0, column=0)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar", command=self.eliminar_elemento)
        self.btn_eliminar.grid(row=0, column=1)

        self.btn_buscar = tk.Button(self.frame_botones, text="Buscar", command=self.buscar_elemento)
        self.btn_buscar.grid(row=0, column=2)

    def insertar_elemento(self):
        valor = input("Ingrese el valor a insertar en la pila: ")
        self.pila.insertar(valor)
        self.actualizar_estado()

    def eliminar_elemento(self):
        elemento_eliminado = self.pila.eliminar()
        if elemento_eliminado is not None:
            print("Elemento eliminado:", elemento_eliminado)
        else:
            print("La pila está vacía.")
        self.actualizar_estado()

    def buscar_elemento(self):
        valor = input("Ingrese el valor a buscar en la pila: ")
        if self.pila.buscar(valor):
            print("El valor", valor, "está en la pila.")
        else:
            print("El valor", valor, "no está en la pila.")

    def actualizar_estado(self):
        if self.pila.esta_vacia():
            self.etiqueta_estado.config(text="La pila está vacía.")
        else:
            self.etiqueta_estado.config(text="Elementos en la pila: " + str(self.pila.items))

# Crear la ventana principal de la aplicación
ventana_principal = tk.Tk()
app = InterfazPila(ventana_principal)
ventana_principal.mainloop()