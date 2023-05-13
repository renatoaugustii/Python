import re

texto="Na pequena cidade de Willow Creek, as coisas pareciam sempre iguais. As casas de madeira alinhadas nas ruas de paralelepípedos, as árvores frondosas que sombreavam as calçadas, e os sorrisos amigáveis dos moradores que se cumprimentavam todos os dias. Mas algo estranho estava acontecendo na cidade. Desde a semana passada, várias pessoas relataram ter visto luzes estranhas no céu durante a noite. E não eram apenas luzes comuns - eram luzes coloridas, que se moviam rapidamente em todas as direções. Alguns diziam que pareciam naves espaciais. Outros, que eram drones. Mas ninguém sabia ao certo o que eram aquelas luzes. E agora, a cidade inteira aguardava ansiosamente para descobrir a verdade."

res=re.split("\s",texto)

print(res)
print(res[4])