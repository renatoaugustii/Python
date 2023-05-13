import re
import os


nome = "teste.txt"
caminho= "C:/Users/Renato Augusto/OneDrive/Github/Python/"

if os.path.exists(caminho+nome):
    print("Existe")
else:    
    f=open(caminho+nome,"x")
    f.close()

os.remove(caminho+nome)
