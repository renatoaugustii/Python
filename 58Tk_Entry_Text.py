#Tkinter é nativo do Python, simples e rápido.
#Para casos de usos mais robustos, necessário migrar por exemplo para o QTCreator

from tkinter import *

app=Tk()
app.title("Teste de Interface")
app.geometry("500x300")
app.configure(background="#dde")

#anchor=> N=Norte, S=Sul, E =LEste, W=Oeste
#NE= Nordeste, SE=Sudeste, SO= Sudoeste, NO=Noroeste
Label(app,text="Nome",bg="#dde",fg="#009",anchor=W).place(x=10,y=10,width=100)
vnome=Entry(app)
vnome.place(x=10,y=30,width=200,height=20)


Label(app,text="Telefone",bg="#dde",fg="#009",anchor=W).place(x=10,y=60,width=100)
vfone=Entry(app)
vfone.place(x=10,y=80,width=100,height=20)

Label(app,text="E-mail",bg="#dde",fg="#009",anchor=W).place(x=10,y=110,width=100)
vmail=Entry(app)
vmail.place(x=10,y=130,width=200,height=20)


#Aqui vamos inserir o componente Text diferente dos Entry que estávamos utilizando
Label(app,text="OBS",bg="#dde",fg="#009",anchor=W).place(x=10,y=160,width=100)
vobs=Text(app)
vobs.place(x=10,y=180,width=200,height=80)


app.mainloop()