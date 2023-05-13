import json
import os

os.system('cls')

json_string = '{"nome": "João", "idade": 30, "cidade": "São Paulo", "hobbies": ["futebol", "música", "cozinhar"], "amigos": [{"nome": "Maria", "idade": 28, "cidade": "Rio de Janeiro"}, {"nome": "Pedro", "idade": 32, "cidade": "Belo Horizonte"}]}'

# Carregar o objeto JSON em Python
objeto_json = json.loads(json_string)

# Acessar valores do objeto JSON
# print("Nome:", objeto_json["nome"])
# print("Idade:", objeto_json["idade"])
# print("Cidade:", objeto_json["cidade"])
# print("Hobbies:", objeto_json["hobbies"])
# print("Primeiro amigo:", objeto_json["amigos"][0]["nome"])
# print("Segundo amigo:", objeto_json["amigos"][1]["nome"])

# for x in objeto_json:
#     print (x)

# for x in objeto_json.values():
#     print (x)

# for x in objeto_json.items():
#     print (x)


print(objeto_json["nome"]," - ", objeto_json["cidade"])
