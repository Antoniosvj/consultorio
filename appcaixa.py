import tkinter as tk
from tkinter import ttk, messagebox

def livroCaixa():
    # Esta função abrirá uma nova janela para o Livro Caixa
    root = tk.Tk()
    root.title('Livro Caixa')
    root.geometry('800x600')

    # Exemplos de widgets
    lblTitulo = tk.Label(root, text='Livro Caixa', font=('Arial', 24))
    lblTitulo.pack(pady=20)

    # Aqui você pode adicionar lógica para exibir e manipular registros financeiros

    root.mainloop()
