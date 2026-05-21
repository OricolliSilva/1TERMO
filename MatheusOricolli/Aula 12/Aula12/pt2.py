# import tkinter as tk 
# from tkinter import messagebox

# def saudar_usuario():
#     # .get() serve para buscar o texto que vamos digitar 

#     nome = campo_nome.get()

#     if nome == "":
#         messagebox.showinfo("Saudações Alunos", f"Olá, {nome}! Seja bem-vindo ao mundo das intefaces gráficas")

# # Configurações da janela
# app = tk.Tk()
# app.title("Exemplo 1")
# app.geometry("350x200")

# #Componentes
# lbl_instrucao = tk.Label(app, text="Digite seu nome abaixo:")
# lbl_instrucao.pack(pady=5)

# campo_nome = tk.Entry(app, font=("Arial", 12))
# campo_nome.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=saudar_usuario)
# btn_enviar.pack(pady=15)

# app.mainloop()

#Exercicio: Crie uma interface gráfica que calcule a média de 3 notas digitadas pelo usúario. A interface deve conter campos
#para o usúario. A interface deve conter campos para o usúario inserir as notas e um botão para calcular a média
#Ao clicar no botão, a média deve ser exibida em uma mensagem 

import tkinter as tk
from tkinter import messagebox

def calcular_numeros():
    try:
        num1 = float(_numercampo_numero1.get())
        num2 = float(campoo2.get())
        num3 = float(campo_numero3.get())
        
        media = (num1 + num2 + num3) / 3
        
        messagebox.showinfo("Resultado", f"A média dos 3 números é: {media:.2f}")

    except ValueError:
 
        messagebox.showerror("Erro", "Por favor, digite números válidos em todos os campos!")


app = tk.Tk()
app.title("Página de Cálculo")
app.geometry("350x300")
app.configure(bg = "#C8A2C8")

lbl_calculo1 = tk.Label(app, text="Digite o primeiro número abaixo: \n", bg="#C8A2C8", font=("Arial", 12), fg="#2C3E50")
lbl_calculo1.pack(pady=5)

campo_numero1 = tk.Entry(app, font=("Arial", 12))
campo_numero1.pack(pady=5)

lbl_calculo2 = tk.Label(app, text="Digite o segundo número abaixo: \n", bg = "#C8A2C8", font =("Arial", 12), fg="#2C3E50")
lbl_calculo2.pack(pady=5)

campo_numero2 = tk.Entry(app, font=("Arial", 12))
campo_numero2.pack(pady=5)

lbl_calculo3 = tk.Label(app, text="Digite o terceiro número abaixo: \n", bg="#C8A2C8", font=("Arial", 12), fg="#2C3E50")
lbl_calculo3.pack(pady=5)

campo_numero3 = tk.Entry(app, font=("Arial", 12))
campo_numero3.pack(pady=5)

btn_enviar = tk.Button(app, text = "Concluído", command=calcular_numeros)
btn_enviar.pack(pady=15)

app.mainloop()