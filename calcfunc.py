# -*- coding: utf-8 -*-

import pandas as pd
from bin.coletar import *
from bin.detect_troca import *

try:
    f = open("relatorio.txt", 'r+', encoding='utf-8')
except FileNotFoundError:
    print("Não encontrei o arquivo relatorio.txt, verifique se ele está na mesma pasta que eu..\n")
    exit()

f.seek(0)
STRING = f.read()
STRING = STRING.split('endfunc')
DADOS_limpo = []
for aux in STRING:
    aux1 = aux.replace(' ','')
    aux1 = aux1.replace('\n','')
    DADOS_limpo.append(aux1)

DADOS_sujo = []
for aux2 in STRING:
    DADOS_sujo.append(aux2)

DADOS_sujo.pop()
DADOS_limpo.pop()

f.seek(0)
VET = {}
for i, j in zip(DADOS_sujo, DADOS_limpo):
    if coletar_dias(j) <= 0:
        VET.update({str(coletar_nome(i)) + '!': (coletar_dias(j), coletar_posto(i))})
    else:
        VET.update({str(coletar_nome(i) + detect_troca(j)): (coletar_dias(j), coletar_posto(i))})
STR = pd.DataFrame.from_dict(VET, orient='index', columns=('DIAS', 'POSTO'))
STR.sort_values('POSTO', inplace=True)
STR.to_excel('saida.xlsx')


print('ARQUIVO SAIDA GERADO!\n\nsaindo..')
#os.system('start saida.xlsx')
#exit()