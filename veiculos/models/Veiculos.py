class Veiculos:
    def __init__(self, placa:str,modelo: str, marca: str,ano:int,cor: str,valor_fipe) -> None:
        """
        Classe com as principais funcionalidade do sistema de veiculos
        Atributos: placa(str), modelo(str), marca(str), ano(int), cor(str), valor_fipe(float)
        """
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe
    def __str__(self) -> str:
        """Retorna uma string com as informações do veículo"""
        infos = f"placa:{self.__placa}\n"
        infos += f"modelo:{self.__modelo}\n"
        infos += f"marca:{self.__marca}\n"
        infos += f"ano:{self.__ano}\n"
        infos += f"cor:{self.__cor}\n"
        infos += f"valor_fipe:{self.__valor_fipe}\n"
        return infos
    
    def getPlaca(self) -> str:
        """Retira a placa"""
        return self.__placa
    def setValorFipe(self, valor:float) -> None:
        """Metodo que altera o valor da fipe do veiculo
        Argumento: valor(float): nova valor da Fipe
        Saída: True se ok
        """
        self.__valor_fipe = valor
        return True