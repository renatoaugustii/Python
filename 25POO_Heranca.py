import os
os.system('cls')

class NPC: #Base, Pai, Super
    def __init__(self,nome,time,forca,municao):
        self.nome=nome
        self.forca=forca
        self.time=time
        self.municao=municao
        self.vivo=True
        self.energia=100
    def info(self):
        print("Nome: ",self.nome)    
        print("Time: ",self.time)
        print("forca: ",self.forca)
        print("municao: ",self.municao)
        print("vivo: ","Sim" if self.vivo else "Não")
        print("energia: ",self.energia)
        print("-------------------------------------------")

#herança de todas as propriedades
class Soldado(NPC):        
    def __init__(self,nome,time):
        self.forca=200
        self.municao=200  
        super().__init__(nome,time,self.forca,self.municao)  #Invoca da Classe PAI

class Guarda(NPC):
    def __init__(self,nome,time):
        self.forca=100
        self.municao=20  
        super().__init__(nome,time,self.forca,self.municao)      


class Elite(NPC):
    def __init__(self,nome,time):
        self.forca=100
        self.municao=20  
        super().__init__(nome,time,self.forca,self.municao)    
        def inf(self):
            super().info()


s1=Guarda("Olho Vivo",1)
s2=Soldado("Nascimento",2)
s3=Guarda("Atento",2)
s4=Soldado("Da Cunha",1)
s5=Elite("Samurai",1)

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
