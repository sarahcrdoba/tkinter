import tkinter

finestra = tkinter.Tk()
# state pot habilitar o deshabilitar (normal o disabled)
# padx i pady defineixen el tamany del boto
boto = tkinter.Button(finestra, text='acceptar', state=tkinter.NORMAL, padx=10, pady=8)
boto.grid(row=8, column=2)

finestra.mainloop()
