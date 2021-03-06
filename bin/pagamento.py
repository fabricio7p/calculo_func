from bin.coletar import coletar_dias
from bin.scan_escala import *
from bin.detect import falta


def pagamento(STRING_limpa, mes):
    t1 =['Janeiro', 'Março', 'Maio', 'Julho', 'Agosto', 'Outubro', 'Dezembro']
    t2 =['Fevereiro']
    t0 = ['Abril', 'Junho', 'Setembro', 'Novembro']
    t_hold = 0
    if mes in t1:
        t_hold = 15
    elif mes in t2:
        t_hold = 13
    elif mes in t0:
        t_hold = 14
    if scan_escala(STRING_limpa) == 1 and coletar_dias(STRING_limpa) >= t_hold:
        if ('ATM' or 'DiaJustificado') not in STRING_limpa:
            if falta(STRING_limpa) == 0:
                return 20
            else:
                return coletar_dias(STRING_limpa)
        else:
            return coletar_dias(STRING_limpa)
    else:
        return coletar_dias(STRING_limpa)