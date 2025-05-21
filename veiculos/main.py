from models.Veiculos import Veiculos
from models.CarroCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletrico import CarroConvEletrico
from models.Carro import Carro
from models.Moto import Moto
from models.Caminhao import Caminhao
from models.Frota import Frota


carro1 = Carro("ABC1234", "Onix", "Chevrolet", 2022, "Branco", 60000.0, 100)
moto1 = Moto("XYZ5678", "Fazer", "Yamaha", 2020, "Preta", 20000.0, 200)
caminhao1 = Caminhao("DEF3456", "FH", "Volvo", 2019, "Cinza", 450000.0, 300)
carroElet = CarroEletrico("CCC1234", "Tesla", "Tesla", 2023, "Vermelho", 300000, 5, 4, 90, "Lítio", 400)

frota = Frota(carro1)
frota.add_veiculo(moto1)
frota.add_veiculo(caminhao1)
frota.consumo_Total(100)
print("Consumo total da frota:", frota.consumo_Total(100), "litros")
"""


print(carro1==moto1)
carro1.set_Placa("ABC1235")
print(carro1.get_Placa())

carroElet.recarregar(10)
print(carroElet)
veiculos = [carro1, moto1, carroElet]
distancia = 100
for v in veiculos:
    print(f"Consumo de {v.get_Placa()} para {distancia} km: {v.calcular_consumo(distancia)}")
    """