
#interator percorre uma lista sem precisar necessariamente de um laco for
carros = ["HRV","Polo","Golf","Argo", "Fox","Argo"]

itCarros=iter(carros)

print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))


#Atualiza e imprimi mesmo que a lista vá aumentando.
while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        break           


