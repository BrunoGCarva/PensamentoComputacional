from models.produto import Produto
from models.Exceptions import MoedaInvalidaError

class ConversorMoeda:
    def __init__(self):
        self.__cotacao_usd = 5.05
        self.__cotacao_eur = 6.14
        self.__cotacao_eur_usd = 1.22

    def converte_preco_para_usd(self, produto: Produto):
        moeda_atual = produto.get_moeda()
        if moeda_atual == "USD":
            return False
        elif moeda_atual == "BRL":
            novo_preco = produto.get_preco() / self.__cotacao_usd
        elif moeda_atual == "EUR":
            novo_preco = produto.get_preco() / self.__cotacao_eur_usd
        else:
            raise MoedaInvalidaError(moeda_atual)

        produto.set_preco(novo_preco)
        produto.set_moeda("USD")
        return True

    def converte_preco_para_eur(self, produto: Produto):
        moeda_atual = produto.get_moeda()
        if moeda_atual == "EUR":
            return False
        elif moeda_atual == "BRL":
            novo_preco = produto.get_preco() / self.__cotacao_eur
        elif moeda_atual == "USD":
            novo_preco = produto.get_preco() * (1 / self.__cotacao_eur_usd)
        else:
            raise MoedaInvalidaError(moeda_atual)

        produto.set_preco(novo_preco)
        produto.set_moeda("EUR")
        return True

    def converte_preco_para_brl(self, produto: Produto):
        moeda_atual = produto.get_moeda()
        if moeda_atual == "BRL":
            return False
        elif moeda_atual == "USD":
            novo_preco = produto.get_preco() * self.__cotacao_usd
        elif moeda_atual == "EUR":
            novo_preco = produto.get_preco() * self.__cotacao_eur
        else:
            raise MoedaInvalidaError(moeda_atual)

        produto.set_preco(novo_preco)
        produto.set_moeda("BRL")
        return True