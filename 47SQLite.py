#Site para Download do SQLite : sqlitestudio.pl

import sqlite3
from sqlite3 import Error

#### Criar conexão
def ConexaoBanco():
    caminho="C:\\Users\\Renato Augusto\\OneDrive\\Github\\Python\\DB\\agenda.db"
    con=None
    try:
          con=sqlite3.connect(caminho)  
    except Error as ex:
         print(ex)   
    return con      

vcon=ConexaoBanco()

## Criar Tabela
vsql = """CREATE TABLE tb_contatos (
    N_IDCONTATO       INTEGER   PRIMARY KEY,
    T_NOMECONTATO     TEXT (30),
    T_TELEFONECONTATO TEXT (14),
    T_EMAILCONTATO    TEXT (30) 
);"""

def CriarTabela(conexao,sql):
    try:
         c = conexao.cursor()
         c.execute(sql)
         print("Tabela Criada")

    except Error as ex:
         print(ex) 

CriarTabela(vcon,vsql)

vcon.close()        