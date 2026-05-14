# Exercicio 1
#Criar um algorotimo para calculara a média e com base em notas, podemos inserir duas notas e apresenta a média porém a nota base de 50 é aprovado menor que esse valor será reprovado

n1 = int(input("Digite a primeira nota: \n"))
n2 = int(input("Digite a segunda nota: \n"))
media = (n1 + n2) / 2 
if media >= 50:
    print("Aprovado")
elif media <= 50:
    print("Reprovado")

