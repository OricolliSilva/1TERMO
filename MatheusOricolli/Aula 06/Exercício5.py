#Exercício 5 - Identificador de peças Defeituosas (for + if)
#percorra uma lista de medida de peças
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# O padrão de qualidade aceita peças com exatamente 50.0 ou mais
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada"

medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
for i in medidas:

    if i <= 50.0:
        print(" Peça com medidas", i, "Rejeitada")
    elif i >= 50.0:
        print(" Peça com medidas", i, "Aprovada")
else:
    print("O padrão de qualidade está abaixo!")