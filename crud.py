import sqlite3 as conector

class AppBD:
    def __init__(self):
        self.conn = None
        self.cursor = None
    
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
            comando = '''CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                dataNascimento DATE,
                telefone TEXT NOT NULL,
                cpf TEXT,
                responsavel TEXT
            );'''
            self.cursor.execute(comando)
            self.conn.commit()
            print('Tabela pacientes criada com sucesso')
        except (Exception, conector.Error) as error:
            print('Erro ao criar a tabela', error)
        finally:
            self.fecharConexao()

    def adicionarPaciente(self, nome, dataNascimento, telefone, cpf, responsavel):
        try:
            self.abrirConexao()
            comando = '''INSERT INTO pacientes (nome, dataNascimento, telefone, cpf, responsavel)
                         VALUES (?, ?, ?, ?, ?);'''
            self.cursor.execute(comando, (nome, dataNascimento, telefone, cpf, responsavel))
            self.conn.commit()
            print('Paciente adicionado com sucesso')
        except (Exception, conector.Error) as error:
            print('Erro ao adicionar paciente', error)
        finally:
            self.fecharConexao()
    
    def carregarPacientes(self):
        pacientes = []
        try:
            self.abrirConexao()
            comando = '''SELECT * FROM pacientes'''
            self.cursor.execute(comando)
            pacientes = self.cursor.fetchall()
        except (Exception, conector.Error) as error:
            print('Erro ao conectar ao banco de dados', error)
        finally:
            self.fecharConexao()
            return pacientes
            
    def atualizarPaciente(self, id, nome, dataNascimento, telefone, cpf, responsavel):
        try:
            self.abrirConexao()
            comando = '''UPDATE pacientes SET
                        nome = ?,
                        dataNascimento = ?,
                        telefone = ?,
                        cpf = ?,
                        responsavel = ?
                        WHERE id = ?'''
            self.cursor.execute(comando, (nome, dataNascimento, telefone, cpf, responsavel, id))
            self.conn.commit()
            print('Atualização realizada com sucesso.')
        except (Exception, conector.Error) as error:
            print('Erro ao conectar ao banco de dados')
        finally:
            self.fecharConexao()
            
    def deletarPaciente(self, id):
        try:
            self.abrirConexao()
            comando = '''DELETE FROM pacientes WHERE id = ?;'''
            self.cursor.execute(comando, (id,))
            self.conn.commit()
            print('paciente deletado')
        except (Exception, conector.Error) as error:
            print('Erro ao conectar ao banco de dados')
        finally:
            self.fecharConexao()
