def imprime_filmes(filmes):
  for filme in filmes:
    print(f"O filme {filme['nome']} tem a nota {filme['nota']}")
def duplicidade(novo, filmes):
  for filme in filmes:
    if novo == filme['nome']:
      return True
  return False
def nota_valida(nota):
  if nota >= 0 and nota <= 10:
    return True
  return False
sum= 0
contador = 0
filmes = []
parar = False
info = "digite: add para adicionar filme,"
info += "\n        rm para apagar"
info += "\n        ed para editar"
info += "\n        sa para sair"
info += "\n -------------------------------"
while contador < 5:
  print(info)
  operacao = input()
  if operacao == "add":
    contador += 1
    nome = input("Digite o nome do filme: ").lower()
    nota = float(input("Digite a nota do filme: "))
    while not nota_valida(nota):
      print("Nota inválida !!!")
      nota = float(input("Digite a nota do filme: "))
    sum += nota
    filmes.append({"nome":nome, "nota":nota})
    print ("Filme adicionado")
    if contador>2:
      if duplicidade(nome, filmes):
        print("Filme já cadastrado")
        filmes.remove({"nome":nome, "nota":nota})
        contador -= 1
        sum -= nota

  elif operacao == "rm":
    if contador == 0:
      print("Não há filmes cadastrados")
      continue
    contador -= 1
    sum -= nota
    nome = input("Digite o nome do filme: ").lower()
    for filme in filmes:
      if nome == filme['nome']:
        filmes.remove(filme)
        print("Filme removido")

  elif operacao == "ed":
    nome = input("Digite o nome do filme a ser editado: ").lower()
    filme_encontrado = False
    for i in range(len(filmes)):
        if filmes[i]['nome'] == nome:
            filme_encontrado = True
            sum -= nota
            nota = float(input("Digite a nova nota do filme: "))
            while not nota_valida(nota):
                print("Nota inválida !!!")
                nota = float(input("Digite a nota do filme: "))
            filmes[i]['nota'] = nota

            sum += nota
            print("Filme editado")
            break
    if not filme_encontrado:
        print("Filme não encontrado")
  elif operacao == "sa":
    for filme in filmes:
      print(f"O filme {filme['nome']} tem a nota {filme['nota']}")
      print("A média das notas são", sum/contador)
    break
  else:
    print("Operação inválida")
