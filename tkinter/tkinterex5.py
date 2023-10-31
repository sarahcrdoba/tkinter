import tkinter
finestra = tkinter.Tk()

# primer creem un quadre de text per escriure el nom
nom = tkinter.Entry(finestra, )
nom.pack()


def accio():    # fem una funcio que ens monstri per text el nom introduit
    text = tkinter.Label(finestra, text='el teu nom es ' + nom.get())   # nom.get per agafar el text
    text.pack()


boto = tkinter.Button(finestra, text='introdueix el teu nom', command=accio)
boto.pack()
# quan presionem el boto crida a la funcio

finestra.mainloop()
