import tkinter as tk
from tkinter import ttk
#from crud import AppBD


class ConsultorioApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Consultório Odontológico')
        self.root.geometry('1050x680')
        
        self.setup_widgets()
    
    def setup_widgets(self):
        #adição das labels
        self.lblId = tk.Label(self.root, text='Id:', font=14)
        self.lblNome = tk.Label(self.root, text='Nome:', font=14)
        self.lblDataNascimento = tk.Label(self.root, text='Data de Nascimento:', font=14)
        self.lblTelefone = tk.Label(self.root, text='Telefone:', font=14)
        self.lblCpf = tk.Label(self.root, text='Cpf:', font=14)
        
        #adição das entry
        self.txtId = ttk.Entry(font=14)
        self.txtNome = ttk.Entry(font=14)
        self.txtTelefone = ttk.Entry(font=14)
        self.txtDataNascimento = ttk.Entry(font=14)
        self.txtCpf = ttk.Entry(font=14)


        #adicionando na tela label e entry
        self.lblId.place(x=50, y=50)
        self.txtId.place(x=80, y=50, width=100, height=25)
        self.lblNome.place(x=300, y= 50)
        self.txtNome.place(x=360, y=50, width=600, height=25)
        self.lblTelefone.place(x=50, y=100)
        self.txtTelefone.place(x=130, y=100, width=150, height=25)
        self.lblDataNascimento.place(x=300, y=100)
        self.txtDataNascimento.place(x=470, y=100, width=150, height=25)
        self.lblCpf.place(x=650, y=100)
        self.txtCpf.place(x=700, y=100, width=150, height=25)
        
        #criar e adicionar botões na tela
        self.btnAdicionar = ttk.Button(self.root, text='Adicionar')
        self.btnAdicionar.place(x=50, y=150, width=100, height=25)
        
        self.btnAbrir = ttk.Button(self.root, text='Abrir Ficha')
        self.btnAbrir.place(x=250, y=150, width=100, height=25)
        
        self.btnEditar = ttk.Button(self.root, text='Editar Cadastro')
        self.btnEditar.place(x=450, y=150, width=100, height=25)
        
        self.btnExcluir = ttk.Button(self.root, text='Excluir Cadastro')
        self.btnExcluir.place(x=650, y=150, width=100, height=25)
        
        self.btnCaixa = ttk.Button(self.root, text='Livro Caixa')
        self.btnCaixa.place(x=850, y=150, width=100, height=25)

def main():
    root = tk.Tk()
    app = ConsultorioApp(root)
    
    root.mainloop()
    
if __name__=='__main__':
    main()