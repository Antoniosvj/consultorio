import tkinter as tk
from tkinter import ttk
from crud import AppBD
from appcaixa import livroCaixa
from appFicha import fichaPaciente

class ConsultorioApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Consultório Odontológico')
        self.root.geometry('1200x680')
        self.AppBD = AppBD()
        self.setup_widgets()
        self.carregar_dados()
        
    def carregar_dados(self):
        try:
            pacientes = self.AppBD.carregarPacientes()  
        
            for paciente in pacientes:
                self.tree.insert('', 'end', values=(
                    paciente[0],
                    paciente[1],
                    paciente[2],
                    paciente[3],
                    paciente[4],
                    paciente[5]
                ))
        except Exception as e:
            print('Erro ao carregar dados: ', e)

    def limpar_campos(self):
        self.txtId.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtDataNascimento.delete(0, tk.END)
        self.txtTelefone.delete(0, tk.END)
        self.txtCpf.delete(0, tk.END)
        self.txtResponsavel.delete(0, tk.END)
    
    def f_adicionar(self):
        self.limpar_campos()
        
    def f_abrir(self):
        fichaPaciente()
    
    def f_editar(self):
        print('editado')
    
    def f_excluir(self):
        print('excluido')
    
    def f_caixa(self):
        livroCaixa()
        
    def on_treeview_double_click(self, event):
        #obter item selecionado e seus valores
        item = self.tree.selection()[0]
        valores = self.tree.item(item, 'values')
        
        self.limpar_campos()
        #preencher campos com os dados selecionados
        self.txtId.insert(0, valores[0])
        self.txtNome.insert(0, valores[1])
        self.txtDataNascimento.insert(0, valores[2])
        self.txtTelefone.insert(0, valores[3])
        self.txtCpf.insert(0, valores[4])
        self.txtResponsavel(0, valores[5])
        
    
    def setup_widgets(self):
        # labels e entry
        self.lblId = tk.Label(self.root, text='Id:', font=14)
        self.lblId.place(x=50, y=50)
        self.txtId = ttk.Entry(font=14)
        self.txtId.place(x=80, y=50, width=100, height=25)
        
        self.lblNome = tk.Label(self.root, text='Nome:', font=14)
        self.lblNome.place(x=200, y= 50)
        self.txtNome = ttk.Entry(font=14)
        self.txtNome.place(x=260, y=50, width=400, height=25)
        
        self.lblResponsavel = tk.Label(self.root, text='Responsável:', font=14)
        self.lblResponsavel.place(x=700, y=50)
        self.txtResponsavel = tk.Entry(self.root, font=14)
        self.txtResponsavel.place(x=820, y=50, width=300, height=25)
        
        self.lblDataNascimento = tk.Label(self.root, text='Data de Nascimento:', font=14)
        self.lblDataNascimento.place(x=300, y=100)
        self.txtDataNascimento = ttk.Entry(font=14)
        self.txtDataNascimento.place(x=470, y=100, width=150, height=25)
        
        self.lblTelefone = tk.Label(self.root, text='Telefone:', font=14)
        self.lblTelefone.place(x=50, y=100)
        self.txtTelefone = ttk.Entry(font=14)
        self.txtTelefone.place(x=130, y=100, width=150, height=25)
        
        self.lblCpf = tk.Label(self.root, text='Cpf:', font=14)
        self.lblCpf.place(x=650, y=100)      
        self.txtCpf = ttk.Entry(font=14)
        self.txtCpf.place(x=700, y=100, width=150, height=25)
        
        #criar e adicionar botões na tela
        self.btnLimpar = ttk.Button(self.root, text='Limpar Campos', command=self.limpar_campos)
        self.btnLimpar.place(x=30, y=150, width=100, height=25)
        
        self.btnAdicionar = ttk.Button(self.root, text='Adicionar', command=self.f_adicionar)
        self.btnAdicionar.place(x=220, y=150, width=100, height=25)
        
        self.btnAbrir = ttk.Button(self.root, text='Abrir Ficha', command=self.f_abrir)
        self.btnAbrir.place(x=420, y=150, width=100, height=25)
        
        self.btnEditar = ttk.Button(self.root, text='Editar Cadastro', command=self.f_editar)
        self.btnEditar.place(x=620, y=150, width=100, height=25)
        
        self.btnExcluir = ttk.Button(self.root, text='Excluir Cadastro', command=self.f_excluir)
        self.btnExcluir.place(x=820, y=150, width=100, height=25)
        
        self.btnCaixa = ttk.Button(self.root, text='Livro Caixa', command=self.f_caixa)
        self.btnCaixa.place(x=1060, y=150, width=100, height=25)
        
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
        
        #evento duplo click
        self.tree.bind("<Double-1>", self.on_treeview_double_click)

def main():
    root = tk.Tk()
    app = ConsultorioApp(root)
    root.mainloop()
    
if __name__=='__main__':
    main()
