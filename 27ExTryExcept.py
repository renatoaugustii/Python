#Aula de exercício para Python e testes de conhecimento das funcoes aprendidas ate o momento
import os
from typing import Any
os.system('cls')

def limpa_tela():
    os.system('cls')

carros=[]

class Carro:
    nome=""
    pot=0
    velMax=0
    ligado=False
    def __init__(self,nome,pot):
        self.nome=nome
        self.pot=pot
        self.velMax=int(pot)*2
        self.ligado=False
    def ligar(self):
        self.ligado=True
    def desligar(self):
        self.ligado=False
    def info(self):
        print("Nome..........:",self.nome)
        print("Nome..........:",self.pot)   
        print("Nome..........:",self.velMax)
        print("Nome..........:",("Sim" if self.ligado==True else "Nao"))      

def menu():
    os.system('cls') or None
    print("1 - Novo Carro")
    print("2 - Info do Carro")
    print("3 - Excluir")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carro")
    print("7 - Sair")
    print("Quantidade de Carros: ", len(carros))
    opc=input("Digite Uma opção: ")
    return opc


def NovoCarro():
    limpa_tela()
    n = input("Nome do Carro: ")
    p = n = input("Potencia do Carro: ")
    car = Carro(n,p) #Passa parametro apara a classe
    carros.append(car)
    print("Novo carro Criado!")
    os.system('pause')

def informacoes():
    limpa_tela()
    n = input("Informe o numero do carro que deseja informacoes:  ")
    try:
        carros[int(n)].info()
    except:
        print("Carro nao existe na lsita")
    os.system('pause')

def ExcluirCarros():
    limpa_tela()
    n = input("Informe o numero do carro que deseja Excluir:  ")
    try:
        del carros[int(n)]
    except:
        print("Carro nao existe na lsita")
    os.system('pause')

def LigarCarro():
    limpa_tela()
    n = input("Informe o numero do carro que deseja Ligar:  ")
    try:
        carros[int(n)].ligar
        print("Carro Ligado")
    except:
        print("Carro nao existe na lsita")
    os.system('pause')


def DesligarCarro():
    limpa_tela()
    n = input("Informe o numero do carro que deseja desligar:  ")
    try:
        carros[int(n)].desligar
        print("Carro desligado")
    except:
        print("Carro nao existe na lsita")
    os.system('pause')   


def ListarCarros():
    limpa_tela()
    p=0
    for c in carros:
        print(p," - ", c.nome)
        p=p+1
    os.system('pause')   

ret=menu()

while ret < "7":
    if ret=="1":
        NovoCarro()
    elif ret == "2":
        informacoes()
    elif ret == "3":
        ExcluirCarros()
    elif ret == "4":
        LigarCarro()
    elif ret == "5":
        DesligarCarro()
    elif ret == "6":
        ListarCarros()
    ret = menu() 

limpa_tela()  
print("Finalizado!")