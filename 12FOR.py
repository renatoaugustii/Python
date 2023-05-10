#Aprendendo sobre o FOR

carros = ["Gol", "Palio", "Corsa", "Celta", "Fiesta", "Uno", "Golf"]

print(carros)

for x in carros:
    print(x)
    if x=="Golf":
        print("VW")

print(carros)

for x in carros:
    if x=="Fiesta":
        break #PARAR o FOR
    print(x)

