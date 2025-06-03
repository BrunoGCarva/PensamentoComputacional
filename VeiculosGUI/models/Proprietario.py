import re

class Proprietario:
    def __init__(self, nome, cpf):
        if not self.validar_cpf(cpf):
            raise ValueError("CPF inválido")
        self.nome = nome
        self.cpf = cpf
        self.placas = []

    def adicionar_veiculo(self, placa):
        if not self.validar_placa(placa):
            raise ValueError("Placa inválida")
        self.placas.append(placa)
    def validar_cpf(cpf):
        return re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf) is not None
    def validar_placa(placa):
        return re.match(r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$', placa) is not None
    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf} - Veículos: {', '.join(self.placas) if self.placas else 'Nenhum'}"
