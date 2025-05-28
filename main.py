from pydoc import text
import tkinter as tk
from tkinter import font
def mostrar_opcao(botao):
    rotulo.config(text=f"Escolheu: {botao}")
    
    if opcao1.get() and opcao2.get() and opcao3.get():
        if botao == "Saúde":
            opcao1.set(False)
            texto = "Dinheiro"
            
janela = tk.Tk()
janela.title("Exemplo Radiobutton")
janela.geometry("250x150")
opcao1 = tk.BooleanVar()
opcao2 = tk.BooleanVar()
opcao3 = tk.BooleanVar()

tk.Radiobutton(janela, text="Tempo", variable=opcao1, value=True, command=lambda:mostrar_opcao("Tempo")).pack()
tk.Radiobutton(janela, text="Dinhero", variable=opcao2, value=True, command=lambda: mostrar_opcao("Dinheiro")).pack()
tk.Radiobutton(janela, text="Saúde", variable=opcao3, value=True, command=lambda: mostrar_opcao("Saúde")).pack()
rotulo = tk.Label(janela, text="Escolheu:")
rotulo.pack(pady=10)
janela.mainloop()