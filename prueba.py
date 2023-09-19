import tkinter as tk

def verificar_respuesta(respuesta, boton):
    # Comprobar si la respuesta es correcta
    if respuesta == respuesta_correcta:
        label_estado.config(text="Correcto", fg="green")
        boton.config(bg="green")  # Cambiar el color de fondo a verde para el botón correcto
    else:
        label_estado.config(text="Incorrecto", fg="red")
        boton.config(bg="red")  # Cambiar el color de fondo a rojo para los botones incorrectos

# Respuesta correcta (puedes cambiarla según tu necesidad)
respuesta_correcta = "Opción 2"

# Crear una ventana
ventana = tk.Tk()
ventana.title("Verificación de Respuesta")

# Crear etiqueta para mostrar el estado
label_estado = tk.Label(ventana, text="", font=("Arial", 14))
label_estado.pack(pady=10)

# Crear botones con diferentes respuestas
boton1 = tk.Button(ventana, text="Opción 1", command=lambda: verificar_respuesta("Opción 1", boton1))
boton1.pack(pady=5)

boton2 = tk.Button(ventana, text="Opción 2", command=lambda: verificar_respuesta("Opción 2", boton2))
boton2.pack(pady=5)

boton3 = tk.Button(ventana, text="Opción 3", command=lambda: verificar_respuesta("Opción 3", boton3))
boton3.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
