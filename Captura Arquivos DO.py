from requests import get
from requests import request
import requests
import os
from pathlib import Path
from bs4 import BeautifulSoup as bs

r = requests.get('http://doweb.rio.rj.gov.br/apifront/portal/edicoes/ultimas_edicoes.json')
itens = r.json()['itens'] #Captura todas as edições
id_dia = itens[0]['id'] #Captura o id da ultima edição
id_data = str(itens[0]['data']).replace('/', '-') #Captura a data da ultima edição
#id_data_arquivo = str(id_data).replace('/','-')
print(id_dia, id_data)

base_url = 'http://doweb.rio.rj.gov.br'
url = f'{base_url}/portal/visualizacoes/view_html_diario/{id_dia}'
page = bs(get(url).content, 'html.parser')
identificadores = [x.text.split()[0] for x in page.find_all('a')]

conteudo = '{}/apifront/portal/edicoes/publicacoes_ver_conteudo/{}'

fileName = (f'D:/Projetos Python/Diario Oficial/{id_data}.txt')
file = Path(fileName)
if file.is_file():
    pass
else:
    try:
        for identificador in identificadores:
            page = bs(get(conteudo.format(base_url, identificador)).text, 'html.parser')
            with open(f'D:/Projetos Python/Diario Oficial/{id_data}.txt', 'a', encoding='utf-8') as f:
                f.writelines([x.text.strip() + '\n' for x in page.find_all('p')])
    except:
        pass
