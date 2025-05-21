from .CarroCombustao import CarroCombustao
from .CarroEletrico import CarroEletrico

class CarroConvEletrico(CarroCombustao, CarroEletrico):
    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe,
                 combustivel, nPortas, nAssentos, nCilindrada, nCambio,
                 nivel_combustivel, nivel_bateria, tipo_bateria, autonomia):

        CarroCombustao.__init__(self, placa, modelo, marca, ano, cor, valor_fipe,
                                 combustivel, nPortas, nAssentos, nCilindrada, nCambio, nivel_combustivel)

        CarroEletrico.__init__(self, placa, modelo, marca, ano, cor, valor_fipe,
                                nAssentos, nPortas, nivel_bateria, tipo_bateria, autonomia)

    def __str__(self):
        infos = CarroCombustao.__str__(self)
        infos += f"Nivel de bateria: {self.get_nivel_bateria()}\n"
        infos += f"Tipo de bateria: {self.get_tipo_bateria()}\n"
        infos += f"Autonomia: {self.get_autonomia()}\n"
        return infos

    def abastecer(self, percentual_adicionado: float) -> bool:
        print("Carro convertido para elétrico! Não é mais possível abastecer!")
        return False