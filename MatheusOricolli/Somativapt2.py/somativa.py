#Exercício 1 - Crie uma aplicação que faça o calculo da idade de pessoas
#Deve perguntar o nome da pessoa e o ano de nascimento 

# import tkinter as tk
# from tkinter import messagebox

# def registrar_operador():
#     nome_operador = ent_nome.get()
#     turno_operador = ent_turno.get()
#     messagebox.showinfo("Resultado", f"Operador {nome_operador} registrado no Turno {turno_operador}. Boa jornada!")

# janela = tk.Tk()
# janela.title("Registro de Operador")
# janela.geometry("400x500")
# janela.configure(bg="#C8A2C8")

# lbl_nome = tk.Label(janela, text="Digite o nome do operador:", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_nome.grid(row=10, column=0, pady=0, padx=80)
# lbl_turno = tk.Label(janela, text="Digite o turno (A, B ou C):", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_turno.grid(row=13, column=0, pady=0, padx=80)

# ent_nome = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_nome.grid(row=11, column=0, pady=10, padx=35)
# ent_turno = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_turno.grid(row=14, column=0, pady=10, padx=35)

# btn_registrar = tk.Button(janela, text="Registrar", font=("Arial", 14), fg="white", bg="#C8A2C8", command=registrar_operador)
# btn_registrar.grid(row=15, column=0, pady=20, padx=35)

# janela.mainloop()
 
#------------------------------------------------------------------------------------------------------------------------------------------

# Exercicio 2 - Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox

# def calcular_producao():
#     try:
#         pecas_hora = int(ent_pecas.get())
#         producao_total = pecas_hora * 8
        
#         messagebox.showinfo("Resultado", f"Em um turno de 8 horas, serão produzidas {producao_total} peças.")
#     except ValueError:
#         messagebox.showerror("Erro", "Digite um valor correto.")

# janela = tk.Tk()
# janela.title("Cálculo de Produção")
# janela.geometry("400x500")
# janela.configure(bg="#C8A2C8")

# lbl_pecas = tk.Label(janela, text="Peças produzidas em 1 hora:", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_pecas.grid(row=10, column=0, pady=0, padx=80)

# ent_pecas = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_pecas.grid(row=11, column=0, pady=10, padx=35)

# btn_calcular = tk.Button(janela, text="Calcular", font=("Arial", 14), fg="white", bg="#C8A2C8", command=calcular_producao)
# btn_calcular.grid(row=15, column=0, pady=20, padx=35)

# janela.mainloop()

#---------------------------------------------------------------------------------------------------------
# Exercicio 3 - Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
#≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# def converter_pressao():
#     try:
#         pressao_bar = float(ent_bar.get())
#         pressao_psi = pressao_bar * 14.5
        
#         messagebox.showinfo("Resultado", f"A pressão é de {pressao_psi} PSI")
#     except ValueError:
#         messagebox.showerror("Erro", "Digite um valor correto.")

# janela = tk.Tk()
# janela.title("Conversor Bar para PSI")
# janela.geometry("400x500")
# janela.configure(bg="#C8A2C8")

# lbl_bar = tk.Label(janela, text="Digite a pressão em Bar:", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_bar.grid(row=10, column=0, pady=0, padx=80)

# ent_bar = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_bar.grid(row=11, column=0, pady=10, padx=35)

# btn_converter = tk.Button(janela, text="Converter", font=("Arial", 14), fg="white", bg="#C8A2C8", command=converter_pressao)
# btn_converter.grid(row=15, column=0, pady=20, padx=35)

# janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------
# Exercício 4 Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
#aritmética simples delas.


# import tkinter as tk
# from tkinter import messagebox

# def calcular_media():
#     try:
#         nota1 = float(ent_nota1.get())
#         nota2 = float(ent_nota2.get())
#         nota3 = float(ent_nota3.get())
        
#         media = (nota1 + nota2 + nota3) / 3
        
#         messagebox.showinfo("Resultado", f"A média de qualidade da peça é: {media}")
#     except ValueError:
#         messagebox.showerror("Erro", "Digite valores corretos.")

# janela = tk.Tk()
# janela.title("Média de Qualidade")
# janela.geometry("400x500")
# janela.configure(bg="#C8A2C8")

# lbl_nota1 = tk.Label(janela, text="Digite a primeira nota:", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_nota1.grid(row=10, column=0, pady=0, padx=80)
# lbl_nota2 = tk.Label(janela, text="Digite a segunda nota:", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_nota2.grid(row=12, column=0, pady=0, padx=80) 
# lbl_nota3 = tk.Label(janela, text="Digite a terceira nota:", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_nota3.grid(row=14, column=0, pady=0, padx=80)

