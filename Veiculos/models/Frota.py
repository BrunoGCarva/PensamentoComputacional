from .Veiculos import Veiculos


class Frota:
    """
    Classe que representa uma frota de veículos, herda de Veiculos
    """

    def __init__(self,veiculo):
        
        self.__frota = [veiculo]


    def add_frota(self,veiculo):
        """
        Adiciona um veiculo a frota
        """
        self.__frota.append(veiculo)
        return True
    def consumo_Total(self,distancia):
        consumo_total = 0
        for veiculo in self.__frota:
            consumo_total += veiculo.calcular_consumo(distancia)
        return consumo_total