#install PANDAS : pip install pandas
#instal lxml : pip3 install lxml

#import pandas library and defined as pd
import pandas as pd

df = pd.read_html('https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=31230503083231001680651110000982031545552068%7C2%7C1%7C1%7C5B4A21D218BF633703649C8C308197768F7C746F')

#Sets how many lines to print
#print(df[0].head(15))

df[1].to_csv('data.csv')