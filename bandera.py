import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk
from lectorCSV import sorteador 

ventana = tk.Tk()

def mostrar_imagen_desde_url(url):
    response = requests.get(url)
    image_data = BytesIO(response.content)
    image = Image.open(image_data)
    photo = ImageTk.PhotoImage(image)
    label_imagen.config(image=photo)
    label_imagen.image = photo 

frame1 = tk.Frame(ventana, bg="white", width=256, height=192)
frame1.grid(column=0, row=0)

label_imagen = tk.Label(frame1)
label_imagen.grid(column=0, row=0)

frame2 = tk.Frame(ventana, bg="blue", width=256, height=192)
boton1 = tk.Button(frame2, text="", width=7, height=1)
boton2 = tk.Button(frame2, text="", width=7, height=1)
boton3 = tk.Button(frame2, text="", width=7, height=1)
boton4 = tk.Button(frame2, text="", width=7, height=1)
boton1.grid(column=0, row=0)
boton2.grid(column=0, row=1)
boton3.grid(column=1, row=0)
boton4.grid(column=1, row=1)

'''.place(x=15, y=25)
.place(x=15, y=70)
.place(x=150, y=25)
.place(x=150, y=70)'''
frame2.grid(column=0, row=1)

ventana.geometry("250x320")

banderas = []
for i in range(4):
    bandera = sorteador()
    banderas.append(bandera)
 
boton1.config(text=banderas[0][0])   
boton2.config(text=banderas[1][0])
boton3.config(text=banderas[2][0])
boton4.config(text=banderas[3][0])
    
url_imagen = f"https://flagcdn.com/256x192/{banderas[3][1].lower()}.png"
mostrar_imagen_desde_url(url_imagen) 

boton = [boton1, boton2, boton3, boton4]



ventana.mainloop()