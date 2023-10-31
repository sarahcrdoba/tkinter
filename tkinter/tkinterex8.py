import tkinter
finestra = tkinter.Tk()

num = tkinter.Entry(finestra, )
num.pack()


def click_boto(numero):
    boto1 = tkinter.Button(finestra, text=numero)
    boto1.pack()
    num.delete(0, 'end')


boto = tkinter.Button(finestra, text='escriu un numero', command=lambda: click_boto(num.get()))
boto.pack()

finestra.mainloop()
