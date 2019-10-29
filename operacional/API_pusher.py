# Arquivo para atualizar o conteudo
import os.path
import urllib.request


# Para adquirir o caminho do local certo para colocar o .csv:
current_path = os.path.dirname(__file__)
new_path = os.path.relpath('../conteudo/cotacao.csv', current_path)

with open(new_path, 'w') as fin:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' \
          'MSFT&interval=5min&apikey=YIG0BW9UI8N4X0ZH&datatype=csv'
    content = urllib.request.urlopen(url)
    fin.write(content.read().decode('utf-8'))