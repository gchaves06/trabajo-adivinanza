import tkinter as tk
import random

def cambiar_texto():
    textos = ["Texto 1", "Texto 2", "Texto 3", "Texto 4"]
    texto_seleccionado = random.choice(textos)
    label.config(text=texto_seleccionado)

app = tk.Tk()
app.title("Sorteo de Textos")

label = tk.Label(app, text="Presiona el botón para sortear un texto")
label.pack()

button = tk.Button(app, text="Sortear", command=cambiar_texto)
button.pack()

app.mainloop()
