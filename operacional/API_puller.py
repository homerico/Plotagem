# Arquivo para atualizar o conteudo
import os
import random
import string
import urllib.request as rqst

# Outros arquivos
import Path_finder as pf

# Criar keys aleatórias
def random_key(key_length=16):
    letters = string.ascii_uppercase
    numbers = '0123456789'
    key_base = letters + numbers
    return ''.join(random.choice(key_base) for i in range(key_length))

# Para adquirir o caminho do local certo para colocar o .csv:
def pull(interval='5min',function='TIME_SERIES_INTRADAY'):
    path = pf.find('cotacao.csv','/home/homerico/Documentos/POO2/Plotagem')
    url = 'https://www.alphavantage.co/query?function={function}&symbol=MSFT&interval={interval}&apikey={key}&' \
          'datatype=csv'.format(function=function,interval=interval,key=random_key())
    #url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=YIG0BW9UI8N4X0ZH&datatype=csv'
    with open(path, 'w') as fin:
        content = rqst.urlopen(url)
        fin.write(content.read().decode('utf-8'))
        print(content)