import os #library para manipular recursos do windows
os.system('cls')

def imprimir():
    print("Primeira execução da minha função!")

imprimir() #Executando minha função

n1 = 10
n2 = 20

def somar():
    r=n1+n2
    print(r)
somar() #Executando minha função


########################################################################
os.system('cls')

def calculos(): #criando a função
    imprimir()
    somar()

calculos() #chamando a função
