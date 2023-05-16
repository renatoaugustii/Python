#Tkinter é nativo do Python, simples e rápido.
#Para casos de usos mais robustos, necessário migrar por exemplo para o QTCreator

from tkinter import *

#defnir um nome para a classe tk, nesse caso escolhi o nome app por ser simples de escrever
app=Tk()
app.title("Teste de Interface")
app.geometry("500x300")
app.configure(background="#c8c8c8")

txt1=Label(app,text="Curso de Python", bg="#008", fg="#fff")
txt1.place(x=10,y=10,width=150,height=20)

vtxt="Módulo Tkinter"
vbg="#008"
vfg="#fff"
txt2=Label(app,text=vtxt,bg=vbg,fg=vfg)
txt2.pack(ipadx=20,ipady=20,padx=5,pady=5,side="bottom",fill=X,expand=True)

app.mainloop()