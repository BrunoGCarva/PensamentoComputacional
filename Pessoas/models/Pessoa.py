class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    def aniversario(self):
        self.idade += 1
    def crescer(self, altura):
        self.altura += altura
    def exibir_info(self):
        print("-------------------------")
        print(f'Nome: {self.nome}\nIdade: {self.idade}\nAltura: {self.altura} cm')
        print("-------------------------")