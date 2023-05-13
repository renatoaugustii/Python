import re #regEx

texto = "Um texto aleatorio qualquer!"

pesq=input("Pesquisar: ")

res = re.findall(pesq,texto)

print (res)

qtd = len(res)

print(qtd)