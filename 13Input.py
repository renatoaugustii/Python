#Aprendendo sobre input de dados no Python
import os #library para manipular recursos do windows

os.system('cls') #Comando para o windows limpar o terminal


print("HEllo World!") #Saida

nome = input("Digite seu nome: ")

print("Nome Digitado: ", nome)


num1 = input("Digite o primeiro valor: ") #Entradas sao strings devemos converter para calcular no futuro
num2 = input("Digite o segundo valor: ")

res = int(num1) + int(num2) #conversao para numero inteiro

print("Soma dos valores: ",res)