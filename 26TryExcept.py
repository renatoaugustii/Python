import os
os.system('cls')


try:
    print(x) #X is not defined
except NameError:
    print("X nao definido")    
except:
    print("Erro descoinhecido")    
else:
    print("Tudo certo")

#----------------------------------------------------------------

x=10
try:
    print(x) #X is defined
except NameError:
    print("X nao definido")    
except:
    print("Erro descoinhecido")    
else:
    print("Tudo certo")
finally:
    print("Fim do programa!")    

num = -10

if num<1:
    raise Exception("Valor nao permitido") #Gerando uma exceção
else:
    print("Tudo certo")



