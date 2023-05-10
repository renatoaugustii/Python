#Trabalhando com listas

carros = ["HRV","Polo","Golf","Argo", "Fox"]


print(carros[1]) 

carros[3] = "Fusion" #Substitui na posiçao 3

print(carros[0:4]) 

carros.append("Fit") #Adiciona a lista
carros.append("Maveric")
carros.append("Fusca")

print(carros)

print("Tamanho da lista: ", len(carros))

tam = len(carros)

print(carros[tam-1])#imprime o Ultimo carro da lista

carros.remove("Fusca")#Remover da lista

tam = len(carros)

print(carros[tam-1])#imprime o Ultimo carro da lista

carros.pop() #remove o ultimo item da lista

print(carros)

carros.pop() #remove o ultimo item da lista

print(carros)

del carros[2] #remove index 2

print(carros)

carros.clear() #Limpou todos os dados da lista

print(carros)

carros = ["HRV","Polo","Golf","Argo", "Fox", "Ferrari", "Porshe"]

carros2=list(carros) #transfere a lista
print(carros2)


carros3 = carros + carros2
print(carros3) #Juntou todas as listas na lista 3
