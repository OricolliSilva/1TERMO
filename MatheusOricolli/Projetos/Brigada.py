print("Olá! Seja bem vindo ao sistema de controle da SESMT (Serviço Especializado em Engenharia de Segurança e em Medicina do Trabalho) ")
print("Informe seus dados abaixo: \n")

total_cadastrados = 0
total_em_dia = 0

nome = input("Digite o nome do funcionário: ")
setor = input("Digite o setor (Elétrica / Trabalho em Altura): ")
nr10 = input("Status NR-10 (OK/Pendente): ")
nr35 = input("Status NR-35 (OK/Pendente): ")
ano_brigada = int(input("Ano do último treinamento da Brigada: "))

def verificar_epi(setor_escolhido):
    print(f"Setor: {setor_escolhido}")
    if setor_escolhido == "Elétrica":
        print("EPIs: Luvas de alta tensão e botas dielétricas.")
    elif setor_escolhido == "Trabalho em Altura":
        print("EPIs: Cinturão de segurança e talabarte.")
    else:
        print("EPIs: Consultar setor de segurança.")

# Função para o Requisito 3: Alerta de Reciclagem
def alerta_reciclagem(ano_treino):
    ano_atual = 2026
    if (ano_atual - ano_treino) > 2:
        print("MENSAGEM: Treinamento Vencido! Encaminhar para reciclagem.")
        return "Vencido"
    else:
        print("MENSAGEM: Treinamento Válido.")
        return "OK"

total_cadastrados = total_cadastrados + 1

print("\n--- RESULTADOS ---")
verificar_epi(setor)
status_brigada = alerta_reciclagem(ano_brigada)

if nr10 == "OK" and nr35 == "OK" and status_brigada == "OK":
    total_em_dia = total_em_dia + 1

print("\n" + "="*30)
print("RELATÓRIO GERAL")
print(f"Total de funcionários cadastrados: {total_cadastrados}")
print(f"Funcionários com treinamentos em dia: {total_em_dia}")
print("="*30)