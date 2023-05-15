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
def consulta(conexao, sql):

         c = conexao.cursor()  
         c.execute(sql)
         #conexao.commit() #PAra SELECT nao necessita de COmmit por ser apenas uma consulta
         resultado=c.fetchall()
         print("Registro atualizado")
         return resultado
 
#"SELECT * FROM tb_contatos WHERE N_IDCONTATO=4"
#"SELECT * FROM tb_contatos WHERE N_IDCONTATO=4 LIKE '%no'"
#vsql = "SELECT * FROM tb_contatos"

vsql = "SELECT * FROM tb_contatos"
res = consulta(vcon,vsql)

for r in res:
    print(r)
