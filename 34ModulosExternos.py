#Aprendendo utilizar arquivos .py externos dentro do meu codigo
import Auxiliar

#Posso utilizar um alias tbm
# import Auxiliar as Ax
 #Posso tambem buscar somente o jogador por exemplo
 #from Auxiliar import jogador
 
import os

os.system('cls')
Auxiliar.canal() #Executando função de outro arquivo

print(Auxiliar.jogador["Nome"]) #Buscando info de outro arquivo
