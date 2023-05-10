import os #library para manipular recursos do windows
import random #Necessário para utilizar o Random

os.system('cls') #Comando para o windows limpar o terminal

numSorteado = random.randrange(1,10)
tentativas =0
numUsuario = 0

print(numSorteado)

while (numUsuario!=numSorteado)or(numUsuario==-1):
    numUsuario = int(input("Digite uma tentativa: "))
    print("Voce digitou: ",numUsuario," ",numSorteado)
    tentativas = tentativas+1
print("PROGRAMA FINALIZADO COM ", tentativas, " TENTATIVAS")
