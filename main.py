import sqlite3 as conexao
from tkinter import ttk
from tkinter import *
    
root = Tk()

class Funcs():
    def limpar_tela(self):
        self.entry_cod.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_telefone.delete(0, END)
        self.entry_cpf.delete(0, END)
    def conecta_bd(self):
        self.conn = conexao.connect('cadastro_cliente.db')
        self.cursor = self.conn.cursor()
        print('Conectando ao banco de dados.')
    def desconecta_bd(self):
        self.cursor.close()
        self.conn.close()
        print('Banco de dados desconectado.')
    def montar_tabela(self):
        self.conecta_bd()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cadastro_clientes (
                    id INTEGER NOT NULL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    telefone INTEGER(20),
                    cpf INTEGER(12));
                    ''')
        self.conn.commit()
        print('Banco de dados criado.')
        self.desconecta_bd()
    def add_cliente(self):
        self.cod = self.entry_cod.get()
        self.nome = self.entry_nome.get()
        self.telefone = self.entry_telefone.get()
        self.cpf = self.entry_cpf.get()

        self.conecta_bd()
        self.cursor.execute('''INSERT INTO cadastro_clientes (nome, telefone, cpf) VALUES (?, ?, ?)''', (self.nome, self.telefone, self.cpf))
        self.conn.commit()
        print('Cadastro salvo com sucesso')
        self.desconecta_bd()
        self.select_lista()
        self.limpar_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute('''SELECT id, nome, telefone, cpf from cadastro_clientes ORDER BY nome ASC''')
        for i in lista:
            self.listaCli.insert('', END, values=i)
        self.desconecta_bd()

class Aplication(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame()
        self.widgets_frame()
        self.frame_lista_clientes()
        self.montar_tabela()
        self.select_lista()
        self.root.mainloop()

    def tela(self):
        self.root.title('Consultório Odontológico')
        self.root.configure(background='#4D869C')
        self.root.geometry('1200x650')
        self.root.resizable(False, False)

    def frame(self):
        self.frame_cadastro = Frame(self.root, bd=4, bg='#eef7ff')
        self.frame_cadastro.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.4)

        self.frame_lista = Frame(self.root, bd=4, bg='#eef7ff')
        self.frame_lista.place(relx=0.03, rely=0.45, relwidth=0.94, relheight=0.5)

    def widgets_frame(self):
        # Botão Buscar
        self.btn_buscar = Button(self.frame_cadastro, text='Buscar', bg='#7AB2B2', bd=2, activebackground='#CDE8E5', foreground='#fff',font='Helvetica')
        self.btn_buscar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.13)

        # Botão Limpar Tela
        self.btn_limpa = Button(self.frame_cadastro, text='Limpar', font='Helvetica', bg='#7ab2b2', bd=2, activebackground='#cde8e5', foreground='#fff', command=self.limpar_tela)
        self.btn_limpa.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.13)

        # Botão Salvar Cadastro
        self.btn_salvar = Button(self.frame_cadastro, text='Salvar Cadastro', bg='#7AB2B2', bd=2, activebackground='#CDE8E5', foreground='#fff', font='Helvetica', command=self.add_cliente)
        self.btn_salvar.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.13)

        # Botão excluir Cadastro
        self.btn_excluir = Button(self.frame_cadastro, text='Excluir', bg='#fa7070', bd=2, activebackground='#fa7171', foreground="#fff", font='Helvetica')
        self.btn_excluir.place(relx=0.65, rely=0.1, relwidth=0.1, relheight=0.13)

        #Botão Livro Caixa
        self.btn_caixa = Button(self.frame_cadastro, text='Livro Caixa', bg='#7ab2b2', bd=2, activebackground='#cde8e5', foreground='#fff', font='Helvetica')
        self.btn_caixa.place(relx=0.8, rely=0.1, relwidth=0.16, relheight=0.13)

        #Código
        self.label_cod = Label(self.frame_cadastro, text='Código', font='Helvetica', bg='#eef7f7')
        self.label_cod.place(relx=0.1, rely=0.02)

        self.entry_cod = Entry(self.frame_cadastro, font='Helvetica')
        self.entry_cod.place(relx=0.1, rely=0.1, relwidth=0.05, relheight=0.13)

        # Nome
        self.label_nome = Label(self.frame_cadastro,text='Nome', font='Helvetica', bg='#eef7f7')
        self.label_nome.place(relx=0.1, rely=0.4)

        self.entry_nome = Entry(self.frame_cadastro, font='Helvetica')
        self.entry_nome.place(relx=0.1, rely=0.5, relwidth=0.6, relheight=0.13)

        # Telefone
        self.label_telefone = Label(self.frame_cadastro, text='Telefone', font='Helvetica', bg="#eef7f7")
        self.label_telefone.place(relx=0.1, rely=0.7)

        self.entry_telefone = Entry(self.frame_cadastro, font='Helvetica')
        self.entry_telefone.place(relx=0.1, rely=0.8, relwidth=0.2, relheight=0.13)

        #CPF
        self.label_cpf = Label(self.frame_cadastro, text='CPF', font='Helvetica', bg='#eef7f7')
        self.label_cpf.place(relx=0.5, rely=0.7)

        self.entry_cpf = Entry(self.frame_cadastro, font='Helvetica')
        self.entry_cpf.place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.13)
    def frame_lista_clientes(self):
        self.listaCli = ttk.Treeview(self.frame_lista, height=3, column=('col1', 'col2', 'col3', 'col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Código')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='CPF')

        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)

        self.listaCli.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.98)

        self.scrollLista = Scrollbar(self.frame_lista, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.01, relwidth=0.03, relheight=0.95)

Aplication()