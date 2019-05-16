import re
import os
from pprint import pprint
import sqlite3
from regras import RULES_CONFIGS

def create_db():
    os.remove('Leitor_DO.db') if os.path.exists('Leitor_DO.db') else None
    con = sqlite3.connect('Leitor_DO.db')
    cur = con.cursor()
    sql_create = 'create table Dados (id integer primary key, nome_da_secretaria text, tipo_instrumento text, nome_do_instrumento text, numero_instrumento text, data text)'
    cur.execute(sql_create)
    return con, cur

def close_db(con, cur):
    con.commit()
    cur.close()
    con.close()


def insert_record(cur, nome_da_secretaria, tipo_instrumento, nome_do_instrumento, numero_instrumento, data):
    cur.execute('INSERT INTO Dados (nome_da_secretaria, tipo_instrumento, nome_do_instrumento, numero_instrumento, data) VALUES(?, ?, ?, ?, ?)',
                (nome_da_secretaria, tipo_instrumento, nome_do_instrumento, numero_instrumento, data))


def read_input(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return str(f.readlines())

RULES_CONFIGS = [
    {"name": "Nome da Secretaria",
     "rule": r"(?P<nome_da_secretaria>CÂMARA MUNICIPAL DO RIO DE JANEIRO)"},
    {"name": "Tipo Instrumento",
     "rule": r"(?P<tipo_instrumento>AVISO DE LICITAÇÃO)"},
    {"name": "Modalidade",
     "rule": r"(?P<nome_instrumento>preg\wo presencial)"},
    {"name": "numero pregao",
     "rule": r"(?P<numero_instrumento>[0-9]{0,50}/[0-9]{0,50})"},
    {"name": "data",
     "rule": r"data:.(?P<data>[0-9]{0,10}\D{0,100}[0-9]{0,50})"}
]

def main():
    con, cur = create_db()
    try:
        text = read_input('arquivos/09-05-2019/572775.txt')
        for rule_config in RULES_CONFIGS:
            matches = re.finditer(rule_config['rule'], text, re.IGNORECASE | re.MULTILINE)
#            print(matches)
            for matchNum, match in enumerate(matches, start=1):
                pprint(match.groups())
#                print("Rule {} matched at pos {}, value = '{}'".format(rule_config['name'], match.span(), match.group()))
#                insert_record(cur, rule_config['name'], match.group('numero_instrumento'), match.span()[0])
    finally:
        close_db(con, cur)


if __name__ == "__main__":
    main()
