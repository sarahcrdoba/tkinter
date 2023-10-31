import tkinter as tk
from tkinter import messagebox

finestra = tk.Tk()
etiqueta = tk.Label(finestra, text="")
etiqueta.pack()


# utilitzem messagebox.askquestion i canviem els booleans per si/no
# askquestion mostra si/no en l'alerta
def mostrarPregunta():
    resposta = messagebox.askquestion('ask question', 'vols continuar?')
    if resposta:
        etiqueta.config(text='has clicat si')
    else:
        etiqueta.config(text='has clicat no')


# utilitzem messagebox.askokcancel i canviem els booleans per si/no
# askokcancel mostra aceptar/cancelar en l'alerta
def mostrarOkCancel():
    resposta = messagebox.askokcancel('ask ok/cancel', 'vols continuar?')
    if resposta:
        etiqueta.config(text='has clicat si')
    else:
        etiqueta.config(text='has clicat no')


# utilitzem messagebox.askyesno i canviem els booleans per si/no
# askyesno mostra si/no en l'alerta
def mostrarYesNo():
    resposta = messagebox.askyesno('ask yes/no', 'vols continuar?')
    if resposta:
        etiqueta.config(text='has clicat si')
    else:
        etiqueta.config(text='has clicat no')


# utilitzem messagebox.showinfo
# showinfo mostra aceptar en l'alerta
def mostrarInfo():
    messagebox.showinfo('show info', 'informacio sobre aquest avis')
    etiqueta.config(text="has vist una finestra d'informació")


# crea els botons que criden a les funcions
boto_pregunta = tk.Button(finestra, text="ask question", command=mostrarPregunta)
boto_pregunta.pack()
boto_okcancel = tk.Button(finestra, text="ask ok/cancel", command=mostrarOkCancel)
boto_okcancel.pack()
botoyesno = tk.Button(finestra, text="ask yes/no", command=mostrarYesNo)
botoyesno.pack()
botoInfo = tk.Button(finestra, text="show info", command=mostrarInfo)
botoInfo.pack()

finestra.mainloop()
