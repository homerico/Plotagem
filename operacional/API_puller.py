# Arquivo para atualizar o conteudo
import os
import urllib.request as rqst
import Path_finder as pf

# Para adquirir o caminho do local certo para colocar o .csv:
path = pf.find('cotacao.csv','/home/homerico/Documentos/POO2/Plotagem')

with open(path, 'w') as fin:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' \
          'MSFT&interval=5min&apikey=YIG0BW9UI8N4X0ZH&datatype=csv'
    content = rqst.urlopen(url)
    fin.write(content.read().decode('utf-8'))