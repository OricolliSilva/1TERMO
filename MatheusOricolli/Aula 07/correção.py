#Correção da Atividade Somativa

#Questão 1 
print("Registro de operador")
operador = input("Digite seu nome ...")
turno = input("Digite seu turno ...")
print(f"Operador {operador} registrado no Turno {turno}. Boa jornada!")

#--------------------------------------------------------------------------------------------------------------------------

#Questão 2
print("Calculo de Produção")
producao_hora = int(input("Digite a quantidade de peças produzidas em 1 hora ..."))
producao_turno = producao_hora * 8 
print(f"Quantidade de peças produzidas em um turno de 8 horas:{producao_turno}")

#---------------------------------------------------------------------------------------------------------------------------

#Questão 3 
print("Conversor de Unidade")
pressao_bar = int(input("Digite a pressao em Bar ..."))
pressao_psi = pressao_bar * 14.5
print(f"Pressão em PSI: {pressao_psi:.2f}")
print(f"Pressão em PSI: {pressao_psi}" ,round(pressao_psi, 2))

#----------------------------------------------------------------------------------------------------------------------------

#Questão 4 
print("Inspeção de Peças")
nota1 = float(input("Digite a nota da inpeção 1 ( 0 a 10 ) ... "))
nota2 = float(input("Digite a nota da inspeção 2 ( 0 a 10 ) ..."))
nota3 = float(input("Digite a nota da inpeção 3 ( 0 a 10 ) ..."))
media = (nota1 + nota2 + nota3) / 3
print(f"Média de qualidade da peça: {media:.2f}")
print("Média de qualidade da peça: ", round(media,2))

#---------------------------------------------------------------------------------------------------------------------------

#Questão 5 
print("Termostato Inteligente")
temperatura = float(input("Digite a temperatura do motor em °C ..."))
if temperatura <40:
    print("Baixa carga")
elif 40 <= temperatura <=70:
    print("Normal")
else:
    print("ALERTA: Resfriamento Ativado!")

print("Termostato Inteligente - Versão 2")
temperatura = float(input("Digite a temperatura em °C ..."))
if temperatura <40:
    print("Baixa carga")
elif temperatura >70:
    print("ALERTA!: Resfriamento Ativado!")
else:
    print("Normal")

#---------------------------------------------------------------------------------------------------------------------------

#Questão 6 
print("Classificador de Lotes")
codigo_produto = input("Digite o Código do produto ...")
if codigo_produto == "A":
    print("Alimento")
if codigo_produto == "E":
    print("Eletronico")
else:
    print("desconhecido")

#Versão 2
codigo_produto = input("Digite o código do produto ...")
if codigo_produto.startswith("A"):
    print("Alimentos")
elif codigo_produto.startswith("E"):
    print("Eletronico")
else:
    print("Desconhecido")

#--------------------------------------------------------------------------------------------------------------------------

#Questão 7
print("Segurança de Operação")
sensor_porta = input("Digite o status do sensor da porta (fechada/aberta) ...")
botao_emergencia = input("Digite o statos do botão de emergência (ligado/desligado) ...")
if sensor_porta == "fechada" and botao_emergencia == "desligado":
    print("A máquina pode iniciar.")
else:
    print("A máquina não pode iniciar.")

#---------------------------------------------------------------------------------------------------------------------------

#Questão 8
print("Calculo de Descarte")
total_pecas = int(input("Digite o total de peças produzidas ..."))
total_defeituosas = int(input("Digite o total de peças defeituosas ..."))
descarte_percentual = (total_defeituosas / total_pecas) * 100
if descarte_percentual >5:
    print("Revisar Processo")
else:
    print("Processo Otimizado")
print(f"Descarte percentual: {descarte_percentual:.2f}%")

#-------------------------------------------------------------------------------------------------------------------------

#Questão 9 
print("Validação da Média")
media =float(input("Digite a medida da peça em mm ..."))
if media < 9.8:
    print("A peça está abaixo da tolerância.")
elif media > 10.2:
    print("A peça está acima da tolerância.")
else:
    print("A peça está dentro da tolerância")

#-------------------------------------------------------------------------------------------------------------------------

#Questão 10
print("Contagem Regressiva de Setup")
for contagem in range(10, 0, -1):
    print(contagem)
print("Prensa Ativada!")

#-------------------------------------------------------------------------------------------------------------------------

#  #Questão 11
# print("Soma de Produção (Acumulador)")
# peso_total = 0 
# while True:
#     peso_caixa = float(input("Digite o peso da caixa (0 para parar)"))
#     if peso_caixa == 0:
#         peso_total += peso_caixa 
#     print(f"Peso total acumulado: {peso_total:.2f} kg ")

#--------------------------------------------------------------------------------------------------------------------------

#Questão 12
print("Multiplas leituras")
temperaturas =  []
for i in range(1, 6):
        temp = float(input(f"Digite a temperatura do sensor {i} em °C ..."))
        temperaturas.append(temp)

print(f"Maior temperatura lida: {max(temperaturas):.2f} °C")
print(f"Menor tempeatura lida : {min(temperatura):.2f} °C")
print(F"Soma temperatura lida: {sum(temperatura):.2f} °C")

#------------------------------------------------------------------------------------------------------------------------

#Questão 13
print("Painel de Login")
senha_correta = "admin123"
tentativas = 3
while tentativas > 0:
    senha = input("Digite a Senha do Supervisor ...")
    if senha == senha_correta:
        print("Acesso Permitido")
        break
else:
    tentativas -= 1
    print(f"Acesso Negado. Tentativas restantes: {tentativas}")
if tentativas == 0:
    print("Painel Bloqueado")

#------------------------------------------------------------------------------------------------------------------------

#Questão 14 
print("Simulador de estoque")
estoque = 100
while True:
    print("\nMenu: ")
    print("1. Adicionar itens")
    print("2. Remover itens")
    print("3, Sair")
    escolha = input("Escolha uma opção (1, 2 ou 3) ...")

    if escolha == 1:
        quantidade = int(input("Digite a quantidade de itens a adicionar ..."))
        estoque += quantidade 
        print(f"Estoque atualizado: {estoque} itens")
    elif escolha == "2":
        quantidade = int(input("Digite a quantidade de itens a remover ..."))
        estoque -= quantidade
        print(f"Estoque atualizado: {estoque} itens")
        if estoque <10:
            print("Estoque Crítico!")
    elif escolha == "3":
        print("Saindo do simulador de estoque.")
        break
    else:
        print("Opção inválida. Tente novamente.")

#------------------------------------------------------------------------------------------------------------------------

#Questões 15
print("Relatório de Turno Completo")
total_pecas = 5 
pecas_aprovadas = 0
for i in range(1, total_pecas, + 1):
    diametro = float(input(f"Digite o diâmetro da peça {i} em mm ..."))
    if 19.9 <= diametro <= 20.1:
        pecas_aprovadas += 1
eficiencias = (pecas_aprovadas / total_pecas) *100
print(f"Total de peças aprovadas: {pecas_aprovadas}")
print(f"Eficiencia do lote: {eficiencias:.2f}%")