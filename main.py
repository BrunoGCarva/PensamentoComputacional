import re
def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]','', cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    padrao_formatado = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return True
cpf_formatado ='123.456.789-09'
print(f'CPF {cpf_formatado}: {'Válido' if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf_formatado)else 'Formato inválido'}')