import tkinter
finestra = tkinter.Tk()

nom = tkinter.Entry(finestra, )
# fem que dins del quadre de text apareixi la frase seguent
nom.insert(0, 'introdueix aqui el teu nom')
nom.pack()


def accio():
    text = tkinter.Label(finestra, text='el teu nom es ' + nom.get())
    text.pack()


boto = tkinter.Button(finestra, text='click per que et digui el teu nom', command=accio)
boto.pack()

finestra.mainloop()
