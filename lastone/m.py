import tkinter as tk
from tkinter import messagebox

# Função para exibir o resultado final
def mostrar_resultado(pontos):
    if pontos == 5:
        resultado = "Parabéns! Você tem um bom conhecimento em educação financeira!"
    elif pontos >= 3:
        resultado = "Bom trabalho! Você tem uma boa base de educação financeira."
    else:
        resultado = "Parece que você tem algumas oportunidades para melhorar seu conhecimento em finanças."
    
    messagebox.showinfo("Resultado", f"Você acertou {pontos} de 5 perguntas.\n\n{resultado}")

# Funções para cada pergunta do quiz
def pergunta_1():
    resposta = resposta_var_1.get()
    if resposta == "a":
        return 1
    else:
        return 0

def pergunta_2():
    resposta = resposta_var_2.get()
    if resposta == "a":
        return 1
    else:
        return 0

def pergunta_3():
    resposta = resposta_var_3.get()
    if resposta == "b":
        return 1
    else:
        return 0

def pergunta_4():
    resposta = resposta_var_4.get()
    if resposta == "a":
        return 1
    else:
        return 0

def pergunta_5():
    resposta = resposta_var_5.get()
    if resposta == "b":
        return 1
    else:
        return 0

# Função para calcular a pontuação e exibir o resultado
def calcular_pontuacao():
    pontos = 0
    pontos += pergunta_1()
    pontos += pergunta_2()
    pontos += pergunta_3()
    pontos += pergunta_4()
    pontos += pergunta_5()
    
    mostrar_resultado(pontos)

# Configuração da janela principal
root = tk.Tk()
root.title("Quiz de Educação Financeira")
root.geometry("400x400")  # Tamanho da janela

# Texto inicial
intro_label = tk.Label(root, text="Responda as perguntas abaixo", font=("Arial", 14))
intro_label.pack(pady=10)

# Pergunta 1
pergunta_1_label = tk.Label(root, text="1. O que é um orçamento pessoal?")
pergunta_1_label.pack()
resposta_var_1 = tk.StringVar(value="")  # Variável para a resposta
opcao_1a = tk.Radiobutton(root, text="a) Controlar as suas receitas e despesas mensais.", variable=resposta_var_1, value="a")
opcao_1a.pack()
opcao_1b = tk.Radiobutton(root, text="b) Gastar mais do que ganha.", variable=resposta_var_1, value="b")
opcao_1b.pack()
opcao_1c = tk.Radiobutton(root, text="c) Investir em ações de alto risco.", variable=resposta_var_1, value="c")
opcao_1c.pack()

# Pergunta 2
pergunta_2_label = tk.Label(root, text="2. O que é uma conta bancária?")
pergunta_2_label.pack()
resposta_var_2 = tk.StringVar(value="")
opcao_2a = tk.Radiobutton(root, text="a) Um lugar onde você guarda seu dinheiro de forma segura e pode fazer transações.", variable=resposta_var_2, value="a")
opcao_2a.pack()
opcao_2b = tk.Radiobutton(root, text="b) Um tipo de investimento de alto risco.", variable=resposta_var_2, value="b")
opcao_2b.pack()
opcao_2c = tk.Radiobutton(root, text="c) Um tipo de empréstimo com juros baixos.", variable=resposta_var_2, value="c")
opcao_2c.pack()

# Pergunta 3
pergunta_3_label = tk.Label(root, text="3. O que significa 'poupança'?")
pergunta_3_label.pack()
resposta_var_3 = tk.StringVar(value="")
opcao_3a = tk.Radiobutton(root, text="a) Gastar todo o dinheiro que você recebe.", variable=resposta_var_3, value="a")
opcao_3a.pack()
opcao_3b = tk.Radiobutton(root, text="b) Guardar parte do seu dinheiro para o futuro.", variable=resposta_var_3, value="b")
opcao_3b.pack()
opcao_3c = tk.Radiobutton(root, text="c) Investir em produtos de alto risco.", variable=resposta_var_3, value="c")
opcao_3c.pack()

# Pergunta 4
pergunta_4_label = tk.Label(root, text="4. Qual é a principal função de uma fatura de cartão de crédito?")
pergunta_4_label.pack()
resposta_var_4 = tk.StringVar(value="")
opcao_4a = tk.Radiobutton(root, text="a) Mostrar quanto você deve pagar ao banco referente aos seus gastos.", variable=resposta_var_4, value="a")
opcao_4a.pack()
opcao_4b = tk.Radiobutton(root, text="b) Informar o valor de um empréstimo pessoal.", variable=resposta_var_4, value="b")
opcao_4b.pack()
opcao_4c = tk.Radiobutton(root, text="c) Mostrar a taxa de juros do seu cartão.", variable=resposta_var_4, value="c")
opcao_4c.pack()

# Pergunta 5
pergunta_5_label = tk.Label(root, text="5. O que é uma despesa variável?")
pergunta_5_label.pack()
resposta_var_5 = tk.StringVar(value="")
opcao_5a = tk.Radiobutton(root, text="a) Uma despesa que ocorre de forma fixa todo mês.", variable=resposta_var_5, value="a")
opcao_5a.pack()
opcao_5b = tk.Radiobutton(root, text="b) Uma despesa que pode variar de mês para mês, como compras e lazer.", variable=resposta_var_5, value="b")
opcao_5b.pack()
opcao_5c = tk.Radiobutton(root, text="c) Uma despesa que você não precisa pagar.", variable=resposta_var_5, value="c")
opcao_5c.pack()

# Botão para calcular a pontuação
calcular_btn = tk.Button(root, text="Calcular Pontuação", command=calcular_pontuacao)
calcular_btn.pack(pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()
