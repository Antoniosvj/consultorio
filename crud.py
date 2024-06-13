import sqlite3 as conector

class AppBD:
    def __init__(self):
        pass
    
    def abrirConexao(self):
        try:
            self.conn = conector.connect('consultorio.db')
            self.cursor = self.conn.cursor()
            
            print('Conexão estabelecida')
        except (Exception, conector.Error) as error:
            print('Erro ao conectar ao banco de dados', error)
    
    def fecharConexao(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print('Conexão fechada')
    
    def criarTabela(self):
        try:
            self.abrirConexao()
            comando = '''CREATE TABLE pacientes (
                id INTEGER NOT NULL PRIMARY KEY,
                nome TEXT NOT NULL,
                dataNascimento DATE,
                telefone TEXT NOT NULL,
                cpf INTEGER,
                responsavel TEXT
            );'''
           self.cursor.execute(comando) 
        except(Exception, conector.Error) as error:
            print('Erro ao conectar ao banco de dados')
        finally:
            self.fecharConexao()
