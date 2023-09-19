import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk
from lectorCSV import sorteador 
import random

ventana = tk.Tk()
ventana.resizable(width=False, height=False)

def mostrar_imagen_desde_url(url):
    response = requests.get(url)
    image_data = BytesIO(response.content)
    image = Image.open(image_data)
    photo = ImageTk.PhotoImage(image)
    label_imagen.config(image=photo)
    label_imagen.image = photo 

frame1 = tk.Frame(ventana,bg="green", width=256, height=192)
frame1.grid(column=0, row=0)

label_imagen = tk.Label(frame1)
label_imagen.grid(column=0, row=0)
pixel = tk.PhotoImage(width=1, height=1)
frame2 = tk.Frame(ventana, width=256, height=192)
boton1 = tk.Button(frame2, text="", image=pixel, width=128, compound="c")
boton2 = tk.Button(frame2, text="", image=pixel, width=128, compound="c")
boton3 = tk.Button(frame2, text="", image=pixel, width=128, compound="c")
boton4 = tk.Button(frame2, text="", image=pixel, width=128, compound="c")
boton1.grid(column=0, row=0)
boton2.grid(column=0, row=1)
boton3.grid(column=1, row=0)
boton4.grid(column=1, row=1)

'''.place(x=15, y=25)
.place(x=15, y=70)
.place(x=150, y=25)
.place(x=150, y=70)'''
frame2.grid(column=0, row=1)



banderas = []
for i in range(4):
    bandera = sorteador()
    banderas.append(bandera)
url_imagen = f"https://flagcdn.com/256x192/{banderas[1][1].lower()}.png"

random.shuffle(banderas)

boton1.config(text=banderas[0][0])   
boton2.config(text=banderas[1][0])
boton3.config(text=banderas[2][0])
boton4.config(text=banderas[3][0])
    
mostrar_imagen_desde_url(url_imagen) 

boton = [boton1, boton2, boton3, boton4]

ventana.mainloop()