from .produto import Produto

class ProdutoAlimenticio(Produto):
    def __str__(self):
        return f"[Alimento] {self.get_nome()} - {self.get_preco():.2f} {self.get_moeda()}"