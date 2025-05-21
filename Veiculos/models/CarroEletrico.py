from .Veiculos import Veiculos

class CarroEletrico(Veiculos):
    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe,
                 nAssentos, nPortas, nivel_bateria, tipo_bateria, autonomia):
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe, 0)
        self.__nAssentos = nAssentos
        self.__nPortas = nPortas
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia

    def __str__(self):
        infos = super().__str__()
        infos += f"Número de Assentos: {self.__nAssentos}\n"
        infos += f"Número de portas: {self.__nPortas}\n"
        infos += f"Nível da Bateria: {self.__nivel_bateria}\n"
        infos += f"Tipo da Bateria: {self.__tipo_bateria}\n"
        infos += f"Autonomia: {self.__autonomia}\n"
        return infos

    def get_nivel_bateria(self): 
        return self.__nivel_bateria
    def get_tipo_bateria(self): 
        return self.__tipo_bateria
    def get_autonomia(self): 
        return self.__autonomia
    def calcular_consumo(self, distancia: float) -> float:
        consumo_por_km = 0.15
        return distancia * consumo_por_km
    def recarregar(self, percentual_adicionado: float) -> bool:
        novo = self.__nivel_bateria + percentual_adicionado
        if novo <= 100:
            self.__nivel_bateria = novo
            return True

        