import os
import json #Biblioteca para trabalhar com Json

os.system('cls')


carros_json='{"marca":"Honda","modelo":"HRV", "cor":"prata"}'

#Se parece muito com Dictonary
carros=json.loads(carros_json)

print(carros["modelo"])

for x in carros:
    print(x)

for x in carros.values():
    print(x)


#transformar dict em Json
carros={
    "marca":"Honda",
    "modelo":"HRV", 
    "cor":"prata"
    }

carros_json=json.dumps(carros)

print(carros_json)