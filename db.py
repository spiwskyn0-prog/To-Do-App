import sqlite3 as lite

# Criando Banco de Dados
connector = lite.connect("lista.db")


def inserir(i):
    with connector:
        cur = connector.cursor()
        query = "INSERT INTO tarefa(nome) VALUES (?)"
        cur.execute(query, i)


def selecionar():
    lista_tarefa = []
    with connector:
        cur = connector.cursor()
        cur.execute("SELECT * FROM tarefa")
        row = cur.fetchall()
        for r in row:
            lista_tarefa.append(r)
    return lista_tarefa


def deletar(i):
    with connector:
        cur = connector.cursor()
        query = "DELETE FROM tarefa WHERE id = ?"
        cur.execute(query, i)


def atualizar(i):
    with connector:
        cur = connector.cursor()
        query = "UPDATE tarefa SET nome = ? WHERE id = ?"
        cur.execute(query, i)


#with connector:
#    cur = connector.cursor()
#    cur.execute("CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

