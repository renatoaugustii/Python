#trabalhando com if, tomar cuidado com identação
if 10 > 2:
    print("Sou Maior")
print("Estou Fora do IF")

#Repare que apenas o print ("Sou Maior") pertence ao IF. Qualquer comando que estiver fora da identação não será entendido como parte da condicional.
if 10 > 2:
    print("Sou Maior")
    print("Ainda Faço parte do IF")
print("Estou Fora do IF")

#Outros exemplos
if 10>2:
                print("Somente quem está logo abaixo pertece ao if")
                print("Eu ainda faço parte do IF")
print("Eu nao faço mais parte do if")    

#Algumas boas práticas
#Use espaços em branco para separar operadores, palavras-chave e parâmetros de função. Por exemplo:

x = 5 + 3
def foo(bar, baz):
    print("Código Aqui")

#Use uma linha em branco para separar blocos de código relacionados. Por exemplo:

y = 2

if x > 0:
    print("Codigo Aqui")

    if y > 0:
        print("Codigo Aqui")

    print("Insira mais códigos aqui") #Esse if ainda faz parte do primeiro if ali encima

#Use parênteses para delimitar expressões complexas em uma única linha. Por exemplo:
valor1=valor2=valor3=valor4 = 4

resultado = (valor1 + valor2) / (valor3 * valor4)

#Use aspas simples ou duplas para delimitar strings. Por exemplo:
nome = 'João'
sobrenome = "Silva"

#Use colchetes para delimitar listas. Por exemplo:
numeros = [1, 2, 3, 4, 5]

#Use chaves para delimitar dicionários. Por exemplo:
dados = {'nome': 'João', 'idade': 30}