# ent_nota1 = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_nota1.grid(row=11, column=0, pady=5, padx=35)
# ent_nota2 = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_nota2.grid(row=13, column=0, pady=5, padx=35)
# ent_nota3 = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_nota3.grid(row=15, column=0, pady=5, padx=35)

# btn_calcular = tk.Button(janela, text="Calcular Média", font=("Arial", 14), fg="white", bg="#C8A2C8", command=calcular_media)
# btn_calcular.grid(row=16, column=0, pady=20, padx=35)

# janela.mainloop()

#--------------------------------------------------------------------------------------------------------------
# Exercicio 5 - Termostato Inteligente: Peça a temperatura de um motor.
#● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# 0
# import tkinter as tk
# from tkinter import messagebox

# def verificar_temperatura():
#     try:
#         temperatura = float(ent_temp.get())

#         if temperatura < 40:
#             messagebox.showinfo("Status", "Baixa carga")
#         else:
#             if temperatura <= 70:
#                 messagebox.showinfo("Status", "Normal")
#             else:
#                 messagebox.showwarning("ALERTA", "ALERTA: Resfriamento Ativado!")
                
#     except ValueError:
#         messagebox.showerror("Erro", "Digite um valor correto.")

# janela = tk.Tk()
# janela.title("Termostato Inteligente")
# janela.geometry("400x500")
# janela.configure(bg="#C8A2C8")

# lbl_temp = tk.Label(janela, text="Digite a temperatura do motor (°C):", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_temp.grid(row=10, column=0, pady=0, padx=80)


# ent_temp = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_temp.grid(row=11, column=0, pady=10, padx=35)

# btn_verificar = tk.Button(janela, text="Verificar", font=("Arial", 14), fg="white", bg="#C8A2C8", command=verificar_temperatura)
# btn_verificar.grid(row=15, column=0, pady=20, padx=35)

# janela.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------

#Exercicio 6 - Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
#exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# import tkinter as tk
# from tkinter import messagebox

# def classificar_lote():
#     codigo = ent_codigo.get().upper()
#     if codigo == "A":
#         messagebox.showinfo("Resultado", "Alimentos")
#     else:
#         if codigo == "E":
#             messagebox.showinfo("Resultado", "Eletrônicos")
#         else:
#             messagebox.showinfo("Resultado", "Desconhecido")

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("400x500")
# janela.configure(bg="#C8A2C8")

# lbl_codigo = tk.Label(janela, text="Digite a letra do produto:", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_codigo.grid(row=10, column=0, pady=0, padx=80)

# ent_codigo = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_codigo.grid(row=11, column=0, pady=10, padx=35)

# btn_classificar = tk.Button(janela, text="Classificar", font=("Arial", 14), fg="white", bg="#C8A2C8", command=classificar_lote)
# btn_classificar.grid(row=15, column=0, pady=20, padx=35)

# janela.mainloop()

#-----------------------------------------------------------------------------------------------
#Exercicio 7 - Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# import tkinter as tk
# from tkinter import messagebox

# def verificar_maquina():
#     sensor_porta = ent_porta.get().lower()
#     botao_emergencia = ent_emergencia.get().lower()

#     if sensor_porta == "fechada":
#         if botao_emergencia == "desligado":
#             messagebox.showinfo("Status", "A máquina pode iniciar.")
#         else:
#             messagebox.showwarning("Aviso", "A máquina não pode iniciar.")
#     else:
#         messagebox.showwarning("Aviso", "A máquina não pode iniciar.")

# janela = tk.Tk()
# janela.title("Segurança de Operação")
# janela.geometry("400x500")
# janela.configure(bg="#C8A2C8")

# lbl_porta = tk.Label(janela, text="Sensor da Porta (fechada/aberta):", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_porta.grid(row=10, column=0, pady=0, padx=40)
# lbl_emergencia = tk.Label(janela, text="Botão Emergência (ligado/desligado):", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_emergencia.grid(row=12, column=0, pady=0, padx=40)

# ent_porta = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_porta.grid(row=11, column=0, pady=10, padx=35)
# ent_emergencia = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_emergencia.grid(row=13, column=0, pady=10, padx=35)

# btn_verificar = tk.Button(janela, text="Verificar", font=("Arial", 14), fg="white", bg="#C8A2C8", command=verificar_maquina)
# btn_verificar.grid(row=15, column=0, pady=20, padx=35)

# janela.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------
# Exercicio 8 - Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# import tkinter as tk
# from tkinter import messagebox

# def calcular_descarte():
#     try:
#         total = int(ent_total.get())
#         defeituosas = int(ent_defesas.get())
        
