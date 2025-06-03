from .Veiculos import Veiculos

class CarroCombustao(Veiculos):
    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe,
                 combustivel, nPortas, nAssentos, nCilindrada, nCambio, nivel_combustivel):
        Veiculos.__init__(self, placa, modelo, marca, ano, cor, valor_fipe, 0)
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindrada = nCilindrada
        self.__nCambio = nCambio
        self.__nivel_combustivel = nivel_combustivel

    def __str__(self):
        infos = super().__str__()
        infos += f"Combustivel: {self.__combustivel}\n"
        infos += f"Número de portas: {self.__nPortas}\n"
        infos += f"Número de assentos: {self.__nAssentos}\n"
        infos += f"Número de cilindrada: {self.__nCilindrada}\n"
        infos += f"Câmbio: {self.__nCambio}\n"
        infos += f"Nível Combustível: {self.__nivel_combustivel}\n"
        return infos    

    def abastecer(self, percentual_adicionado: int) -> bool:
        novo = self.__nivel_combustivel + percentual_adicionado
        if novo <= 100:
            self.__nivel_combustivel = novo
            return True
        return False 