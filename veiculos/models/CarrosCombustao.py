from .Veiculos import Veiculos
class CarrosCombustao(Veiculos):
    """Classe que representa um carro a combustão, herda de Veiculos"""
    def __init__(self, placa:str, modelo: str, marca: str, ano:int, cor: str, valor_fipe:float, combustivel:str, nPortas:int, nAssentos: int, nCilindradas:int,nCambio :str) -> None:
        super().__int__(placa, modelo, marca, ano, cor, valor_fipe)
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindradas = nCilindradas
        self.__nCambio = nCambio
    def __str__(self) -> str:
        infos = super().__str__()
        infos += f"combustivel:{self.__combustivel}\n"
        infos += f"nPortas:{self.__nPortas}\n"
        infos += f"nAssentos:{self.__nAssentos}\n"
        infos += f"nCilindradas:{self.__nCilindradas}\n"
        infos += f"nCambio:{self.__nCambio}\n"
        return infos