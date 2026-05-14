#Questão 1

# n1 = input("Digite o seu nome:")
# n2 = input("Digite o seu turno, se é A, B ou C:")
# print("Nome do Operador:", n1 )
# print("Turno do operador:", n2)

#--------------------------------------------------------------------------

#Questão 2 

# p1 = int(input("Quantas peças são produzidas em 1 hora:"))
# p2 = 8
# total = p1 * p2
# print("Em 8 horas vão ser produzidas:", total , "peças")

#---------------------------------------------------------------------------

#Questão 3 

# print("Sistema de PSI")
# i = int(input("Escolha a pressão do bar PSI \n"))
# psi = 14.5
# total = i * psi
# print("Valor da pressão:", total)


#----------------------------------------------------------------------------
 #Questão 4 

# print("Média de qualidade")

# n1 = int(input("Digite a primeira nota (0 a 10): \n"))
# n2 = int(input("Digite a segunda nota (0 a 10): \n"))
# n3 = int(input("Digite o terceiro número ( 0 a 10:) \n"))
# nota = (n1 + n2 + n3) / 3
# print("A média aritimética é igual a", nota)



#---------------------------------------------------------------------------

#Questão 5 

# temp = int(input("Qual a temperatura do motor?: \n" ))

# if temp <=40:
#     print("Baixa Carga!")
# elif temp <70: 
#     print("Normal")
# else:
#     print("Alerta! Temperatura alta! Resfriamento Ativado")

#--------------------------------------------------------------------------

#Questão 6 

# print("Classificador de lotes")
# l1 = input("Digite o código do produto: \n")

# if l1 =="A":
#     print("Alimentos")
# elif l1 =="E":
#     print("ELetrônicos")
# else:
#     print("Desconhecido")   

#--------------------------------------------------------------------------

#Questão 7 

# print("Segurança de Operação")

# sensor_porta = input("A porta está fechada ou aberta? \n")
# botao_emergencia = input("O botão de emergência está ligado ou desligado? \n")

# if sensor_porta == "fechada" or botao_emergencia == "desligado":
#     print("Máquina pode ligar")
# else:
#     print("Máquina não pode iniciar")

#-------------------------------------------------------------------------

#Questão 8

# print("Calculo de Descarte")

# pp = int(input("Digite o total de peças produzidas: \n"))
# pcd = int(input("Qual o total de peças defeituosas?: \n"))


# defeituosas = (pcd / pp) * 0.05 / 100

# if defeituosas >=5:
#     print("Revisar Processo")
# else:
#     print("Processo Otimizado")

#-----------------------------------------------------------------------

#Questão 9 

# print("Validação de Medida")

# p1 = float(input("Qual a medida da peça? \n"))

# if p1 < 9.8:
#     print("Abaixo da tolerância")
# elif p1 > 10.2: 
#     print("Acima da tolerância")
# elif 9.8 < p1 or 10.2 >=p1:
#     print("Tolerância está na Média")

# #--------------------------------------------------------------------------

# #Questão 10 

# for i in range(10, 0, -1):
#     print(i)
# print("Prensa Ativada!")

#--------------------------------------------------------------------------

#Questão 11

# print("Soma de produção (Acumulador)")

# total = 0 

# while True:
#     peso = float(input("Digite o peso da caixa (ou 0 para sair): "))

#     if peso == 0:
#         break

#     total += peso

# print(f"Total da acumulação: {total}")

#----------------------------------------------------------------

#Questão 12

# print("Multiplas leituras")

# maior = 0 

# for i in range (0,5):
#     temp = float(input(f"Temperatura {i+1}: "))

# if i == 0 or temp > maior: maior = temp
# print(f"A maior temperatura é: {maior}.")

#------------------------------------------------------------------

#Questão 13

# print("Painel de login")

# senha = "admin123"

# while True <3:
#     senha = input("Digite a sua senha: \n")

#     if senha == "admin123":
#         break
#     print(f"Sua senha está correta!")

#     if senha != "admin123":
#         print(f"Acesso Negado!")
        
        
#         break
# else: 
#     print(F"Acesso negado")

