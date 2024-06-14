import tkinter as tk
from tkinter import ttk

id = '1'
nome = 'Antonio Sérgio Viana Júnior'

class FichaPaciente:
    def __init__(self, root):
        self.root = root
        self.root.title(f'Ficha Paciente - {nome}')
        self.root.geometry('1200x680')
        self.setup_widgets()
        
    def setup_widgets(self):
        #labels
        self.lblId = tk.Label(self.root, text=f'Id: {id}', font=14)
        self.lblId.place(x=50, y=30)

        self.lblNome = tk.Label(self.root, text=f'Nome: {nome}', font=14)
        self.lblNome.place(x=150, y=30)
      
        #Abas
        self.nb = ttk.Notebook(self.root)
        self.nb.place(x=20, y=100, width=800, height=570)
        
        self.orcamento = ttk.Frame(self.nb)
        self.nb.add(self.orcamento, text='Orçamento')
        
        self.tratamento = ttk.Frame(self.nb)
        self.nb.add(self.tratamento, text='Tratamento')
        
        self.pagamento = ttk.Frame(self.nb)
        self.nb.add(self.pagamento, text='Pagamentos')
        
        self.anamnese = ttk.Frame(self.nb)
        self.nb.add(self.anamnese, text='Anamnese')
        
        self.tratamentosAnteriores = ttk.Frame(self.nb)
        self.nb.add(self.tratamentosAnteriores, text='Tratamentos Anteriores')

        #widgets  da aba orcamento
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
        
        self.btnAdicionar = ttk.Button(self.orcamento, text='Adicionar')
        self.btnAdicionar.place(x=300, y=70, width=200, height=25)
        
        
        #widgets da aba tratamento

        #widgets da aba pagamento

        #widgets da aba anamnese

        #widgets da aba tratamentos anteriores        

def fichaPaciente():
    root = tk.Tk()
    app = FichaPaciente(root)
    root.mainloop()
