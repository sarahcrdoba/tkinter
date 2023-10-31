import tkinter as tk
from PIL import Image, ImageTk

# creem una finestra i una etiqueta on posar les fotos
finestra = tk.Tk()
etiqueta_foto = tk.Label(finestra)
etiqueta_foto.pack()

# llista amb les fotos i la ruta
fotos = [
    'fotos/ejercicio2.jpeg',
    'fotos/ejercicio22.jpeg',
    'fotos/ejercicio222.jpeg',
]

index_foto = 0


def mostrarFoto(index):
    foto = Image.open(fotos[index])     # obre la primera foto de la llista
    foto = foto.resize((900, 650))      # mida de la foto
    foto = ImageTk.PhotoImage(foto)     # permet que la foto sigui compatible amb tkinter
    etiqueta_foto.config(image=foto)    # introduim la foto a l'etiqueta abans creada
    etiqueta_foto.image = foto


def fotoSeguent():
    global index_foto                   # declarem la variable global per modificar-la a la funcio
    if index_foto < len(fotos) - 1:     # si l'index es menor a la longuitud de la llista de fotos
        index_foto += 1                 # hi ha mes fotos per mostrar, incrementem l'index
        mostrarFoto(index_foto)         # cridem a la funcio de mostrar foto
        actualitzarEtiqueta()           # actualitzem l'etiqueta amb la nova foto
        actualitzarBoto()               # actualitzem el boto


def fotoAnterior():
    global index_foto
    if index_foto > 0:                  # si l'index es major a 0
        index_foto -= 1                 # hi ha fotos anteriors, restem l'index
        mostrarFoto(index_foto)
        actualitzarEtiqueta()
        actualitzarBoto()


def actualitzarBoto():
    if index_foto == len(fotos) - 1:        # si l'index es igual a la longitud de la llista
        boto_seguent.config(tk.DISABLED)    # no hi ha mes fotos, deshabilitem

    elif index_foto == 0:                   # si l'index es igual a 0
        boto_anterior.config(tk.DISABLED)   # no hi ha fotos anteriors, deshabilitem


def actualitzarEtiqueta():
    # actualitza l'etiqueta agafant l'index +1 de la llista perque no començi de 0
    etiqueta_estado.config(text=f'Imatge {index_foto + 1} de {len(fotos)}')


# crea i posiciona el text que indica la numeracio de fotos
etiqueta_estado = tk.Label(finestra, bd=1, relief=tk.SUNKEN, anchor=tk.E)
etiqueta_estado.pack(fill=tk.X)


# crea els 3 botons, els posiciona, i crida a les funcions pertinents per fer les comandes
boton_salir = tk.Button(finestra, text="Sortir", command=finestra.quit)
boton_salir.pack()
boto_seguent = tk.Button(finestra, text="Següent fotografia", command=fotoSeguent)
boto_seguent.pack(side=tk.RIGHT)
boto_anterior = tk.Button(finestra, text="Fotografia anterior", command=fotoAnterior)
boto_anterior.pack(side=tk.LEFT)

# actualitza tot al final del bucle
actualitzarBoto()
actualitzarEtiqueta()
mostrarFoto(index_foto)

finestra.mainloop()
