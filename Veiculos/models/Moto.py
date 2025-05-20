from turtle import distance
from .Veiculos import Veiculos
class Moto(Veiculos):
    """
    Classe que representa uma moto, herda de Veiculos
    """

    def __init__(self,
                 placa: str,
                 modelo: str,
                 marca: str,
                 ano: int,
                 cor: str,
                 valor_fipe: float,
                 distancia: float) -> None:
                 
        Veiculos.__init__(self,
                          placa=placa,
                          modelo=modelo,
                          marca=marca,
                          ano=ano,
                          cor=cor,
                          valor_fipe=valor_fipe,
                          distancia=distancia)
        def __str__(self) -> str:
            infos = super().__str__()
            
            return infos
        def calcular_consumo(self, distancia: float) -> float:
            
            consumototal = self.distancia / 20
            return consumototal