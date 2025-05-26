class Produto:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco
        self.__moeda = "BRL"

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_moeda(self):
        return self.__moeda

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        self.__preco = preco

    def set_moeda(self, moeda):
        self.__moeda = moeda

    def __str__(self):
        return f"Produto: {self.__nome}, Preço: {self.__preco:.2f} {self.__moeda}"
