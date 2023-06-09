import sqlite3
from sqlite3 import Error
import os


## conexão com o Banco de dados SQLite
def ConexaoBanco():
    caminho = "C:\\Users\\Renato Augusto\\OneDrive\\Github\\Python\\DB\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho) #Realiza a conexão com banco de dados
    except Error as ex:
        print(ex) #Imprime o possivel error qe aconteceu ao tentar realizar a conexão com o banco de dados
    return con        

vcon = ConexaoBanco()

#Funcao para limpar a tela
def limpaTela():
    os.system('cls')


#INSERT, UPDATE E DELETE
def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("PROCEDIMENTO COM SUCESSO!")  
        conexao.close()      

def consultar(conexao,sql):
    vcon = ConexaoBanco()
    c=conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    conexao.close()   
    return res

def menuPrincipal():
    os.system('cls')
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registros ")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")

def menuInserir():
    limpaTela()
    vnome=input("Digite o nome: ")
    vTelefone=input("Digite o Telefone: ")
    vEmail=input("Digite o e-mail: ")
    vsql="INSERT INTO tb_contatos(T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('{}','{}','{}')".format(vnome, vTelefone, vEmail)
    query(vcon,vsql)
    #vcon.close()
    os.system('pause')

def menuDeletar():
    limpaTela()
    vid=input("Digite o ID do registo que deseja deletar: ")
    vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO={}".format(vid)
    query(vcon,vsql)
    #vcon.close()

def menuAtualizar():
    limpaTela()
    vid=input("Digite o ID do registo que deseja alterar: ")
    vsql = "SELECT * FROM tb_contatos WHERE N_IDCONTATO={}".format(vid)
    r=consultar(vcon,vsql)
    rnome=r[0][1]
    rtelefone=r[0][2]
    remail=r[0][3]
    vnome=input("Digite o nome: ")
    vTelefone=input("Digite o Telefone: ")
    vEmail=input("Digite o e-mail: ")

    if(len(vnome)==0):
        vnome=rnome
    if(len(vTelefone)==0):
        vTelefone=rtelefone
    if(len(vEmail)==0):
        vEmail=remail

    vsql="UPDATE tb_contatos SET T_NOMECONTATO='{}', T_TELEFONECONTATO='{}', T_EMAILCONTATO='{}' WHERE  N_IDCONTATO={}".format(vnome, vTelefone, vEmail,vid)
    query(vcon,vsql)
    #vcon.close()
    
def menuConsultar():
    limpaTela()
    vsql = "SELECT * FROM tb_contatos"
    res=consultar(vcon,vsql)
    #vcon.close()
    vlim=5
    vcont=0
    for r in res:
        print("ID:{0:<3} Nome:{1:<30} Telefone:{2:<14} E-mail:{3:<30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1
        if(vcont>=vlim):
            vcont = 0 
            os.system('pause')
            limpaTela
    print("Fim da Lista")    
    os.system('pause')

def menuConsultarNomes():
    limpaTela()
    vnome=input("Digite o nome: ")
    vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%{}%'".format(vnome)
    res= consultar(vcon,vsql)
    #vcon.close()
    vlim=5
    vcont=0
    for r in res:
        print("ID:{0:<3} Nome:{1:<30} Telefone:{2:<14} E-mail:{3:<30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1
        if(vcont>=vlim):
            vcont = 0 
            os.system('pause')
            limpaTela
    print("Fim da Lista")    
    os.system('pause')


opc = 0
#Enquanto for diferente de 6 - Sair o While continua rodando!
while   opc != 6: 
    menuPrincipal()
    opc = int(input("Digite uma opção: "))

    if opc==1:
        vcon = ConexaoBanco()
        menuInserir()
    elif opc==2:
        menuDeletar()
        vcon = ConexaoBanco()
    elif opc==3:
        vcon = ConexaoBanco()
        menuAtualizar()
    elif opc==4:    
        vcon = ConexaoBanco() 
        menuConsultar()
    elif opc==5:  
        vcon = ConexaoBanco()   
        menuConsultarNomes() 
    elif opc==6:
        os.system('cls')
        print("Fim do Programa!")
    else:
        os.system('cls')
        print('Opção Inválida')
        os.system('pause')
os.system('pause')        



