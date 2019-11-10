import os
import random
import string
import urllib.request as rqst

# Outros arquivos
import Path_finder as pf

# Cria keys aleatórias
def random_key(key_length=16):
    letters = string.ascii_uppercase
    numbers = string.digits
    key_base = letters + numbers
    return ''.join(random.choice(key_base) for i in range(key_length))

# Puxa o conteudo da API e armazena no arquivo de nome desejado, caso não exista esse arquivo, é criado na mesma função.
def pull(key=random_key(), function='TIME_SERIES_DAILY', datatype='csv', symbol='MSFT', **kwargs):

    # Se um arquivo já foi criado, vai ser pego o caminho dele, caso contrário será criado um caminho para esse arquivo novo.
    try:
        path = pf.find(name='{}.csv'.format(function),path='/home/homerico/Documentos/POO2/Plotagem')
    except FileNotFoundError:
        path = pf.find('conteudo',path='/home/homerico/Documentos/POO2/Plotagem',type='dir') + \
               '/{}.csv'.format(function)

    # Criação do url com parametros prefeitos pela API para poder puxar o conteúdo.
    url = 'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={key}&datatype={datatype}'\
        .format(function=function,key=key,symbol=symbol,datatype=datatype)
    for kwvalue,kwkey in kwargs.items():
        url = url + '&{kwvalue}={kwkey}'.format(kwvalue=kwvalue,kwkey=kwkey)

    # Cria o arquivo e/ou armazena o conteudo
    with open(path, 'w') as fin:
        content = rqst.urlopen(url)
        fin.write(content.read().decode('utf-8'))
    return function