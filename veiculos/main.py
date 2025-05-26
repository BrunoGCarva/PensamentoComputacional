from models.Veiculos import Veiculos
from models.CarroCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletrico import CarroConvEletrico
from models.Carro import Carro
from models.Moto import Moto
from models.Caminhao import Caminhao
from models.Frota import Frota


frota = Frota()


try:
    tipo = input("Digite o tipo de veículo (Carro, Moto, Caminhao): ").lower()
    distancia = float(input("Digite a distância da viagem (km): "))
    placa = input("Digite a placa (formato LLLNLNN): ").upper()

    if tipo == "carro":
        veiculo = Carro(placa, "Onix", "Chevrolet", 2020, "Branco", 60000, distancia)
    elif tipo == "moto":
        veiculo = Moto(placa, "Fazer", "Yamaha", 2021, "Preta", 22000, distancia)
    elif tipo == "caminhao":
        veiculo = Caminhao(placa, "FH", "Volvo", 2019, "Prata", 300000, distancia)
    else:
        raise ValueError("Tipo de veículo inválido!")

    veiculo.set_placa(placa)
    print(f"\nConsumo para {distancia} km: {veiculo.calcular_consumo(distancia):.2f}")
    frota.add_frota(veiculo)

except ValueError as ve:
    print("Erro de valor:", ve)

except PlacaInvalidaException as e:
    print(e)

except Exception as erro:
    print("Erro inesperado:", erro)

try:
    distancia = float(input("\nDigite uma nova distância para calcular consumo total da frota: "))
    if distancia <= 0:
        raise ValueError("A distância deve ser positiva!")

    if len(frota._Frota__frota) == 0:
        raise Exception("A frota está vazia!")

    total = frota.consumo_Total(distancia)
    print(f"\nConsumo total da frota para {distancia} km: {total:.2f}")

except Exception as e:
    print("Erro:", e)