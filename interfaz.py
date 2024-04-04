import tkinter as tk
import algoritmo    #Archivo .py en donde está el algoritmo

class Interfaz:
    def __init__(self, master):     # self.master = ventana
        self.master = master
        self.master.title("Autómata Finito Deterministico")
        self.master.geometry("350x400")

        #Etiqueta de Condición de uso
        self.etiqueta0 = tk.Label(master, text="Condición: La cadena debe tener una longitud impar, no debe formar un 10 y solo puede usar los caracteres 0, 1 y 2.", wraplength = 300)
        self.etiqueta0.pack(fill=tk.BOTH)

        #Etiqueta de Ingresar Cadena
        self.etiqueta1 = tk.Label(master, text="Ingresar cadena")
        self.etiqueta1.pack(fill=tk.BOTH)

        # Caja de texto
        self.cajaTexto = tk.Entry(master)
        self.cajaTexto.pack()

        # Variable para almacenar la cadena
        self.cadena = ""

        # Botón Ingresar Datos
        self.boton1 = tk.Button(master, text="Ingresar", command=self.obtenerCadena)
        self.boton1.pack()

        #Etiqueta que muestra el resultado
        self.etiquetaResultado = tk.Label(master)
        self.etiquetaResultado.pack(fill=tk.BOTH)


    #Obtención de la cadena de texto
    def obtenerCadena(self):
        self.cadena = self.cajaTexto.get()
        self.resultado = algoritmo.validacion(self.cadena)
        self.etiquetaResultado["text"] = self.resultado

def main():
    ventana = tk.Tk()           #Creación de la ventana | Uso de Tkinter
    app = Interfaz(ventana)     
    ventana.mainloop()

if __name__ == "__main__":
    main()
    