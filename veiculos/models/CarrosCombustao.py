from .Veiculos import Veiculos
class CarrosCombustao(Veiculos):
    """Classe que representa um carro a combustão, herda de Veiculos"""
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float, combustivel: str, nPortas: int, nAssentos: int, nCilindradas: int, nCambio: str,nivel_combustivel:int) -> None:
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindradas = nCilindradas
        self.__nCambio = nCambio
        self.__nivel_combustivel = nivel_combustivel
    def __str__(self) -> str:
        infos = super().__str__()
        infos += f"combustivel:{self.__combustivel}\n"
        infos += f"nPortas:{self.__nPortas}\n"
        infos += f"nAssentos:{self.__nAssentos}\n"
        infos += f"nCilindradas:{self.__nCilindradas}\n"
        infos += f"nCambio:{self.__nCambio}\n"
        infos += f"nivel_combustivel:{self.__nivel_combustivel}\n"
        return infos
    def abastecer(self, percentual: int) -> bool:
        """
        Argumentos: 
            percentual(int): percentual adicionado
        retorno:
            bool: True se foi possivel abastecer, e false se não
        """
        novo_percentual = self.__nivel_combustivel + percentual
        if novo_percentual <= 100:
            self.__nivel_combustivel = novo_percentual
            return True
        return False
        