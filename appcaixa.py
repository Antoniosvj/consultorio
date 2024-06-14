import tkinter as tk

class LivroCaixa:
    def __init__(self, root):
        self.root = root
        self.root.title('Livro Caixa Consultório')
        self.root.geometry('1200x680')
        
        
def livroCaixa():
    root = tk.Tk()
    app = LivroCaixa(root)
    root.mainloop()
 
