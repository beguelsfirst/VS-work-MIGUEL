import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Função para calcular o montante de juros compostos
def calcular_juros_compostos(principal, taxa_juros, tempo):
    montante = principal * (1 + taxa_juros) ** tempo
    return montante

# Função para exibir o gráfico e resultado
def exibir_resultado():
    try:
        # Obtendo os dados da interface
        principal = float(entry_principal.get())
        taxa_juros = float(entry_taxa.get()) / 100
        tempo = int(entry_tempo.get())

        # Listas para armazenar o progresso do montante e do tempo
        anos = list(range(0, tempo+1))
        montantes = [calcular_juros_compostos(principal, taxa_juros, t) for t in anos]

        # Montante final
        montante_final = montantes[-1]
        resultado_label.config(text=f"Montante final após {tempo} anos: R${montante_final:.2f}")

        # Criando o gráfico
        plt.plot(anos, montantes, marker='o', color='b', label="Montante")
        plt.title("Progresso do Montante com Juros Compostos")
        plt.xlabel("Tempo (anos)")
        plt.ylabel("Montante (R$)")
        plt.grid(True)
        plt.legend()
        plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para todos os campos.")

# Função para configurar a interface
def configurar_interface():
    # Criando a janela principal
    window = tk.Tk()
    window.title("Cálculo de Juros Compostos")

    # Criando os widgets de entrada
    tk.Label(window, text="Capital inicial (R$):").grid(row=0, column=0, padx=10, pady=5)
    global entry_principal
    entry_principal = tk.Entry(window)
    entry_principal.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(window, text="Taxa de juros anual (%):").grid(row=1, column=0, padx=10, pady=5)
    global entry_taxa
    entry_taxa = tk.Entry(window)
    entry_taxa.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(window, text="Número de anos:").grid(row=2, column=0, padx=10, pady=5)
    global entry_tempo
    entry_tempo = tk.Entry(window)
    entry_tempo.grid(row=2, column=1, padx=10, pady=5)

    # Botão para calcular e exibir resultados
    calcular_button = tk.Button(window, text="Calcular", command=exibir_resultado)
    calcular_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Label para exibir o resultado
    global resultado_label
    resultado_label = tk.Label(window, text="Montante final: R$")
    resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

    # Iniciar a interface
    window.mainloop()

if __name__ == "__main__":
    configurar_interface()
