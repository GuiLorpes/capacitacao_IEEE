import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Cursos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               nivel TEXT NOT NULL,
               duracao INTERGER NOT NULL,
               vagas INTERGER NOT NULL,
               carga_horaria INTERGER NOT NULL)
                ''')

print("Banco de dados e tabela 'Cursos' criados!")

conexao.commit()
conexao.close()