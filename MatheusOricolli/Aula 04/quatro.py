#Conteúdo sobre lógica
#Exemplo 1
print("Expressões lógicas")
idade = int(input("Digite sua idade: \n"))

if idade >= 18:
    print("Você é maior de idade")
    print("Você pode tirar carta de motorista")
elif idade >= 16:
    print("Você ainda não é maior de idade, mas já pode votar")
else:
    print("Você é menor de idade")

#if: "Se" a acondição for verdadeira
# elif: "Senão, se" ( usado para multiplas condições)
#else: "Senão" (executa se nenhuma das ateriores for verdadeira) 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Exemplo 2
print("Escolha sua modalidade?")
print("Opção 1: T.I")
print("Opção 2: Humanas")
print("Opção 1: Exatas ")
modalidade = int(input("Digite sua Opção de modalidade por números: \n"))
if modalidade == 1:
    print("Você escolheu T.I")
elif modalidade == 2:
    print("Você escolheu Humanas")
else:
    print("Você escolheu Exatas")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Exemplo 3
print("Categoria de Series e Filmes")
print("Escolha uma Categoria")
print("Séries = S")
print("Filmes = F")
categoria = input("Digite sua categoria: \n")
if categoria == "S": 
    print("Sua escolha foi para Séries")
elif categoria == "F": 
    print("Sua escolha foi para Filmes")
else:
    print("Você não escolheu nenhuma das categorias")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Exemplo 4
print("Calculadora com condições")
print("Escolha como quer calcular")
print("1 = Soma")
print("2 = Subtração")
print("3 = Multiplicação")
print("4 = Divisão")
calculadora = float(input("Digite sua opção para calcular: \n"))
if calculadora == 1:
    print("1 = Você Escolheu soma")
    soma1 = int(input("Digite o primeiro valor \n"))
    soma2 = int(input("Digite o segundo valor: \n"))
    print("O resultado da soma foi: \n", soma1 + soma2)
elif calculadora == 2:
    print("2 = Você escolheu subtração")
    subtração1 = int(input("Digite o primeiro valor: \n"))
    subtração2 = int(input("Digite o segundo valor: \n"))
    print("O resultado da subtração foi: \n", subtração1 - subtração2)
elif calculadora == 3: 
    print("3 = Você escolheu multiplicação")
    multiplicação1 = int(input("Digite o primeiro valor: \n"))
    multiplicação2 = int(input("Digite o segundo valor: \n"))
    print("O resultado da multiplicação foi: \n", multiplicação1 * multiplicação2)
elif calculadora == 4: 
    print("4 = Você escolheu divisão")
    divisão1 = int(input("Digite o primeiro valor: \n"))
    divisão2 = int(input("Digite o segundo valor: \n"))
    print("O resultado da divisão foi: \n ", divisão1 / divisão2)
else:
    print("Você não escolheu nenhuma opção")
    print("Sair do programa")