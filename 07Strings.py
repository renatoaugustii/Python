Curso = "Curso de Python"

res = "Python" in Curso #Verifica se existe a palavra Python dentro de Curso
print(res) #Retorna true


cidade = "Belo Horizonte"
dia = 9
mes = "Maio"
ano = 2023
meunome = "Renato Augusto"
print(cidade,", ",dia," de ",mes," de ",ano)

#OU PODEMOS FAZER ASSIM

data = "{}, {} de {} de {}"

print(data.format(cidade,dia,mes,ano))

data = "{}, {} de {} de {}\n{}" #quebra de linha com \n

print(data.format(cidade,dia,mes,ano,meunome))

#  \'  \"  \n  \r  \t  \b   Mais utilizados

