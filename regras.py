RULES_CONFIGS = [
    {"name": "Nome da Secretaria",
     "rule": r"<nome_da_secretaria>CÂMARA MUNICIPAL DO RIO DE JANEIRO"},
    {"name": "Tipo Instrumento",
     "rule": r"<tipo_instrumento>AVISO DE LICITAÇÃO"},
    {"name": "Modalidade",
     "rule": r"Modalidade: ?Ppregao presencial n(?P[0-9]{0,50}"},
    {"name": "numero pregao",
     "rule": r"Modalidade: pregao presencial n?(?P<numero_instrumento>[0-9]{0,50}"},
]

'''
    {"name": "Processo Administrativo",
        "rule": r"processo administrativo: (?P<numero_instrumento>[a-zA-Z]{0,50} ?[0-9]{0,50}/[0-9]{0,50})"},
    {"name": "contrato",
        "rule": r"contrato nº (?P<numero_instrumento>[0-9]+/[0-9]{1,20})"},
    {"name": "Edital",
        "rule": r"Edital (?P<numero_instrumento>[0-9]+/[0-9]{1,20})"},
    {"name": "Valor",
        "rule": r"Valor: (?P<valor>R.+[0-9])"},
    {"name": "Data",
        "rule": r"Data: (?P<data>[0-9]{0,2}/?[0-9]{0,2}/?[0-9]{0,4} "},
'''
