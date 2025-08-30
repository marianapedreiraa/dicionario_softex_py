dicionario_original = {"a": 1, "b": 2, "c": 3}

# Cria um novo dicionário invertido usando um dicionário de compreensão
dicionario_invertido = {valor: chave for chave, valor in dicionario_original.items()}
print(dicionario_invertido)