#         limite = total * 0.05
      
#         if defeituosas > limite:
#             messagebox.showwarning("Resultado", "Revisar Processo")
#         else:
#             messagebox.showinfo("Resultado", "Processo Otimizado")
            
#     except ValueError:
#         messagebox.showerror("Erro", "Digite valores corretos.")

# janela = tk.Tk()
# janela.title("Cálculo de Descarte")
# janela.geometry("400x500")
# janela.configure(bg="#C8A2C8")

# lbl_total = tk.Label(janela, text="Total de peças produzidas:", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_total.grid(row=10, column=0, pady=0, padx=80)
# lbl_defesas = tk.Label(janela, text="Total de peças defeituosas:", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_defesas.grid(row=12, column=0, pady=0, padx=80)

# ent_total = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_total.grid(row=11, column=0, pady=10, padx=35)
# ent_defesas = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_defesas.grid(row=13, column=0, pady=10, padx=35)

# btn_calcular = tk.Button(janela, text="Calcular", font=("Arial", 14), fg="white", bg="#C8A2C8", command=calcular_descarte)
# btn_calcular.grid(row=15, column=0, pady=20, padx=35)

# janela.mainloop()

#---------------------------------------------------------------------------------------------------
# Exercicio 9 - Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
#diga se está dentro da tolerância, acima ou abaixo.

# import tkinter as tk
# from tkinter import messagebox

# def validar_medida():
#     try:
#         medida = float(ent_medida.get())
        
#         if medida < 9.8:
#             messagebox.showwarning("Resultado", "Abaixo da tolerância")
#         else:
#             if medida > 10.2:
#                 messagebox.showwarning("Resultado", "Acima da tolerância")
#             else:
#                 messagebox.showinfo("Resultado", "Dentro da tolerância")
                
#     except ValueError:
#         messagebox.showerror("Erro", "Digite um valor correto.")


# janela = tk.Tk()
# janela.title("Validação de Medida")
# janela.geometry("400x500")
# janela.configure(bg="#C8A2C8")

# lbl_medida = tk.Label(janela, text="Digite a medida da peça (mm):", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_medida.grid(row=10, column=0, pady=0, padx=80)

# ent_medida = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_medida.grid(row=11, column=0, pady=10, padx=35)

# btn_validar = tk.Button(janela, text="Validar", font=("Arial", 14), fg="white", bg="#C8A2C8", command=validar_medida)
# btn_validar.grid(row=15, column=0, pady=20, padx=35)

# janela.mainloop()

#-------------------------------------------------------------------------------------------------------------
# Exercicio 10Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
#de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

# import tkinter as tk
# from tkinter import messagebox

# def iniciar_prensa():
#     for i in range(10, 0, -1):
#         print(i) 
        
#     messagebox.showinfo("Status", "Prensa Ativada!")

# janela = tk.Tk()
# janela.title("Contagem de Setup")
# janela.geometry("400x500")
# janela.configure(bg="#C8A2C8")

# lbl_aviso = tk.Label(janela, text="Clique para iniciar o setup da prensa:", font=("Arial", 14), fg="white", bg="#C8A2C8")
# lbl_aviso.grid(row=10, column=0, pady=40, padx=40)

# btn_iniciar = tk.Button(janela, text="Iniciar Prensa", font=("Arial", 14), fg="white", bg="#C8A2C8", command=iniciar_prensa)
# btn_iniciar.grid(row=15, column=0, pady=20, padx=35)


# janela.mainloop()

#--------------------------------------------------------------------------------------------
#Exercicio 11 - Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
#O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.
 
#----------------------------------------------------------------------------------------------------------------------------------------------
# Exercicio 12.Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes.
# Ao final, mostre qual foi a maior temperatura lida.

#----------------------------------------------------------------------------------------------------------------------------------------------
# Exercicio 13.Painel de Login: Crie um while que peça a senha do supervisor ("admin123").
# Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas.
# Se esgotar, exiba "Painel Bloqueado".

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Exercicio 14.Simulador de Estoque: Comece com estoque = 100. Crie um menu (while) onde o
# usuário pode: (1) Adicionar itens, (2) Remover itens ou (3) Sair. Se o estoque ficar
# abaixo de 10, avise: "Estoque Crítico!".

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Exercicio 15.Relatório de Turno Completo: Use um for para processar 5 peças. Para cada peça,
# peça o diâmetro. Se a peça for aprovada (entre 19.9 e 20.1), conte-a. No final do
# loop, exiba o total de peças aprovadas e a porcentagem de eficiência do lote.'     ef9oqufhrjryjry]


wgwihnjeriughe
perguntar
print      