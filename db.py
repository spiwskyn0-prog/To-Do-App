import sqlite3 as lite

# Criando Banco de Dados
connector = lite.connect("lista.db")

with connector:
    cur = connector.cursor()
    cur.execute("CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, nome, TEXT)")