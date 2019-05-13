from bs4 import BeautifulSoup as bs
from requests import get

#Guarda o link da página princial do DO em uma variável.

base_url = 'http://doweb.rio.rj.gov.br'

# Complementa o link principal com o link da publicação diária. O número ao final, no exemplo 4132, é o identificador do dia do DO".
# Após acessar o link, capturo todos os "Identificadores" que são os números que identificam cada arquivo publicado no DO.


url = f'{base_url}/portal/visualizacoes/view_html_diario/4132'
page = bs(get(url).content, 'html.parser')
identificadores = [x.text.split()[0] for x in page.find_all('a')]


# Seleciona cada identificador, substitui no link respectivo e salva cada arquivo em um txt.

conteudo = '{}/apifront/portal/edicoes/publicacoes_ver_conteudo/{}'
for identificador in identificadores:
    page = bs(get(conteudo.format(base_url, identificador)).text, 'html.parser')
    with open(f'arquivos/09-05-2019/{identificador}.txt', 'w', encoding='utf-8') as f:
        f.writelines([x.text.strip() + '\n' for x in page.find_all('p')])
