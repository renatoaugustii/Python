import datetime

data=datetime.datetime.now()

print(data)

print(data.day)
print(data.month)
print(data.year)

print(data.day,"/",data.month,"/",data.year)

nasc = datetime.datetime(1992,1,12)

print(nasc.strftime("%A")) #Dia da semana

print(nasc.strftime("%a")) #Resumo dia da semana

print(nasc.strftime("%W")) #numerto do dia da semana

print(nasc.strftime("%d")) #num dia do mes

print(nasc.strftime("%b")) #nome mes

print(nasc.strftime("%n")) #numero do mes

print(nasc.strftime("%y")) #Ano

print(nasc.strftime("%h")) #hora

print(nasc.strftime("%I")) #Hora

print(nasc.strftime("%p")) #AM PM

print(nasc.strftime("%S")) #Segundos

print(nasc.strftime("%f")) #microsegundos