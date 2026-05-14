#Exercício 6 
print("Este é o meu nome inteiro:")
nome = input("Digite seu nome: \n")
sobrenome = input("Digite seu sobrenome: \n")
print("Meu nome é", nome + sobrenome)

#Exercício 7 
print("Separação de peças")
total = int(input("Digite o total de peças boas e defeituosas: \n"))
boas = int(input("Digite a quantidade de peças boas: \n"))
ruins = int(input("Digite a quantidade de peças defeituosas: \n"))
print("Esse é o total de taxa de aproveitamento: \n", boas / total)

#Exercício 8 
idade1 = int(input("Digite sua idade: \n"))
ano = int(input("Quer saber sua idade daqui a quantos anos? \n"))
idade2 = (idade1 + ano)
print("Eu tenho ", idade1 + "e, em" + ano +  " anos eu terei" + idade2 + "anos")

#Exercício 9 
hotel = 250.50
passagem = 421.00
print("O valor total da viagem é:", (hotel *3) + passagem)

#Exercício 10
print("Relatório de vendas: \n")
p = str(input("Digite qual o produto: \n"))
q = int(input( "Digite a quantidade de vendas do produto: \n" ))
v = int(input( "Digite o valor únitario: \n"))
print("Esse foi o preço do total de vendas: \n", q * v)

