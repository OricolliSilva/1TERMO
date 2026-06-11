# Revisão Tkinter

import tkinter as tk
from tkinter import messagebox, ttk

#DEF funçoes em bloco
def cadastrar_usuario():
    #get.
    nome_usuario = ent_nome_usuario.get()
    curso_usuario = ent_curso_usuario.get()
    nome_escola = cmb_nome_escola.get()

    if nome_usuario == "" and curso_usuario == "" and nome_escola =="":
        messagebox.showwarning("Bem-Vindo", "Digite seu nome, seu curso e sua escola")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá {nome_usuario}! Seu curso é {curso_usuario} e sua escola é {nome_escola}")


# 0 - Etapa Janela
janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("400x500")
janela.configure(bg="blue")

# 1 - Etapa Componentes
#print = label(lbl)
#input = Entry
lbl_nome_usuario = tk.Label(janela, text="Digite seu nome:", font=("Arial", 14),fg="white", bg="blue")
lbl_nome_usuario.grid(row=10, column=0, pady=0, padx=80)
lbl_curso_usuario = tk.Label(janela, text="Digite seu curso:", font=("Arial", 14), fg="white", bg="blue")
lbl_curso_usuario.grid(row=13, column=0, pady=0, padx=80)
lbl_nome_escola =tk.Label(janela, text="Selecione sua escola:", font=("Arial,", 14), fg="white", bg="blue" )
lbl_nome_escola.grid(row=15, column=0, pady=0, padx=80 )

# Entrys = Caixa de texto antigas input 
ent_nome_usuario = tk.Entry(janela, font=("Arial, 14"), width=30)
ent_nome_usuario.grid(row=11, column=0, pady=10, padx=35)
ent_curso_usuario = tk.Entry(janela, font=("Arial, 14"), width=30,)
ent_curso_usuario.grid(row=14, column=0, pady=10, padx=35)

#ComboBox = Caixa de seleção
cmb_nome_escola = ttk.Combobox(janela, values=["SESI408", "SESI05"], font=("Arial", 14) , state="readonly")
cmb_nome_escola.grid(row=16, column=0, pady=10, padx=35)

# - Botões de 
btn_realizar_cadastro = tk.Button(janela, text="Cadastrar", font=("Arial", 14), fg="white", bg="blue", command=cadastrar_usuario)
btn_realizar_cadastro.grid(row=17, column=0, pady=10, padx=80 )
btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), fg="white", bg="blue", command=janela.destroy)
btn_fechar_janela.grid(row=18, column=0, pady=10, padx=80)
# 4 - Etapa loop
janela.mainloop()