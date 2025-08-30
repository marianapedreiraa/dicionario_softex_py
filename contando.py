def contar_frequencia(lista_de_palavras):
  """
  Conta a frequência de cada palavra em uma lista e retorna um dicionário.
  """
  frequencia_palavras = {}
  for palavra in lista_de_palavras:
    # Se a palavra já estiver no dicionário, incrementa a contagem
    if palavra in frequencia_palavras:
      frequencia_palavras[palavra] += 1
    # Caso contrário, adiciona a palavra com a contagem inicial de 1
    else:
      frequencia_palavras[palavra] = 1
  return frequencia_palavras

# Lista de palavras fornecida 
palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

# Chamando a função e armazena o resultado
contagem = contar_frequencia(palavras)
print(contagem)