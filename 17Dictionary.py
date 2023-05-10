#Aprendendo Dictionary

import os #library para manipular recursos do windows
os.system('cls') #Comando para o windows limpar o terminal

#chave/Key  - Valor/Value
carro={"Fabricante":"Honda",
        "Modelo":"HRV",
        "Ano":"2011",
        "Cor":"Azul Bebê"
        }

print(carro["Modelo"]) #Imprimi HRV
print(carro["Cor"]) #Imprimi Azul bebê

######################################################################
#OUTRO EXEMPLO

fab=carro.get("Fabricante")

print(fab)

######################################################################
#OUTRO EXEMPLO

for x in carro:
    print(x) #Imprimi a chave 

for x in carro:
    print(carro[x]) #Imprimi o valor

for c,v in carro.items(): #Imprime os chave e valor
    print(c," :",v)

if "Modelo" in carro: #verifica se existe essa chave MODELO dentro do dictionary CARRO
    print("Existe")

print("Tamanho :",len(carro)) #tamanho do Dictionary

#Asicionando items
carro["cambio"]="Automatico"

#removendo items
carro.pop("Cor")

for c,v in carro.items(): #Imprime os chave e valor
    print(c," :",v)

#limpa tudo
carro.clear()

if carro:
    print("Existe items")
else:print("Não existe mais items")

for c,v in carro.items(): #Imprime os chave e valor
    print(c," :",v)

carro.clear()

###################################################################

carros ={
    "Carro1":{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    },
    "Carro2":{
        "Fabricante":"VW",
        "Modelo":"Golf"
    }
}

print(carros["Carro1"])
print(carros["Carro1"]["Fabricante"])