import tkinter as tk
from tkinter import messagebox
import subprocess

# Função para executar o Projeto 1
def executar_projeto1():
    try:
        subprocess.run(["python", "a.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Erro ao executar o Projeto 1: {e}")

# Função para executar o Projeto 2
def executar_projeto2():
    try:
        subprocess.run(["python", "m.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Erro ao executar o Projeto 2: {e}")

# Função para executar o Projeto 3
def executar_projeto3():
    try:
        subprocess.run(["python", "o.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Erro ao executar o Projeto 3: {e}")

# Criando a janela principal
root = tk.Tk()
root.title("Interface para Projetos")

# Criando os botões para cada projeto
btn_projeto1 = tk.Button(root, text="Executar Projeto 1", command=executar_projeto1)
btn_projeto1.pack(pady=10)

btn_projeto2 = tk.Button(root, text="Executar Projeto 2", command=executar_projeto2)
btn_projeto2.pack(pady=10)

btn_projeto3 = tk.Button(root, text="Executar Projeto 3", command=executar_projeto3)
btn_projeto3.pack(pady=10)

# Iniciando a interface gráfica
root.mainloop()
    