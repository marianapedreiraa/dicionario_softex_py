def mesclar_dicionarios(dicionario1, dicionario2):
  """
  Mescla dois dicionários, dando prioridade aos valores do segundo.
  """
  # Criar uma cópia do primeiro dicionário para não modificar o original
  dicionario_mesclado = dicionario1.copy()

  # Atualizar o dicionário mesclado com os pares do segundo dicionário.
  dicionario_mesclado.update(dicionario2)

  return dicionario_mesclado

# Exemplo de uso:
dicionario_a = {"a": 1, "b": 2, "c": 3}
dicionario_b = {"c": 4, "d": 5, "e": 6}

dicionario_final = mesclar_dicionarios(dicionario_a, dicionario_b)

print(dicionario_final)
