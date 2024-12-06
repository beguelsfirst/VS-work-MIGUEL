import random
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

# Função para simular o impacto do mercado nos investimentos
def simular_mercado(tipo_investimento, saldo):
    if tipo_investimento == "ações":
        variacao = random.uniform(-0.2, 0.3)  # Mercado de ações pode ter grandes variações
    elif tipo_investimento == "renda fixa":
        variacao = random.uniform(0.02, 0.1)  # Renda fixa é mais estável
    elif tipo_investimento == "poupança":
        variacao = random.uniform(0.01, 0.03)  # Poupança, bem conservadora
    else:
        variacao = 0.0  # Se não for um investimento conhecido, nada acontece

    # Calcula o novo saldo com base na variação
    saldo += saldo * variacao
    return saldo, variacao

# Função para gerar eventos econômicos aleatórios
def evento_economico():
    eventos = [
        ("Recessão", random.uniform(-0.15, -0.05)),
        ("Boom Econômico", random.uniform(0.15, 0.3)),
        ("Inflação Alta", random.uniform(-0.1, -0.02)),
        ("Crescimento Estável", random.uniform(0.05, 0.1))
    ]
    evento = random.choice(eventos)
    return evento[0], evento[1]

# Função para atualizar o saldo na interface gráfica
def atualizar_saldo():
    saldo_label.config(text=f"Saldo: R${saldo:.2f}")

# Função para exibir o impacto do investimento
def exibir_impacto(tipo_investimento, saldo, variacao, evento_nome, evento_variacao):
    impacto_texto = f"\nVocê escolheu investir em {tipo_investimento}.\n"
    impacto_texto += f"A variação do mercado foi de {variacao*100:.2f}%.\n"
    impacto_texto += f"Evento Econômico: {evento_nome}!\nO impacto foi de {evento_variacao*100:.2f}%.\n"
    impacto_label.config(text=impacto_texto)

# Função para exibir o histórico de investimentos
def exibir_historico():
    historico_texto = "\nHistórico de Investimentos:\n"
    for i, (tipo, saldo, variacao) in enumerate(historico):
        historico_texto += f"Rodada {i+1}: Investimento em {tipo} | Saldo: R${saldo:.2f} | Variação: {variacao*100:.2f}%\n"
    historico_texto_widget.config(state=tk.NORMAL)
    historico_texto_widget.delete(1.0, tk.END)
    historico_texto_widget.insert(tk.END, historico_texto)
    historico_texto_widget.config(state=tk.DISABLED)

# Função para gerar o gráfico da evolução do saldo
def gerar_grafico():
    fig, ax = plt.subplots()
    ax.plot(saldos, marker='o', color='blue')
    ax.set_title("Evolução do Saldo ao Longo do Tempo")
    ax.set_xlabel("Rodadas")
    ax.set_ylabel("Saldo (R$)")
    ax.grid(True)

    # Mostrar o gráfico na interface gráfica
    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Função para começar o jogo
def jogar(tipo_investimento):
    global saldo, historico, saldos
    if saldo <= 0:
        messagebox.showinfo("Fim do Jogo", f"Você ficou sem dinheiro. Seu saldo final foi R${saldo:.2f}.")
        return

    # Atualiza o saldo na interface
    saldos.append(saldo)

    # Simula o impacto do mercado
    saldo, variacao = simular_mercado(tipo_investimento, saldo)

    # Gera evento econômico
    evento_nome, evento_variacao = evento_economico()
    saldo += saldo * evento_variacao

    # Atualiza o impacto do investimento
    exibir_impacto(tipo_investimento, saldo, variacao, evento_nome, evento_variacao)

    # Salva o histórico
    historico.append((tipo_investimento, saldo, variacao))

    # Atualiza o saldo na interface
    atualizar_saldo()

    # Exibe o histórico de investimentos
    exibir_historico()

# Função para começar o jogo com um botão
def escolha_acao():
    tipo_investimento = "ações"
    jogar(tipo_investimento)

def escolha_renda_fixa():
    tipo_investimento = "renda fixa"
    jogar(tipo_investimento)

def escolha_poupanca():
    tipo_investimento = "poupança"
    jogar(tipo_investimento)

# Função para mostrar o gráfico ao final do jogo
def finalizar_jogo():
    gerar_grafico()
    messagebox.showinfo("Fim do Jogo", "O jogo acabou! O gráfico foi gerado.")

# Função para reiniciar o jogo
def reiniciar_jogo():
    global saldo, historico, saldos
    saldo = 1000  # Dinheiro inicial do jogador
    historico = []  # Limpa o histórico de investimentos
    saldos = [saldo]  # Limpa o histórico de saldos
    atualizar_saldo()
    historico_texto_widget.config(state=tk.NORMAL)
    historico_texto_widget.delete(1.0, tk.END)
    historico_texto_widget.config(state=tk.DISABLED)
    impacto_label.config(text="")

# Criar a janela principal
janela = tk.Tk()
janela.title("Simulação de Investimentos")
janela.geometry("600x600")

# Inicialização das variáveis
saldo = 1000
historico = []  # Histórico de investimentos
saldos = [saldo]  # Para gráfico

# Rótulo do saldo
saldo_label = tk.Label(janela, text=f"Saldo: R${saldo:.2f}", font=("Arial", 16))
saldo_label.pack(pady=20)

# Botões para escolha de investimento
botao_acoes = tk.Button(janela, text="Investir em Ações", width=20, command=escolha_acao)
botao_acoes.pack(pady=5)

botao_renda_fixa = tk.Button(janela, text="Investir em Renda Fixa", width=20, command=escolha_renda_fixa)
botao_renda_fixa.pack(pady=5)

botao_poupanca = tk.Button(janela, text="Investir na Poupança", width=20, command=escolha_poupanca)
botao_poupanca.pack(pady=5)

# Rótulo para mostrar impacto do investimento
impacto_label = tk.Label(janela, text="", font=("Arial", 12), justify=tk.LEFT)
impacto_label.pack(pady=20)

# Campo de texto para histórico
historico_texto_widget = tk.Text(janela, height=8, width=50, wrap=tk.WORD, state=tk.DISABLED)
historico_texto_widget.pack(pady=10)

# Botões de finalização e reinício
botao_finalizar = tk.Button(janela, text="Finalizar Jogo", width=20, command=finalizar_jogo)
botao_finalizar.pack(pady=5)

botao_reiniciar = tk.Button(janela, text="Reiniciar Jogo", width=20, command=reiniciar_jogo)
botao_reiniciar.pack(pady=5)

# Iniciar a interface gráfica
janela.mainloop()
    