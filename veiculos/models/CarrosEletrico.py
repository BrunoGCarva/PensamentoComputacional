from .Veiculos import Veiculos
class CarrosEletrico(Veiculos):
    """Classe que implementa métodos especificos de carros elétricos
    Argumentos: Classe api Veiculos
    """
    def __init__(self, placa:str, modelo: str, marca: str, ano:int, cor: str, valor_fipe:float, mAssentos:int, nPortas:int,nivel_bateria:int, tipo_bateria:str,autonomia:int):
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self.__nAssentos = mAssentos
        self.__nPortas = nPortas
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia
    def __str__(self) -> str:
        infos = super().__str__()
        infos += f"Número de assentos:{self.__nAssentos}\n"
        infos += f"Número de portas:{self.__nPortas}\n"
        infos += f"Nível da bateria:{self.__nivel_bateria}\n"
        infos += f"Tipo da bateria:{self.__tipo_bateria}\n"
        infos += f"Autonomia:{self.__autonomia}\n"
        return infos
        
        