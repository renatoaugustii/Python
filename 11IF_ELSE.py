#Aprendendo a utilizar o Else

a=1
b=3
op = "-"
res =0 


if op=="+":
    res = a+b
elif op=="-":
    res = a-b
elif op=="*":
    res = a*b
elif op=="/":
    res = a/b            
else:
    print("Valor de op não foi válido")


print(a,op,b,"= ",res)


clima = "Chuva"
lugar = ""

if clima=="Sol":
    lugar="Clube"
else:
    lugar = "Cinema"  

print("Vou ao ", lugar)      