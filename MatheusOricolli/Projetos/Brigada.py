print("Olá! Seja bem vindo ao sistema de controle da SESMT (Serviço Especializado em Engenharia de Segurança e em Medicina do Trabalho)")
print("Informe seus dados abaixo: \n")

total_cadastrados = 0
total_em_dia = 0

def verificar_epi(setor_escolhido):
    print(f"Setor: {setor_escolhido}")
    if setor_escolhido == "Elétrica":
        print("EPIs: Luvas de alta tensão e botas dielétricas.")
    elif setor_escolhido == "Trabalho em Altura":
        print("EPIs: Cinturão de segurança e talabarte.")
    else:
        print("EPIs: Consultar setor de segurança.")

def alerta_reciclagem(ano_treino):
    ano_atual = 2026
    if (ano_atual - ano_treino) > 2:
        print("MENSAGEM: Treinamento Vencido! Encaminhar para reciclagem.")
        return "Vencido"
    else:
        print("MENSAGEM: Treinamento Válido.")
        return "OK"

while True:
    nome = input("\nDigite o nome do funcionário: ")
    setor = input("Digite o setor (Elétrica / Trabalho em Altura): ")
    nr10 = input("Status NR-10 (OK/Pendente): ")
    nr35 = input("Status NR-35 (OK/Pendente): ")
    ano_brigada = int(input("Ano do último treinamento da Brigada: "))

    total_cadastrados = total_cadastrados + 1

    print("\n--- RESULTADOS ---")
    verificar_epi(setor)
    status_brigada = alerta_reciclagem(ano_brigada)

    if nr10 == "OK" and nr35 == "OK" and status_brigada == "OK":
        total_em_dia = total_em_dia + 1
    continuar = input("\nDeseja realizar mais um cadastro? (Sim/Não): ").strip().lower()
    
    if continuar not in ["sim", "s"]:
        break

print("\n" + "="*60)
print(f"{'RELATÓRIO GERAL':^60}")
print(f"{'-'*25:^60}")
print(f"Total de funcionários cadastrados: {total_cadastrados:>6}")
print(f"Funcionários com treinamentos em dia: {total_em_dia:>3}")
print("="*60)

