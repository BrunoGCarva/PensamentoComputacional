from .Veiculos import Veiculos

class Moto(Veiculos):
    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe, distancia):
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe, distancia)

    def __str__(self):
        return super().__str__() + f"Consumo: {self.distancia / 20:.2f} L\n"

    def calcular_consumo(self, distancia: float) -> float:
        consumo = distancia / 20
        return consumo