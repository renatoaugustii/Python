import json

# Abrir o arquivo JSON
with open('C:/Users/Renato Augusto/OneDrive/Github/Python/ExampleJSON.json', 'r') as arquivo_json:
    # Carregar o conteúdo do arquivo em um objeto Python
    objeto_json = json.load(arquivo_json)

# Acessar valores do objeto JSON
# print("Nome:", objeto_json["nome"])
# print("Idade:", objeto_json["idade"])
# print("Cidade:", objeto_json["cidade"])
# print("Hobbies:", objeto_json["hobbies"])
# print("Primeiro amigo:", objeto_json["amigos"][0]["nome"])
# print("Segundo amigo:", objeto_json["amigos"][1]["nome"])


for c in objeto_json.values():
    print(c)