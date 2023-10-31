import tkinter as tk

# creem una finestra i una entrada amb un format especific
finestra = tk.Tk()
entrada = tk.Entry(finestra, width=20)
entrada.grid(row=0, column=0, columnspan=4)


# funcio que permet concatenar els numeros i operadors
def click(numero):
    num = entrada.get()
    entrada.delete(0, 'end')    # borra els primers numeros per poder afegir de nous desprès de posar l'operador
    entrada.insert(0, num + numero)


# funcio que permet calcular, i donar el resultat o l'error
def calcular():
    try:
        operacio = entrada.get()
        resultat = eval(operacio)  # eval() permet llegir una cadena de text i retornar el resultat
        entrada.delete(0, 'end')
        entrada.insert(0, resultat)
    except Exception:
        entrada.delete(0, 'end')
        entrada.insert(0, "Error")


# funcio que elimina el quadre de text en cas que vulguem
def limpiar():
    entrada.delete(0, 'end')


def get_command(boton):
    if boton != '=':
        return lambda: click(boton)
    elif boton == 'C':
        limpiar()
    else:
        return calcular


botons = [      # llista amb els botons necessaris per fer una calculadora
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

fila = 1
columna = 0

for boton in botons:
    comando = get_command(boton)
    boton = tk.Button(finestra, text=boton, padx=20, pady=20, command=comando)
    boton.grid(row=fila, column=columna)
    columna += 1

    if columna > 3:
        columna = 0
        fila += 1


finestra.mainloop()
