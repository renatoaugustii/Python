import random #Necessário para utilizar o Random

num_i = 10
num_f = 1.1
num_c = 1j


#x = num_i
#x = num_f
x = num_c

num_r = random.randrange(0,60) #Sorteio aleatório de valores de 0 a 60


print("Valor de x: ",x," Tipo: ",type(x)) #Usar Virgula para concatenar simplifica a função
print(num_r)