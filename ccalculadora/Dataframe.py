import pandas as pd 

# Dados dos alunos
dados_alunos = {
    'nome': ['Alice', 'Bob', 'Carlos', 'Diana'],
    'nota': [7.5, 5.0, 8.0, 6.0]
}

df = pd.DataFrame(dados_alunos)  # Cria o DataFrame

# Adiciona coluna de status
df['status'] = df['nota'].apply(lambda x: 'Aprovado' if x >= 6 else 'Reprovado')

print(df)  # Mostra o DataFrame
