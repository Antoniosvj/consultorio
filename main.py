import tkinter as tk
from tkinter import ttk, messagebox
from crud import AppBD
from appcaixa import livroCaixa
from appFicha import fichaPaciente

class ConsultorioApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Consultório Odontológico')
        self.root.geometry('1200x680')
        self.pacientes = []
        self.AppBD = AppBD()
        self.setup_widgets()
        self.carregar_dados()

    def carregar_dados(self):
        try:
            self.tree.delete(*self.tree.get_children())
            self.pacientes = self.AppBD.carregarPacientes()
            self.pacientes_ordenados = sorted(self.pacientes, key=lambda x: x[1].lower())

            for paciente in self.pacientes_ordenados:
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

    def procurar(self, event=None):
        filtro = self.txtNome.get().lower()
        self.tree.delete(*self.tree.get_children())

        for paciente in self.pacientes:
            if filtro in paciente[1].lower():
                self.tree.insert('', 'end', values=(
                    paciente[0],
                    paciente[1],
                    paciente[2],
                    paciente[3],
                    paciente[4],
                    paciente[5]
                ))

    def limpar_campos(self):
        self.txtId.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtDataNascimento.delete(0, tk.END)
        self.txtTelefone.delete(0, tk.END)
        self.txtCpf.delete(0, tk.END)
        self.txtResponsavel.delete(0, tk.END)

    def f_adicionar(self):
        nome = self.txtNome.get()
        dataNascimento = self.txtDataNascimento.get()
        telefone = self.txtTelefone.get()
        cpf = self.txtCpf.get()
        responsavel = self.txtResponsavel.get()

        if nome and telefone:
            try:
                self.AppBD.adicionarPaciente(nome, dataNascimento, telefone, cpf, responsavel)
                self.carregar_dados()
                messagebox.showinfo('Adicionar', 'Paciente adicionado com sucesso!')
            except Exception as e:
                messagebox.showerror('Erro', f'Erro ao adicionar paciente: {e}')
            finally:
                self.limpar_campos()
        else:
            messagebox.showwarning('Erro', 'Os campos nome e telefone são obrigatórios.')

    def f_abrir(self):
        item = self.tree.selection()
        if item:
            paciente_id = self.tree.item(item, 'values')[0]
            paciente_nome = self.tree.item(item, 'values')[1]
            fichaPaciente(paciente_id, paciente_nome)
        else:
            messagebox.showwarning('Aviso', 'Selecione um paciente para abrir a ficha.')

    def f_editar(self):
        id = self.txtId.get()
        nome = self.txtNome.get()
        dataNascimento = self.txtDataNascimento.get()
        telefone = self.txtTelefone.get()
        cpf = self.txtCpf.get()
        responsavel = self.txtResponsavel.get()

        if id:
            try:
                self.AppBD.atualizarPaciente(id, nome, dataNascimento, telefone, cpf, responsavel)
                self.carregar_dados()
                messagebox.showinfo('Editar', 'Paciente atualizado com sucesso!')
            except Exception as e:
                messagebox.showerror('Erro', f'Erro ao editar paciente: {e}')
        else:
            messagebox.showwarning('Erro', 'Nenhum paciente selecionado para editar.')

    def f_excluir(self):
        id = self.txtId.get()

        if id:
            try:
                self.AppBD.deletarPaciente(id)
                self.carregar_dados()
                messagebox.showinfo('Excluir', 'Paciente excluído com sucesso.')
                self.limpar_campos()
            except Exception as e:
                messagebox.showerror('Erro', f'Erro ao excluir paciente: {e}')
        else:
            messagebox.showwarning('Erro', 'Nenhum paciente selecionado para excluir.')

    def f_caixa(self):
        livroCaixa()

    def on_treeview_double_click(self, event):
        item = self.tree.selection()[0]
        valores = self.tree.item(item, 'values')

        self.limpar_campos()
        self.txtId.insert(0, valores[0])
        self.txtNome.insert(0, valores[1])
        self.txtDataNascimento.insert(0, valores[2])
        self.txtTelefone.insert(0, valores[3])
        self.txtCpf.insert(0, valores[4])
        self.txtResponsavel.insert(0, valores[5])

    def setup_widgets(self):
        self.lblId = tk.Label(self.root, text='Id:', font=14)
        self.lblId.place(x=50, y=50)
        self.txtId = ttk.Entry(font=14)
        self.txtId.place(x=80, y=50, width=100, height=25)

        self.lblNome = tk.Label(self.root, text='Nome:', font=14)
        self.lblNome.place(x=200, y=50)
        self.txtNome = ttk.Entry(font=14)
        self.txtNome.place(x=260, y=50, width=400, height=25)
        self.txtNome.bind('<KeyRelease>', self.procurar)

        self.lblResponsavel = tk.Label(self.root, text='Responsável:', font=14)
        self.lblResponsavel.place(x=700, y=50)
        self.txtResponsavel = tk.Entry(self.root, font=14)
        self.txtResponsavel.place(x=820, y=50, width=300, height=25)

        self.lblTelefone = tk.Label(self.root, text='Telefone:', font=14)
        self.lblTelefone.place(x=50, y=100)
        self.txtTelefone = ttk.Entry(font=14)
        self.txtTelefone.place(x=130, y=100, width=150, height=25)

        self.lblDataNascimento = tk.Label(self.root, text='Data de Nascimento:', font=14)
        self.lblDataNascimento.place(x=300, y=100)
        self.txtDataNascimento = ttk.Entry(font=14)
        self.txtDataNascimento.place(x=470, y=100, width=150, height=25)

        self.lblCpf = tk.Label(self.root, text='Cpf:', font=14)
        self.lblCpf.place(x=650, y=100)
        self.txtCpf = ttk.Entry(font=14)
        self.txtCpf.place(x=700, y=100, width=150, height=25)

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

        self.tree = ttk.Treeview(self.root, columns=('id', 'nome', 'dataNascimento', 'telefone', 'cpf', 'responsavel'),
                                 show='headings')

        self.tree.heading('id', text='ID')
        self.tree.heading('nome', text='Nome')
        self.tree.heading('dataNascimento', text='Data de Nascimento')
        self.tree.heading('telefone', text='Telefone')
        self.tree.heading('cpf', text='CPF')
        self.tree.heading('responsavel', text='Responsável')

        self.tree.column('id', width=30)
        self.tree.column('nome', width=400)
        self.tree.column('dataNascimento', width=150)
        self.tree.column('telefone', width=150)
        self.tree.column('cpf', width=150)
        self.tree.column('responsavel', width=250)

        self.tree.place(x=10, y=200, width=1160, height=450)

        self.tree.bind("<Double-1>", self.on_treeview_double_click)

def main():
    root = tk.Tk()
    app = ConsultorioApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
