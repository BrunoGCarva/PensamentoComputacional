class Veiculos:
    """
    Classe com as principais funcionalidades do sistema de veiculos, como placas, veiculos, etc.
    """
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float, distancia: float) -> None:
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
        return infos

    def get_Placa(self) -> str:
        return self.__placa
    def set_Placa(self, nova_placa: str) -> bool:
        if len(nova_placa) != 7:
            return False

        letras = nova_placa[:3]
        numeros = nova_placa[3:]

        if letras.isalpha() and numeros.isdigit():
            self.__placa = nova_placa
            return True
        return False
    def setValorFipe(self, valor: float) -> None:
        self.__valor_fipe = valor

    def calcular_consumo(self, distancia: float) -> float:
        return 0.0
