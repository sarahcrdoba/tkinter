import tkinter

finestra = tkinter.Tk()
finestra2 = tkinter.Tk()
finestra2.title('nova finestra')    # nom de la finestra

# es crea una funcio que reproduira el text quan se la cridi
def accio():
    text = tkinter.Label(finestra2, text='hola')
    # finestra2 fa que el text surti en una nova finestra
    text.pack()

# en clicar al boto crida a accio i llavors surt el text
boto = tkinter.Button(finestra, text='acceptar', command=accio)
boto.pack()
finestra.mainloop()
