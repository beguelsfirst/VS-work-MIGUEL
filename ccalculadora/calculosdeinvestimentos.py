import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a média mensal
def calcular_media_mensal(valores):
    soma = np.sum(valores)
    quantidade_meses = len(valores)
    media = soma / quantidade_meses
    return media

# Função para obter os dados do usuário
def obter_dados_mensais():
    valores = []
    print("Por favor, insira sua renda mensal para os próximos 6 meses:")
    for i in range(6):
        while True:
            try:
                valor = float(input(f"Renda do Mês {i + 1}: R$ "))
                if valor < 0:
                    print("O valor deve ser positivo. Tente novamente.")
                else:
                    valores.append(valor)
                    break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
    return valores

# Obter dados do usuário
valores_mensais = obter_dados_mensais()

# Calcular a média
media_mensal = calcular_media_mensal(valores_mensais)

# Criar gráfico
meses = ['Mês 1', 'Mês 2', 'Mês 3', 'Mês 4', 'Mês 5', 'Mês 6']

plt.style.use('dark_background')  # Usar o estilo de fundo escuro do matplotlib

plt.figure(figsize=(10, 6))

# Plotar os valores mensais
plt.plot(meses, valores_mensais, marker='o', linestyle='-', color='#FDFFE2', label='Renda Mensal')  # Roxo claro

# Plotar a média
plt.axhline(y=media_mensal, color='#D1C4E9', linestyle='--', label=f'Média Mensal = R$ {media_mensal:.2f}')  # Roxo mais claro

# Ajustar o fundo do gráfico
plt.gca().set_facecolor('#121212')  # Cor de fundo escuro

# Adicionar título e rótulos
plt.title('Renda Mensal e Média ao Longo de 6 Meses', color='#EDE7F6')  # Título roxo claro
plt.xlabel('Meses', color='#1230AE')  # Rótulo do eixo X roxo claro
plt.ylabel('Renda (R$)', color='#6C48C5')  # Rótulo do eixo Y roxo claro

# Adicionar legenda
plt.legend(facecolor='#333333', edgecolor='#444444')  # Fundo e borda da legenda

# Ajustar a grade e a borda
plt.grid(True, linestyle='--', color='#BF2EF0')  # Grade cinza escura
plt.tick_params(axis='both', colors='#2E073F')  # Cores dos ticks roxas claras

# Exibir o gráfico
plt.show()
