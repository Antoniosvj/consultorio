import tkinter as tk
from tkinter import ttk
#from crud import AppBD
from appcaixa import livroCaixa
from appFicha import fichaPaciente

class ConsultorioApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Consultório Odontológico')
        self.root.geometry('1200x680')
        self.setup_widgets()
        #self.AppBD()
        #self.AppBD.criarTabela()
        
    def f_adicionar(self):
        pass
    
    def f_abrir(self):
        fichaPaciente()
    
    def f_editar(self):
        print('editado')
    
    def f_excluir(self):
        print('excluido')
    
    def f_caixa(self):
        livroCaixa()
    
    def setup_widgets(self):
        # labels
        self.lblId = tk.Label(self.root, text='Id:', font=14)
        self.lblNome = tk.Label(self.root, text='Nome:', font=14)
        self.lblDataNascimento = tk.Label(self.root, text='Data de Nascimento:', font=14)
        self.lblTelefone = tk.Label(self.root, text='Telefone:', font=14)
        self.lblCpf = tk.Label(self.root, text='Cpf:', font=14)
        
        # entry
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
        self.btnAdicionar = ttk.Button(self.root, text='Adicionar', command=self.f_adicionar)
        self.btnAdicionar.place(x=50, y=150, width=100, height=25)
        
        self.btnAbrir = ttk.Button(self.root, text='Abrir Ficha', command=self.f_abrir)
        self.btnAbrir.place(x=300, y=150, width=100, height=25)
        
        self.btnEditar = ttk.Button(self.root, text='Editar Cadastro', command=self.f_editar)
        self.btnEditar.place(x=550, y=150, width=100, height=25)
        
        self.btnExcluir = ttk.Button(self.root, text='Excluir Cadastro', command=self.f_excluir)
        self.btnExcluir.place(x=800, y=150, width=100, height=25)
        
        self.btnCaixa = ttk.Button(self.root, text='Livro Caixa', command=self.f_caixa)
        self.btnCaixa.place(x=1050, y=150, width=100, height=25)
        
        #tabela dos pacientes
        self.tree = ttk.Treeview(self.root, columns=('id', 'nome', 'dataNascimento', 'telefone', 'cpf', 'responsavel'),
                                 show='headings')
        
        #cabeçalho da coluna
        self.tree.heading('id', text='ID')
        self.tree.heading('nome', text='Nome')
        self.tree.heading('dataNascimento', text='Data de Nascimento')
        self.tree.heading('telefone', text='Telefone')
        self.tree.heading('cpf', text='CPF')
        self.tree.heading('responsavel', text='Responsável')
        
        #largura da coluna
        self.tree.column('id', width=30)
        self.tree.column('nome', width=400)
        self.tree.column('dataNascimento', width=150)
        self.tree.column('telefone', width=150)
        self.tree.column('cpf', width=150)
        self.tree.column('responsavel', width=250)
        
        #localização da tabela
        self.tree.place(x=10, y=200, width=1160, height=450)

def main():
    root = tk.Tk()
    app = ConsultorioApp(root)
    root.mainloop()
    
if __name__=='__main__':
    main()
