import os

os.system('cls')


def somar(n1, n2):
    r=n1+n2
    return r
    print(r)

somar(5,7)
somar(3,2)

resultado = somar(1,2) #retornando valor da função
print(resultado)


if resultado==3:
    print("Resultado bem sucedido")
else:print("Nao foi satisfeito")

##############################################################

def textos(*t):
    print(t[0])
    print(t[1])
    print(t[2])

textos("Renato","Augusto","Correa","da", "Silva")    


def textos(*txt):
        for t in txt:
             print(t)

textos("Renato","Augusto","Correa","da", "Silva")    

##################################################################

def subtrair(*num):
    r=0
    for n in num:
         r+=n
    return r      

    
resultado = subtrair(10,25,2,2) 

print(resultado)