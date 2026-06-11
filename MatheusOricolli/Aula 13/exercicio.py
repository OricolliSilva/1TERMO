#Exercício - Crie uma aplicação que faça o calculo da idade de pessoas
#Deve perguntar o nome da pessoa e o ano de nascimento 

import tkinter as tk
from tkinter import messagebox

def calcular_idade():
    ano_atual = 2026
    nome_usuario = ent_nome_usuario.get()
    
    try:
        ano_nascimento = int(ent_ano_nascimento.get())
        idade = ano_atual - ano_nascimento
        
        messagebox.showinfo("Resultado", f"Olá {nome_usuario}, você tem {idade} anos!")
    except ValueError:
        messagebox.showerror("Erro, digite um ano de nascimento correto.")
    resultado_texto = (
            f"Nome: {nome_usuario}\n"
            f"Ano de nascimento: {ano_nascimento.get()}\n"
        )
        
janela = tk.Tk()
janela.title("Calculo de idade")
janela.geometry("400x500")
janela.configure(bg="#C8A2C8")

lbl_nome_usuario = tk.Label(janela, text="Digite seu nome:", font=("Arial", 14),fg="white", bg="#C8A2C8")
lbl_nome_usuario.grid(row=10, column=0, pady=0, padx=80)
lbl_ano_nascimento = tk.Label(janela, text="Digite seu ano de nascimento:", font=("Arial", 14), fg="white", bg="#C8A2C8")
lbl_ano_nascimento.grid(row=13, column=0, pady=0, padx=80)

ent_nome_usuario = tk.Entry(janela, font=("Arial, 14"), width=30)
ent_nome_usuario.grid(row=11, column=0, pady=10, padx=35)
ent_ano_nascimento = tk.Entry(janela, font=("Arial, 14"), width=30,)
ent_ano_nascimento.grid(row=14, column=0, pady=10, padx=35)

btn_calcular = tk.Button(janela, text="Calcular Idade", font=("Arial", 14), command=calcular_idade)
btn_calcular.grid(row=15, column=0, pady=20, padx=35)


janela.mainloop()