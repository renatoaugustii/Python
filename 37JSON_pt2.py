import json

carros_dictionary={
    "marca":"honda",
    "modelo":"HRV",
    "cor":"prata",
}
#Dictionary -> objeto json

carros_list=["honda","Volkswagem","Ford","fiat"]
# list -> array json

carros_tupla=("honda","Volkswagem","Ford","fiat")
#Tupla -> array json


carros_j = json.dumps(carros_dictionary, indent=4, separators=(":","="),sort_keys=True)

print(carros_j)

