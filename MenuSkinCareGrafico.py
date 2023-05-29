import tkinter as tk

def piel_grasa():
    resultado.config(text="\nTu rutina será la siguiente:\n\n1. Dermolimpiador de Matcha y menta\n\n2. Serum de retinol para el contorno de ojos (Aplicar solo por la noche)\n\n3. Serum de Ácido Hialurónico")

def piel_seca():
    resultado.config(text="\nTu rutina será la siguiente:\n\n1. Dermolimpiador de Matcha y menta\n\n2. Serum de retinol para el contorno de ojos (Aplicar solo por la noche)\n\nSerum Iluminador")

def piel_mixta():
    resultado.config(text="\nTu rutina será la siguiente:\n\n1. Dermolimpiador de Matcha y menta\n\n2. Serum de retinol para el contorno de ojos (Aplicar solo por la noche)\n\nSerum de Vitamina C")

def menu():
    lbl_menu.config(text="¡Bienvenido/a! ¡Comencemos tu rutina de Skin Care!")
    lbl_opciones.config(text="\nSeleccione su tipo de piel:")
    btn_grasa.config(text="Piel Grasa", command=piel_grasa)
    btn_seca.config(text="Piel Seca", command=piel_seca)
    btn_mixta.config(text="Piel Mixta", command=piel_mixta)

# Crear la ventana principal
window = tk.Tk()
window.title("Skin Care")

# Etiqueta y botones del menú
lbl_menu = tk.Label(window, text="")
lbl_menu.pack()

lbl_opciones = tk.Label(window, text="")
lbl_opciones.pack()

btn_grasa = tk.Button(window, text="", command=piel_grasa)
btn_grasa.pack()

btn_seca = tk.Button(window, text="", command=piel_seca)
btn_seca.pack()

btn_mixta = tk.Button(window, text="", command=piel_mixta)
btn_mixta.pack()

# Etiqueta para mostrar el resultado
resultado = tk.Label(window, text="")
resultado.pack()

# Iniciar el bucle principal de la ventana
menu()
window.mainloop()

