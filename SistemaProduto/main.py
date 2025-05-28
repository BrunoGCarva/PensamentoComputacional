from models.produto_alimenticio import ProdutoAlimenticio
from models.produto_eletronico import ProdutoEletronico
from models.conversor import ConversorMoeda
from models.Exceptions import MoedaInvalidaError
def main():
    try:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto em BRL: "))
        tipo = input("Tipo do produto ('alimenticio' ou 'eletronico'): ").lower()

        if tipo == "alimenticio":
            produto = ProdutoAlimenticio(nome, preco)
        elif tipo == "eletronico":
            produto = ProdutoEletronico(nome, preco)
        else:
            print("Tipo de produto inválido.")
            return

        conversor = ConversorMoeda()

        try:
            convertido = conversor.converte_preco_para_usd(produto)
            if convertido:
                print("Preço convertido para USD com sucesso!")
        except MoedaInvalidaError as e:
            print(f"Erro de conversão: {e}")

        print("Informações do produto:")
        print(produto)

    except ValueError:
        print("Erro: O preço deve ser um número válido.")

if __name__ == "__main__":
    main()