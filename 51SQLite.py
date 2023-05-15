import os
import sqlite3
from sqlite3 import Error

os.system('cls')

# Criar conexão
def ConexaoBanco():
    caminho = "C:\\Users\\Renato Augusto\\OneDrive\\Github\\Python\\DB\\agenda.db"
    con = None
    try:
          con = sqlite3.connect(caminho)  
    except Error as ex:
         print(ex)   
    return con      

vcon = ConexaoBanco()

#ATUALIZAR (UPDATE)
def update(conexao, sql):
      try:
         c = conexao.cursor()  
         c.execute(sql)
         conexao.commit()
         print("Registro atualizado")
      except Error as ex:
           print(ex)     


vsql = "UPDATE tb_contatos SET T_NOMECONTATO='Sergio Sacani', T_TELEFONECONTATO = '31 12345678' WHERE N_IDCONTATO=1"
update(vcon,vsql)
