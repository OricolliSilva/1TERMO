#Exercicio 3
#Criar um algoritimo para aplicação de descontos para produtos como sapatos, aplicar 10%, para produtos como roupas, 5% e perfumes, 2%
print("Algoritimo de descontos")
print(" 1 = Sapatos")
print(" 2 = Roupas")
print(" 3 = Perfumes")
d1 = int(input("Digite o número do produto escolhido: \n"))
if d1 == 1:
    print("Você escolheu Sapatos \n")
    print("O produto Sapato tem um desconto total de 10%!!")
    v1 = float(input("Digite o valor do produto: \n"))
    qtde = float(input("Digite a quantidade do profuto: \n"))
    print("Valor total da compra sem o desconto: \n", v1 * qtde)
    print("Valor do desconto da compra: \n", (v1 * qtde) * 10 /100)
    print("Valor total da compra com o desconto: \n", v1 * qtde -(v1 * qtde) * 10 /100)
elif d1 == 2:
    print("Você escolheu Roupas \n")
    print("O produto Roupas tem um desconto de 5%!!")
    v2 = float(input("Digite o valor do produto: \n"))
    qtde2 = float(input("Digite a quantidade do profuto: \n"))
    print("Valor total da compra sem o desconto: \n", v2 * qtde2)
    print("Valor do desconto da compra: \n", (v2 * qtde2) * 5 /100)
    print("Valor total da compra com o desconto: \n", v2 * qtde2 -(v2 * qtde2) * 5 /100)
elif d1 == 3:
    print("Você escolheu o produto Perfumes \n")
    print("O produto Perfumes tem um desconto de 2%!!")
    v3 = float(input("Digite o valor do produto: \n"))
    qtde3 = float(input("Digite a quantidade do profuto: \n"))
    print("Valor total da compra sem o desconto: \n", v3 * qtde3)
    print("Valor do desconto da compra: \n", (v3 * qtde3) * 2 /100)
    print("Valor total da compra com o desconto: \n", v3 * qtde3 -(v3 * qtde3) * 2 /100)
else:
     print("Esse produto não tem desconto!!") 