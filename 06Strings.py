Curso  = "Curso de Python    "

print(Curso)


print(Curso[0]) #Imprime o C
print(Curso[1]) #Imprime o U
print(Curso[2]) #Imprime o R
print(Curso[3]) #Imprime o S

#OU posso utilizar

print(Curso[9:15]) #Imprime os caracteres da posição 9 até a 15

print("Tamanho: ",len(Curso)) #Tamanho da String

Curso.strip() #Remove os espaços no inicio e no final da String

print(Curso.strip())
print("Tamanho: ",len(Curso.strip())) #Tamanho da String


print(Curso.lower()) #Converte para minusculo
print(Curso.upper()) #Converte para maiusculo

print(Curso.replace("Python","C++")) #Troca parte da String, Trocou Python por C++

a = Curso.split(" ") #Separa a string em quantidadades de " ", nesse caso 3
print(a[0]) #imprime em lista as partes
print(a[2]) #imprime em lista as partes