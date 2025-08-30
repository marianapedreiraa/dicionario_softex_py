pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
pontuacoes_ordenadas = sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True)
print(pontuacoes_ordenadas)

dicionario_ordenado = dict(pontuacoes_ordenadas)
print(dicionario_ordenado)