print('calculadora')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão') 
opcao = int(input('escolha uma opção: '))
num1 = float(input('informe o primeiro numero: '))
num2 = float(input('informe o segundo numero numero: '))

if opcao ==1:
     print(num1 + num2)
elif opcao ==2:
     print(num1 - num2)
elif opcao ==3:
     print(num1 * num2)
else:
    if num2 != 0:
        print(num1 / num2)
    else: 
        print('divisão invalida')