class livro:
    def __init__(self,titulo, autor, ano_publicacao,numero_paginas, pagina_atual):
      self.titulo = titulo
      self.autor = autor
      self.ano = ano_publicacao
      self.numero_paginas = numero_paginas
      self.pagina_atual = pagina_atual
    def avancar_pagina(self):
        if self.pagina_atual < self.numero_paginas:
            self.pagina_atual += 1
    def voltar_pagina(self):
        if self.pagina_atual > 1:
            self.pagina_atual -= 1
        
    def exibir_informaçoes(self):
        print("-------------------------")
        print(f'Título: {self.titulo}\nAutor: {self.autor}\nAno de publicação: {self.ano}\nNúmero de páginas: {self.numero_paginas}\nPágina atual: {self.pagina_atual}')
        print("-------------------------")