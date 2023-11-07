import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk
from lectorCSV import sorteador
import random
import tkinter.messagebox as messagebox

ventana = tk.Tk()
ventana.resizable(width=False, height=False)

juego_terminado = False  # Variable para verificar si el juego ha terminado

def imagen_url(url):
    response = requests.get(url)
    image_data = BytesIO(response.content)
    image = Image.open(image_data)
    photo = ImageTk.PhotoImage(image)
    label_imagen.config(image=photo)
    label_imagen.image = photo

def pasar_bandera():
    global bandera_correcta, puntaje, intentos, juego_terminado
    if intentos == 0:
        respuesta_correcta.config(text="¡Perdiste! No quedan más intentos.")
        juego_terminado = True
        resultado = messagebox.askyesno("Juego Terminado", "¿Deseas jugar de nuevo?")
        if resultado:
            nuevo_juego()
        return

    bandera_correcta = random.choice(banderas)
    url_imagen = f"https://flagcdn.com/256x192/{bandera_correcta[1].lower()}.png"
    imagen_url(url_imagen)

    # Obtener cuatro banderas diferentes para las opciones de respuesta
    opciones_respuesta = random.sample(banderas, 4)

    # Asegurarse de que la respuesta correcta esté en las opciones
    if bandera_correcta not in opciones_respuesta:
        opciones_respuesta[random.randint(0, 3)] = bandera_correcta

    for i, boton in enumerate([boton1, boton2, boton3, boton4]):
        boton.config(text=opciones_respuesta[i][0])
        if opciones_respuesta[i][0] == bandera_correcta[0]:
            global boton_correcto
            boton_correcto = boton  # Establece el botón correcto

    for boton in [boton1, boton2, boton3, boton4]:
        boton.config(bg="white")

def verificar_respuesta(boton):
    global puntaje, intentos, juego_terminado
    if juego_terminado:
        return  # No permitir más interacción si el juego ha terminado

    if boton.cget("text") == bandera_correcta[0]:
        boton.config(bg="green")
        respuesta_correcta.config(text="Respuesta correcta")
        puntaje += 1
        actualizar_puntaje()
        ventana.after(1000, nuevo_juego)
    else:
        boton.config(bg="red")
        ventana.after(1000, pasar_bandera)  # Avanzar automáticamente a la siguiente bandera
        intentos -= 1
        actualizar_puntaje()
        if intentos == 0:
            respuesta_correcta.config(text="¡Perdiste! No quedan más intentos.")
            juego_terminado = True
            resultado = messagebox.askyesno("Juego Terminado", "¿Deseas jugar de nuevo?")
            if resultado:
                nuevo_juego()
        else:
            respuesta_correcta.config(f"Respuesta incorrecta. País correcto: {bandera_correcta[0]}. Intentos restantes: {intentos}")
            intentos_label.config(text=f"Intentos restantes: {intentos}")

def nuevo_juego():
    global intentos, juego_terminado, puntaje
    intentos = 3  # Restablecer los intentos a 3
    puntaje = 0  # Reiniciar el puntaje
    respuesta_correcta.config(text="")
    juego_terminado = False
    pasar_bandera()

def actualizar_puntaje():
    puntaje_label.config(text=f"Puntaje: {puntaje}")
    intentos_label.config(text=f"Intentos restantes: {intentos}")

frame1 = tk.Frame(ventana, bg="green", width=256, height=192)
frame1.grid(column=0, row=0)

label_imagen = tk.Label(frame1)
label_imagen.grid(column=0, row=0)
pixel = tk.PhotoImage(width=1, height=1)
frame2 = tk.Frame(ventana, width=256, height=192)
boton1 = tk.Button(frame2, text="", image=pixel, width=128, compound="c", command=lambda: verificar_respuesta(boton1))
boton2 = tk.Button(frame2, text="", image=pixel, width=128, compound="c", command=lambda: verificar_respuesta(boton2))
boton3 = tk.Button(frame2, text="", image=pixel, width=128, compound="c", command=lambda: verificar_respuesta(boton3))
boton4 = tk.Button(frame2, text="", image=pixel, width=128, compound="c", command=lambda: verificar_respuesta(boton4))
boton1.grid(column=0, row=0)
boton2.grid(column=0, row=1)
boton3.grid(column=1, row=0)
boton4.grid(column=1, row=1)

frame2.grid(column=0, row=1)

respuesta_correcta = tk.Label(frame2, text="", font=("Arial", 10))
respuesta_correcta.grid(column=0, row=2, columnspan=2)

puntaje = 0
intentos = 3

puntaje_label = tk.Label(frame2, text=f"Puntaje: {puntaje}", font=("Arial", 10))
puntaje_label.grid(column=0, row=3, columnspan=2)

intentos_label = tk.Label(frame2, text=f"Intentos restantes: {intentos}", font=("Arial", 10))
intentos_label.grid(column=0, row=4, columnspan=2)

# Cargar una lista más grande de banderas
banderas = [sorteador() for _ in range(20)]  # Puedes ajustar el número de banderas

pasar_bandera()

ventana.mainloop()
