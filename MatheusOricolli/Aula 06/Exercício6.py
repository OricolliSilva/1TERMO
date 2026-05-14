#Exercício 6 - Uma balança industrial está pensando em um lote de 6 
#sacos de insumos. O peso idealde cada saco é 5kg, mas o sistema aceita variações.

total = 0 
for sacos in range(1, 7):
    print(f"{sacos}° máquina")
    consumo = int(input("Digite a quantidade de Kg do saco, pouco acima de 50kg: \n"))
    total += consumo
print("O valor total de Kg dos 6 sacos é igual a", total)

