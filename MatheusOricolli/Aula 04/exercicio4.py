#Exercicio 4 
#Criar um algorotimo para calcular a média e com base em notas, podemos inserir duas notas e apresente a média,porém a nota vale de 0 a 100, para ser aprovado, será acima de 70.
#E menor que 50 esse valor será reprovado porém vamos acrescentar uma nova condição que entre 50 e 70, recuperação

n1 = int(input("Digite a primeira nota: \n"))
n2 = int(input("Digite a segunda nota: \n"))
media = (n1 + n2) / 2 
if media >= 70:
    print("Aprovado")
elif media >= 50:
    print("Recuperação")
else:
    print("Sua nota foi abaixo da média, Reprovado!")
                                  