import tkinter as tk
from tkinter import filedialog as quelcom
from PIL import Image, ImageTk

finestra = tk.Tk()
finestra.geometry("300x100")


def obrir_imatge():
    # demana a l'usuari que seleccioni a partir de la ruta i formats acceptats de les imatges
    imatge_path = quelcom.askopenfilename(initialdir='.', title='Selecciona una imatge', filetypes=(('Imatges', '*.jpg *.jpeg *.png *.gif'), ('Tots els arxius', '*.*')))

    # si es selecciona una, s'obre una nova finestra per mostrar-la i ensenyar el path d'on prove
    if imatge_path:
        finestra2 = tk.Toplevel()
        label_path = tk.Label(finestra2, text='Path de la imatge: ' + imatge_path)
        label_path.pack()

        # obrim i fem resize (les fotos de l'activitat 2 són massa grans)
        imatge = Image.open(imatge_path)
        imatge.resize((300, 300))
        imatge_tk = ImageTk.PhotoImage(imatge)

        # posem la foto a la finestra
        label_imatge = tk.Label(finestra2, image=imatge_tk)
        label_imatge.image = imatge_tk
        label_imatge.pack()

        # la funcio la fem servir quan ja s'ha obert una imatge, llavors crea el boto i es pot guardar
        def guardar_imatge():
            imatge_guardar = quelcom.asksaveasfile(defaultextension='.png', filetypes=(('Imatges PNG', '*.png'), ('Tots els arxius', '*.*')))
            if imatge_guardar:
                imatge.save(imatge_guardar.name)

        boto_guardar = tk.Button(finestra2, text="Guardar Imatge", command=guardar_imatge)
        boto_guardar.pack()


# crea el boto per accedir a les imatges
obrir_boto = tk.Button(finestra, text='Obrir Imatge', command=obrir_imatge)
obrir_boto.pack()

finestra.mainloop()
