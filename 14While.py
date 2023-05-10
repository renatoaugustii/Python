#Estrutura While

import os #library para manipular recursos do windows
os.system('cls') #Comando para o windows limpar o terminal

#inicializaçao de variavel de controle
i=0

while (i<9):
    print(i)
    i= i+1 ### IMPORTANTE ### SE ESQUECER ENTRA DENTRO DO LOOP INFINITO

print("fim do loop")    

i=0

while (i<9):
    print(i)
    i= i+1 ### IMPORTANTE ### SE ESQUECER ENTRA DENTRO DO LOOP INFINITO
    if i>=5:
        break 
print("fim do loop")   

carros = ["Gol", "Palio", "Corsa", "Celta", "Fiesta", "Uno"]

tam = len(carros)
i = 0

while i <tam:
    print(carros[i])
    i+=1


carros = ["Volkswagen Gol", "Fiat Palio", "Chevrolet Onix", "Ford Fiesta", "Renault Kwid", "Toyota Corolla", "Honda Civic", "Hyundai HB20", "Nissan March", "Peugeot 208", "Volkswagen Polo", "Chevrolet Prisma", "Ford Ka", "Renault Sandero", "Toyota Yaris", "Honda Fit", "Hyundai Creta", "Nissan Versa", "Kia Rio", "Subaru Impreza"]
print(carros)

for x in carros:
    print(x)