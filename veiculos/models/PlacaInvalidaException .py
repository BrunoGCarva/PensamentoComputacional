class PlacaInvalidaException (Exception):
    def __init__(self, mensagem="Placa inválida! Use o formato LLLNLNN"):
        super().__init__(mensagem)