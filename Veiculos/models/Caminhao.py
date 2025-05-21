from .Veiculos import Veiculos
from .Frota  import Frota

class Caminhao(Veiculos):
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float,distancia:float) -> None:
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe
        self.distancia = distancia
    def __str__(self) -> str:
        infos = f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Valor Fipe: {self.__valor_fipe}\n"
        infos += f"Consumo: {self.distancia /5}\n"
        return infos
    def calcular_consumo(self,distancia:float) -> float:
        consumo = 12 
        consumototal = self.distancia / consumo
        return consumototal
        
        
    
