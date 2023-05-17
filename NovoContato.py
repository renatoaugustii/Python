#Tkinter é nativo do Python, simples e rápido.
#Para casos de usos mais robustos, necessário migrar por exemplo para o QTCreator

from tkinter import *
import os
import Banco


c = os.path.dirname(__file__)
nomeArquivo=c+"\\nomes.txt"

os.system('cls')

def gravarDados():
    if txt_nome.get() != "":
        vnome = txt_nome.get()
        vfone= txt_fone.get()
        vemail= txt_email.get()
        vobs= txt_obs.get("1.0",END)
        vquery="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO, T_OBS) VALUES('{}','{}','{}','{}')".format(vnome,vfone,vemail,vobs)
        Banco.dml(vquery)

        txt_nome.delete(0,END)
        txt_fone.delete(0,END)
        txt_email.delete(0,END)
        txt_obs.delete("1.0",END)

        print("Dados Gravados")
    else:
        print("Erro")   

app=Tk()
app.title("Teste de Interface")
app.geometry("500x300")
app.configure(background="#dde")

#anchor=> N=Norte, S=Sul, E =LEste, W=Oeste
#NE= Nordeste, SE=Sudeste, SO= Sudoeste, NO=Noroeste
Label(app,text="Nome",bg="#dde",fg="#009",anchor=W).place(x=10,y=10,width=100)
txt_nome=Entry(app)
txt_nome.place(x=10,y=30,width=200,height=20)


Label(app,text="Telefone",bg="#dde",fg="#009",anchor=W).place(x=10,y=60,width=100)
txt_fone=Entry(app)
txt_fone.place(x=10,y=80,width=100,height=20)

Label(app,text="E-mail",bg="#dde",fg="#009",anchor=W).place(x=10,y=110,width=100)
txt_email=Entry(app)
txt_email.place(x=10,y=130,width=200,height=20)


#Aqui vamos inserir o componente Text diferente dos Entry que estávamos utilizando
Label(app,text="OBS",bg="#dde",fg="#009",anchor=W).place(x=10,y=160,width=100)
txt_obs=Text(app)
txt_obs.place(x=10,y=180,width=200,height=80)

Button(app,text="Gravar",command=gravarDados).place(x=10,y=270,width=100,height=20)

app.mainloop() 