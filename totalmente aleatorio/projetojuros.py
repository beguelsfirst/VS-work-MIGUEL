    # O objetivo geral deste projeto é criar uma ferramenta que calcule e visualize o crescimento de um investimento ao longo dos anos com base na fórmula de juros compostos. Ele permite que o usuário insira o valor inicial do investimento, a taxa de juros anual e a duração em anos. Com esses dados, o programa calcula o montante acumulado a cada ano e gera um gráfico que mostra o crescimento do investimento ao longo do tempo, facilitando a compreensão do impacto dos juros compostos.


    #ENTRADA = valor inicial, taxa de juros, anos
    #PROCESSAMENTO = montante acumulado e cauculo do gráfico
    #SAÍDA = gráfico e montante final


import matplotlib.pyplot as plt

def calcular_montante(valor_inicial, taxa_juros, anos):
    return valor_inicial * (1 + taxa_juros)** anos

valor_inicial = float(input('Informe o valor inicial do investimento: R$ '))
taxa_juros = float(input('Informe a taxa de juros anual (em %): ')) / 100
anos = int(input('Informe o número de anos de investimentos: '))

montantes = []

for ano in range(1, anos + 1):
    montante = calcular_montante(valor_inicial, taxa_juros, ano)
    montantes.append(montante)

montante_final = montantes[-1]
print(f'o montante final após {anos} anos será de R$: {montante_final:.2f}')

    # criando a grafico

anos_list = list(range(1, anos + 1))
plt.plot(anos_list, montantes, marker='o')

plt.title('aumento do investimento com juros')
plt.xlabel('anos')
plt.ylabel('montante (R$ )')


plt.show()