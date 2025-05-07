class filmes:
    def __init__(self, titulo,genero,duracao,avaliacao):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.avaliacao = avaliacao
    def avaliar(self, avaliacao):
        if avaliacao >= 0 and avaliacao <= 10:
            self.avaliacao = avaliacao
            print(f"Avaliação do filme '{self.titulo}' atualizada para {self.avaliacao}/10 com sucesso.")
        else:
            print("Avaliação inválida. A avaliação deve ser entre 0 e 10.")
    def exibir_info(self):
        print("Informações do Filme:")
        print("---------------------")
        print(f"Título: {self.titulo}")
        print(f"Gênero: {self.genero}")
        print(f"Duração: {self.duracao} minutos")
        print(f"Avaliação: {self.avaliacao}/10")
        print("---------------------")