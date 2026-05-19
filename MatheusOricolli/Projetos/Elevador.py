from time import sleep

andar_atual = 0
quantidade_pessoas = 0

def subindo(andar_desejado, andar_agora):
    print(
        f"Elevador saindo do andar {andar_agora} e subindo até o andar {andar_desejado}!"
    )
    andares_andados = andar_desejado - andar_agora
    passando = andar_agora
    sleep(1)

    for i in range(andares_andados):
        passando += 1
        print(f"----- Andar {passando}")
        sleep(1)

    print(f"Você chegou ao andar {andar_desejado}")
    return andar_desejado  

def descendo(andar_desejado, andar_agora):
    print(
        f"Elevador saindo do andar {andar_agora} e descendo até o andar {andar_desejado}!"
    )
    andares_andados = andar_agora - andar_desejado
    passando = andar_agora
    sleep(1)

    for i in range(andares_andados):
        passando -= 1
        print(f"----- Andar {passando}")
        sleep(1)

    print(f"Você chegou ao andar {andar_desejado}")
    return andar_desejado  


def contando_pessoas(pessoas_atuais):
    saiu_pessoas = int(input("Insira a quantidade de pessoas que saíram: "))
    entrou_pessoas = int(input("Insira a quantidade de pessoas que entraram: "))

    if saiu_pessoas > 6:
        print(
            "Insira um valor válido, o elevador não pode conter mais de 5 pessoas!"
        )
        return pessoas_atuais

    elif entrou_pessoas < 0 or saiu_pessoas < 0:
        print(
            "Insira um valor válido, os números não podem ser negativos!"
        )
        return pessoas_atuais

    else:
        total = pessoas_atuais - saiu_pessoas + entrou_pessoas

        if total > 5:
            pessoas_a_mais = total - 5
            print(
                f"Capacidade máxima excedida, será necessária a saída de {pessoas_a_mais} pessoas."
            )

        return total  # Devolve o novo total de pessoas

print("Você Está Entrando no Elevador!")
quantidade_pessoas = int(input("Insira a quantidade de pessoas no elevador: "))

while True:
    if quantidade_pessoas > 5:
        print(
            "Elevador com capacidade máxima atingida, por favor espere até que alguém desça!"
        )
        while quantidade_pessoas > 5:
            quantidade_pessoas = int(
                input("Insira a quantidade de pessoas no elevador: ")
            )
    else:
        print("="*20)
        print(f"Elevador com {quantidade_pessoas} pessoas!")
        print(f"Andar atual: {andar_atual}")
        print("Painel de andares:")
        print(" ||T ||1 ||2 || \n ||3 ||4 ||5 || \n ||6 ||7 ||8 || \n ||- ||9 ||- || ")

        andar_desejado = input(
            "Insira o andar que deseja se mover ou digite 'sair': "
        )

        if andar_desejado.lower() == "sair":
            print("Você está encerrando o sistema!")
            break
        elif andar_desejado.lower() == "t":
            andar_desejado = 0
        else:
            andar_desejado = int(andar_desejado)
        if andar_desejado > 9 or andar_desejado < 0:
            print("Insira um andar válido de acordo com o painel!")
        elif andar_desejado > andar_atual:
    
            andar_atual = subindo(andar_desejado, andar_atual)
            quantidade_pessoas = contando_pessoas(quantidade_pessoas)
        elif andar_desejado < andar_atual:
            andar_atual = descendo(andar_desejado, andar_atual)
            quantidade_pessoas = contando_pessoas(quantidade_pessoas)

        else:
            print("Você já está no andar desejado!")