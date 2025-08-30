# Dicionário com nomes de alunos e suas notas
alunos_notas = {
    "Alice": [8.5, 9.0, 7.8],
    "Bruno": [6.5, 7.0, 8.0],
    "Clara": [9.5, 9.2, 10.0]
}

# Laço 'for' para iterar sobre os itens do dicionário
for nome_aluno, notas in alunos_notas.items():
    media = sum(notas) / len(notas)
    print(f"A média de {nome_aluno} é: {media:.2f}")