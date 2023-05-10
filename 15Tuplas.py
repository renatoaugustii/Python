#Aprendendo sobre Tuplas
import os #library para manipular recursos do windows
os.system('cls') #Comando para o windows limpar o terminal

carros = ["Volkswagen Gol", "Fiat Palio", "Chevrolet Onix", "Ford Fiesta", "Renault Kwid", "Toyota Corolla", "Honda Civic", "Hyundai HB20", "Nissan March", "Peugeot 208", "Volkswagen Polo", "Chevrolet Prisma", "Ford Ka", "Renault Sandero", "Toyota Yaris", "Honda Fit", "Hyundai Creta", "Nissan Versa", "Kia Rio", "Subaru Impreza"]

tuplaCarros=("Volkswagen Gol", "Fiat Palio", "Chevrolet Onix", "Ford Fiesta", "Renault Kwid", "Toyota Corolla", "Honda Civic", "Hyundai HB20", "Nissan March", "Peugeot 208", "Volkswagen Polo", "Chevrolet Prisma", "Ford Ka", "Renault Sandero", "Toyota Yaris", "Honda Fit", "Hyundai Creta", "Nissan Versa", "Kia Rio", "Subaru Impreza")

carros.append("Fusquinha")

for x in carros:
    print(x)


for x in tuplaCarros:
    print(x)    
#Tuplas nao podem ser alteradas. Um macete é converter em lista e depois voltar para tupla
