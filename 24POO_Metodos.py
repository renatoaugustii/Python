import os 
os.system('cls')

#Criação de classes
class Carro:
    velMAX=0
    ligado=False
    cor=""
    #Definindo um construtor
    def __init__(self,v,l,c):
        self.velMAX = v
        self.ligado=l
        self.cor=c
    def mostrar(self):
        print("Velocidade Maxima: ", self.velMAX)
        print("Velocidade Maxima: ", self.ligado)
        print("Velocidade Maxima: ", self.cor)
        print("-----------------------------")
    def ligar(self):
        self.ligado = True   
    def desligar(self):
        self.ligado = False 
    def andar(self):
        if(self.ligado):
            print("Andando")
        else:
            print("Carro Desligado")

#Intaciamento de Objetos
c1=Carro(200, False,"Preto")
c2=Carro(120,False,"Branco")
c3=Carro(150,True,"Amarelo")

c1.ligar()

#Exibindo
c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andar()
c2.andar()


