capital_inicial = float(input('informe o valor inicial: '))
juros = float(input('informe a taxa de juros anual(em %): ')) /100
tempo = int(input('informe o tempo em anos: '))

montante_final = capital_inicial * (juros + 1)**tempo

print(montante_final)