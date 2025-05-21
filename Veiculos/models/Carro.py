from .Veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe, distancia):
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe, distancia)

    def __str__(self):
        return super().__str__() + f"Consumo: {self.distancia / 12:.2f} L\n"

    def calcular_consumo(self, distancia: float) -> float:
        consumo = distancia / 12
        return consumo