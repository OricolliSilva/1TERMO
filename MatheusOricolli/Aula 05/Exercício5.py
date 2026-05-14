#Exercício 4
#Criar um menu de opções com 4 itens, ex: Escolher Séries, apresente sua escola de séries das outras três.
#Qualquer opção diferente sair do menu
opcao = input("Digite a opcao")

while opcao != "Terror" or "Drama" or "Romance" or "sair":
    if opcao == "Terror":
        print("Você escolheu Terror  ").lower()

    else: 
        print(f"Série '{opcao}' registrada no banco de dados. ")
print("Sistema encerrado.")
