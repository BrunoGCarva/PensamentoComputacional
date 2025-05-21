from .Veiculos import Veiculos

class Frota:
    def __init__(self, veiculo: Veiculos):
        self.__frota = [veiculo]

    def add_veiculo(self, veiculo: Veiculos) -> bool:
        self.__frota.append(veiculo)
        return True

    def consumo_Total(self, distancia):
        consumo_Total = 0
        for veiculo in self.__frota:

            consumo_Total += veiculo.calcular_consumo(distancia)
        return consumo_Total
    def listar_veiculos(self):
        for v in self.__frota:
            print(v)
            print("-" * 30)
