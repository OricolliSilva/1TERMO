#Exercício 1:
#Escreva um programa que solicite ao usuário um número inteiro e calcule a media
# de uma lista de números. O programa deve tratar os seguints erros:
# - ValueError: se o usuario digitar um valor que não seja um número inteiro.

# try:

#     n1 = int(input("Digite o seu primeiro número: \n"))
#     n2 = int(input("Digite o seu segundo número: \n"))
#     n3 = int(input("Digite o seu terceiro número: \n"))
#     resultado = (n1 + n2 + n3) / 3
#     print(f"O resultado da média é: {resultado:.2f}")

# except ValueError:
#     print("Erro! O número digitado não é inteiro. \n")


# Exercício 1:
# Escreva um programa que solicite ao usuário um número inteiro e calcule a média
# de uma lista de números. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um número inteiro.

# soma = 0
# quantidade = 6

# try:
#     for i in range(quantidade):
#         entrada = input(f"Digite o {i+1}º número inteiro: ")

#         numero = int(entrada)
#         soma += numero

#     resultado = soma / quantidade
#     print(f"O resultado da média dos {quantidade} números é: {resultado:.2f}")

# except ValueError:
#     print("Erro! O valor digitado não é um número inteiro.")

#Exercício 2
# Escreva um programa que solicite ao usuario uma lista de palavras e 
# conte quantas vezes cada palavra aparece na lista . O programa deve tratar os seguintes erros:
# - ValueError: Se o usuário digitar um valor que não seja uma string. 


try:
    entrada_qtd = input("Quantas palavras deseja digitar? ")
    quantidade = int(entrada_qtd)
    contagem = {} 
    for i in range(quantidade):
        palavra = str(input(f"Digite a {i+1}ª palavra: "))
       
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    print("\nContagem das palavras:")
    for chave in contagem:
        print(f"{chave}: {contagem[chave]}")

except ValueError:
    print("Erro: Você não digitou um número válido para a quantidade.")

#-----------------------------------------------------------------------------------------------------------

# try:
#     palavras = input("Digite uma lista de palavras separadas por espaço: \n").split()
#     contagem = {}
#     for palavra in palavras:
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1
#             print("Contagem de palavras:")
#             for palavra, contagem in contagem.items():
#                 print(f"{palavra}: {contagem}")
# except ValueError:
#     print("Erro: Entrada inválida. Por Favor, digite uma lista de palavras separadas por espaço.")

#-----------------------------------------------------------------------------------------------------------------------

#Exercício 3
#Escrever um programa mais simples com testes de ratamentos de erros
#Como por exemplo, solicitar ao usuario um número. O programa deve tratar os seguintes erros:
# - ValueError : Se o usuario digitar um valor que não seja um número.
# - ZeroDivisionError: Se o usuário digitar 0 como divisor

