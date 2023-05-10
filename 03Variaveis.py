#Estudando variaveis
num1=num2=res=0
teste = "Renato"

def cn():
    print(teste) #Consigo imprimir pois é uma variável global

cn()


def cn():
    teste1 = 2
    print(teste1) #Consigo imprimir pois é uma variável local

cn()  

print(teste1) #Não é uma variável aceitável pois ela é uma variável local dentro da funcáo cn

#Podemos definir uma variável global mesmo quando ela está dentro de um contexto local como no exemplo:

def cn():
    global VarGlobal #primeiro declaramos como global e na proxima linha atribuimos valor
    VarGlobal = 2
cn()  

print(VarGlobal) #Consigo imprimir pois é uma variável global agora