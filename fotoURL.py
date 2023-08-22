import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from lectorCSV import sorteador

def mostrar_imagen_desde_url(url):
    response = requests.get(url)
    image_data = BytesIO(response.content)
    image = Image.open(image_data)
    photo = ImageTk.PhotoImage(image)
    label_imagen.config(image=photo)
    label_imagen.image = photo  # ¡Importante! Evita que la imagen se elimine por recolección de basura

# Crear una instancia de Tkinter
ventana = tk.Tk()
ventana.title("Imagen desde URL")

# Crear un widget de etiqueta para mostrar la imagen
label_imagen = tk.Label(ventana)
label_imagen.pack()

# URL de la imagen
bandera = sorteador()
url_imagen = f"https://flagcdn.com/256x192/{bandera[1].lower()}.png"
print(bandera[0])

# Cargar y mostrar la imagen desde la URL
mostrar_imagen_desde_url(url_imagen)

# Iniciar el bucle de eventos de Tkinter
ventana.mainloop()
