import tkinter

finestra = tkinter.Tk()
etiqueta = tkinter.Label(finestra, text='holi')
etiqueta.grid(row=1, column=1)      # defineix la posicio de la etiqueta (text)

etiqueta1 = tkinter.Label(finestra, text='adeu')
etiqueta1.grid(columnspan=9, rowspan=8)

finestra.mainloop()
