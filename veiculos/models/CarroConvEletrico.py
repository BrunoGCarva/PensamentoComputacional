from .CarrosCombustao import CarrosCombustao
from .CarrosEletrico import CarrosEletrico

class CarrosConvEletrico(CarrosCombustao, CarrosEletrico):
    """
    Classe que implementa métodos específicos de um carro convertido em elétrico
    """
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float, combustivel: str,nPortas: int, nAssentos: int, nCilindradas: int, nCambio: str,nivel_combustivel:int,nivel_bateria:int,tipo_bateria:str,autonomia:int) -> None:
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe, combustivel, nPortas, nAssentos, nCilindradas, nCambio,nivel_combustivel)
        CarrosEletrico.__init__(self,placa,modelo, marca, ano, cor, valor_fipe, nAssentos, nPortas, nivel_bateria, tipo_bateria, autonomia)

    def __str__(self) -> str:
        infos = super().__str__()
        infos += f"Nível da bateria:{self.__nivel_bateria}\n"
        infos += f"Tipo da bateria:{self.__tipo_bateria}\n"
        infos += f"Autonomia:{self.__autonomia}\n"
        return infos
    def abastecer(self, percentual:float)-> bool:
        """
        Método abastecer desativado
        Argumentos: 
            percentual:float
        returns:
        false,pois não é possivel abastecer
        """
        print("Carro convertida para eletrico! Não é mais possivel abastecer")	