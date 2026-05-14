#Exercício 4 - Soma de cargas de Energia (for)
#Uma fábrica tem 5 máquinas. Peça ao úsuario (via input dentro do loop) 
# o consumo em kwh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica

print("Consumo de KWH das máquinas da empresa")
total = 0 
for máquina in range(1, 6):
    print(f"{máquina}° máquina")
    consumo = int(input("Digite a quantidade de KWH da máquina: "))
    total += consumo
print("O valor total de KWH das 5 máquinas é igual a", total)
print("Produção do dia finalizada")
