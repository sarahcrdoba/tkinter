import tkinter

finestra = tkinter.Tk()     # crea la finestra
etiqueta = tkinter.Label(finestra, text='hola')     # indiquem un text a la finestra
etiqueta.pack()     # posa el label (text) a la finestra de forma visual
finestra.mainloop()     # inici del loop de la finestra
