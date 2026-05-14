#Projeto Cancela Automática
#Criar um algoritimo que consiga gerenciar entrada e saida
#de veículos, inserindo valores por hora permanecida
#A forma de entrada e saída deve ser espeificada e permitir
#o usuário inserir os dados necessários para registro do veículo.
#Passos

#1 - Pressionar botão, imprimiu um ticket
#Calcular tempo de permanência 
#Pagar o ticket 
#Devolver o ticket na saída
#Liberar e fechar cancela

#2 - Acesso por TAGs (Sem parar, Connect Car...)
#Calcular tempo de permanencia 
#Gerar pagamento  em fatura
#Liberar e fechar cancela

#3 - Erros
#Verificar sinal de transmissão da TAG
#Verificar acesso por ticket ou tag ao mesmo tempo
#Perdeu ticket
#Problemas com cancela

#-----------------------------------------------------------------------------------------------------------------
#Parte 1
print("Voz da máquina: Bem vindo ao estacionamento do shopping Limeira.")
print("Voz da máquina: Aqui nós damos o preço do seu ticket de acordo com p seu tempo de permanência.")
print("Voz da máquina: Preço do ticket por hora: R$10.00.")
TI = "Ticket"
TA = "TAG"
E1 = str(input("Digite a maneira escolhida para pagar, Ticket ou TAG: \n"))
if E1 == TI:
    print("\n" + "-"*40)
    print("Perfeito! Sua forma de pagamento escolhida foi o ticket!")
    hora1 = float(input("Digite o seu horário de entrada (EX: 14): \n"))
    print("Aperte o botão para imprimir o seu ticket.")
    print("Retire o seu ticket da máquina e espere a cancela abrir.")
    print("-"*40)
    print("Você está saindo shopping! Insira o ticket para pagar.")
    hora2 = float(input("Digite o seu horário de saída: \n"))
    horap = hora2 - hora1
    valorp = horap * 10
    while True:
        perda = str(input("Ocorreu uma perda de ticket? (Sim ou Não):"))
        if perda == "Não":
            print("Inserir o ticket na máquina...")
            print("-"*40)
            print(f"{'NOTA FICAL DE ESTACIONAMENTO':^40}")
            print("-"*40)
            print(f"Horário de Entrada:     {hora1:>9}h")
            print(f"Horário de saída:       {hora2:>9}h")
            print(f"Tempo de permanência:   {horap:>9}h")
            print("-"*40)
            print(f"VALOR TOTAL:             R${valorp:>9.2f}")
            print("-"*40)
            print(f"{'Obrigado pela preferência!':^40}")
            print("-" * 40)
            break
        elif perda == "Sim":
            print("Parece que você perdeu o seu ticket! Insira as informações a seguir: \n")
            nc = str(input("Nome completo: "))
            cpf = int(input("Seu CPF (Sem traços, pontos ou espaços): "))
            placa = str(input("Informe a placa do seu carro: "))
            print(f"{'NOTA FICAL DE ESTACIONAMENTO':^40}")
            print("-"*40)
            print(f"Horário de Entrada:     {hora1:>9}h")
            print(f"Horário de saída:       {hora2:>9}h")
            print(f"Tempo de permanência:   {horap:>9}h")
            print("-"*40)
            print(f"Nome completo:      {nc:>10}")
            print(f"Número do CPF:      {cpf:>10}")
            print(f"Número da placa:    {placa:>10}")
            print("-"*40)
            print(f"VALOR TOTAL:             R${valorp:>9.2f}")
            print("-"*40)
            print(f"{'Obrigado pela preferência!':^40}")
            print("-" * 40)
            print("Ok! O preço total a pagar será:", valorp * 10)
            print("Obrigado, o pagamento foi concluído! Volte sempre!!")
            break

elif E1 == TA:
    print("Perfeito! Sua forma de pagamento escolhida foi a TAG!")
    HE = float(input("Digite a sua hora de entrada. EX: 14: \n"))
    print("Obrigado! Espere a cancela abrir para passar!")
    print("Você está saindo do shopping! A seguir, informe o seu horário de saída.")
    HS = float(input("Digite seu horário de saída EX: 15: \n"))
    HT = HS - HE
    VT = HT * 10
    print("\n" + "-"*40)
    print(f"{'NOTA FISCAL DE ESTACIONAMENTO':^40}")
    print("-"*40)
    print(f"Horário de Entrada:      {HE:>6}h")
    print(f"Horário de Saída:        {HS:>6}h")
    print(f"Tempo de Permanência:    {HT:>6}h")
    print("-"*40)
    print(f"VALOR TOTAL:             R${VT:>7.2f}")
    print("-"*40)
    print(f"{'Obrigado pela preferência!':^40}")
    print("-" * 40)
else:
    print("ERRO! Você deve escolher alguma das formas de pagamento!")