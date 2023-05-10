#Aprendendo matrizes

import os #library para manipular recursos do windows
os.system('cls') #Comando para o windows limpar o terminal

#lista
#carros = ["Volkswagen Gol", "Fiat Palio", "Chevrolet Onix", "Ford Fiesta", "Renault Kwid", "Toyota Corolla", "Honda Civic", "Hyundai HB20", "Nissan March", "Peugeot 208", "Volkswagen Polo", "Chevrolet Prisma", "Ford Ka", "Renault Sandero", "Toyota Yaris", "Honda Fit", "Hyundai Creta", "Nissan Versa", "Kia Rio", "Subaru Impreza"]

carros=[
    ["Modelo","HRV"],
    ["Fabricante","Honda"],
    ["Ano","2016"]
    ]

print(carros[0][0]) #imprimindo a matriz
print(carros[1][1]) #imprimindo a matriz

for l,c in carros:
    print("Linha: ",l,"| Coluna: ", c) #Imprimindo toda a matriz

for l,c in carros:
    print(l,"| ", c) #Imprimindo toda a matriz  

carros.append(["Cor","Prata"]) #insrindo dados na matriz

for l,c in carros:
    print(l,"| ", c) #Imprimindo toda a matriz  