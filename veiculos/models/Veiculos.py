class Veiculos:
    def __init__(self, modelo, marca, placa, ano, cor, velocidade, latitude, longetude):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
        self.latitude = latitude
        self.longetude = longetude
    def acelerar(self):
        self.velocidade += 10
        nova_latitude = self.latitude + 1
        self.alterarLatitude(nova_latitude)
    def frear(self):
        self.velocidade -= 10
        if self.velocidade < 0:
            self.velocidade = 0
    def Exibir_Info(self):
        print(f"o veículo {self.modelo}, de placa {self.placa} está a {self.velocidade} km/h.")
        print(f"Lat: {self.latitude}, Long: {self.longetude}")
    def AlterarPlaca(self, placa):
        self.placa = placa
    def alterarCor(self, cor):
        self.cor = cor
    def alterarAno(self, ano):
        self.ano = ano
    def alterarModelo(self, modelo):
        self.modelo = modelo
    def alterarMarca(self, marca):
        self.marca = marca
    def alterarLatitude(self, latitude):
        self.latitude = latitude
    def alterarLongetude(self, longetude):
        self.longetude = longetude