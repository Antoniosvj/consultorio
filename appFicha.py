import tkinter as tk
from tkinter import ttk, messagebox
from crud import AppBD

class FichaPaciente:
    def __init__(self, root, paciente_id, paciente_nome):
        self.root = root
        self.root.title(f'Ficha Paciente - {paciente_nome}')
        self.root.geometry('1410x720')
        self.paciente_id = paciente_id
        self.paciente_nome = paciente_nome
        self.AppBD = AppBD()
        self.setup_widgets()
        self.carregar_dados()
        
    def limpar_campos(self):
        self.txtDente.delete(0, tk.END)
        self.txtProcedimento.delete(0, tk.END)
        self.txtValor.delete(0, tk.END)
        self.txtObs.delete(0, tk.END)
        self.txtData.delete(0,tk.END)
        
    def carregar_dados(self):
        try:
            # Carrega os tratamentos do paciente específico
            tratamentos = self.AppBD.carregarTratamento(self.paciente_id)
            
            # Limpa o Treeview antes de inserir os novos dados
            self.tree.delete(*self.tree.get_children())
            
            #carregar total tratamento
            total_tratamento = 0.0
            
            # Insere os tratamentos no Treeview
            for tratamento in tratamentos:
                self.tree.insert('', 'end', values=(
                    tratamento[1],  # data
                    tratamento[2],  # Dente
                    tratamento[3],  # Procedimento
                    tratamento[4],  # Valor
                    tratamento[5]   # Observação
                ))
                
                total_tratamento +=float(tratamento[4])
            
            #atualizar dados total
            self.lblTotal.config(text=f'R${total_tratamento:.2f}')
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao carregar tratamentos: {e}')

        
    def atualizar_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Adicione os novos dados
        for tratamento in self.tratamento:
            self.tree.insert('', 'end', values=tratamento)

        
    def f_adicionar(self):
        dente = self.txtDente.get()
        procedimento = self.txtProcedimento.get()
        valor = self.txtValor.get()
        observacao = self.txtObs.get()
        data = self.txtData.get()
        id_paciente = self.paciente_id
        
        try:
            self.AppBD.adicionarTratamento(data, dente, procedimento, valor, observacao, id_paciente)
            self.carregar_dados()
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao adicionar o tratamento.{e}',e)
        finally:
            self.limpar_campos()
            
    def f_excluir(self):
        pass
    
    def f_editar(self):
        pass
        
        
    def setup_widgets(self):
        self.lblId = tk.Label(self.root, text=f'Id: {self.paciente_id}', font=14)
        self.lblId.place(x=50, y=30)

        self.lblNome = tk.Label(self.root, text=f'Nome: {self.paciente_nome}', font=14)
        self.lblNome.place(x=150, y=30)

        self.nb = ttk.Notebook(self.root)
        self.nb.place(x=20, y=100, width=800, height=570)

        self.orcamento = ttk.Frame(self.nb)
        self.nb.add(self.orcamento, text='Orçamento / Tratamento')

        self.anamnese = ttk.Frame(self.nb)
        self.nb.add(self.anamnese, text='Anamnese')
        
        self.tratamento = ttk.Frame(self.nb)
        self.nb.add(self.tratamento, text='Tratamentos Anteriores')

        self.lblDente = tk.Label(self.orcamento, text='Dente:', font=14)
        self.lblDente.place(x=10, y=20)

        self.txtDente = tk.Entry(self.orcamento, font=14)
        self.txtDente.place(x=80, y=20, width=50, height=25)

        self.lblProcedimento = tk.Label(self.orcamento, text='Procedimento:', font=14)
        self.lblProcedimento.place(x=150, y=20)

        self.txtProcedimento = tk.Entry(self.orcamento, font=14)
        self.txtProcedimento.place(x=280, y=20, width=250, height=25)

        self.lblValor = tk.Label(self.orcamento, text='Valor:', font=14)
        self.lblValor.place(x=550, y=20)

        self.txtValor = tk.Entry(self.orcamento, font=14)
        self.txtValor.place(x=620, y=20, width=150, height=25)
        
        self.lblObs = tk.Label(self.orcamento, text='Obs.', font=14)
        self.lblObs.place(x=10, y=70)
        
        self.txtObs = ttk.Entry(self.orcamento, font=14)
        self.txtObs.place(x=50, y=70, height=25, width=480)
        
        self.lblData = tk.Label(self.orcamento, text='Data', font=14)
        self.lblData.place(x=550, y=70)

        self.btnAdicionar = ttk.Button(self.orcamento, text='Adicionar', command=self.f_adicionar)
        self.btnAdicionar.place(x=30, y=120, width=200, height=25)
        
        self.txtData = ttk.Entry(self.orcamento, font=14)
        self.txtData.place(x=620, y=70, width=150, height=25)
        
        self.btnEditar = ttk.Button(self.orcamento, text='Editar', command=self.f_editar)
        self.btnEditar.place(x=300, y=120, width=200, height=25)
        
        self.btnExcluir = ttk.Button(self.orcamento, text='Exluir', command=self.f_excluir)
        self.btnExcluir.place(x=570, y=120, width=200, height=25)
        
        self.tree = ttk.Treeview(self.orcamento, columns=('data', 'dente', 'procedimento', 'valor', 'obs'), show='headings')
        self.tree.heading('data', text='DATA')
        self.tree.heading('dente', text='DENTE')
        self.tree.heading('procedimento', text='PROCEDIMENTO')
        self.tree.heading('valor', text='VALOR')
        self.tree.heading('obs', text='OBS')
    
        self.tree.column('data', width=70)
        self.tree.column('dente', width=50)
        self.tree.column('procedimento', width=200)
        self.tree.column('valor', width=50)
        self.tree.column('obs', width=330)

        self.tree.place(x=0, y=200, width=800, height=350)

        self.lblAnamnese = tk.Label (self.root, text='Anamnese:', font=14)
        self.lblAnamnese.place(x=850, y=30)
        
        self.lblPagamento = tk.Label(self.root, text='Pagamentos:', font=14)
        self.lblPagamento.place(x=850, y=350)
        
        self.treePagamento = ttk.Treeview(self.root, columns=('data', 'valor'), show='headings')
        self.treePagamento.heading('data', text='DATA')
        self.treePagamento.heading('valor', text='VALOR')
        
        self.treePagamento.column('data', width=150)
        self.treePagamento.column('valor', width=150)
        
        self.treePagamento.place(x=850, y=380, width=301, height=285)
        
        self.lblTotalTratamento = tk.Label(self.root, text='Total Tratamento:', font=14)
        self.lblTotalTratamento.place(x=1160, y=380)
        self.lblTotal = tk.Label(self.root, text='R$0.00', font=14)
        self.lblTotal.place(x=1160, y=430)
        
        self.lblTratamentoRealizado = tk.Label(self.root, text='Total Realizado:', font=14)
        self.lblTratamentoRealizado.place(x=1160, y=480)
        
        self.lblTotalPagamento = tk.Label(self.root, text='Total Pagamento:', font=14)
        self.lblTotalPagamento.place(x=1160, y=580)

def fichaPaciente(paciente_id, paciente_nome):
    root = tk.Tk()
    app = FichaPaciente(root, paciente_id, paciente_nome)
    root.mainloop()


