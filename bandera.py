import tkinter as tk
    
ventana = tk.Tk()

ventana.title("Adivinanzas")

def center_widget(widget, container):
    widget.update_idletasks()
    width = widget.winfo_width()
    height = widget.winfo_height()
    x = (container.winfo_width() - width) // 2
    y = (container.winfo_height() - height) // 2
    widget.place(x=70, y=40)

ventana.configure(bg="white")
ventana.resizable(width=False, height=False)
frame2 = tk.Frame(ventana, bg="red", width=256, height=192)
boton2 = tk.Button(ventana, text="", width=10, height=5)
boton2.grid(column=0, row=2)
frame2.grid(column=0, row=2)

frame1 = tk.Frame(ventana, bg="red", width=256, height=192)

ventana.geometry("250x320")

center_widget(boton2,ventana)

ventana.mainloop()