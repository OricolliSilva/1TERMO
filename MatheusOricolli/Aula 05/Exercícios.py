#Use o Laço "for" (Repetições Determinadas)
#Use o 'for' quando vocce sabe extamente quantas vezes algo deve acontecer ( como ler 10 sensores ou processar uma lisyta de peças )
#Exemplo: Relatório de Produção Diária
#imagine que vocce tem uma meta deproduzir 5 lotes e quer numerar cada um:

# Exemplo 1 
for lote in range(1, 11):
    print(f"Processando lote número {lote}...")
    print("Qualidade verificada. [OK]")
    print("Produção do dia finalizada")

for carros in range(1, 21):
    print(f"Qantidade de carros na loja {carros}...")
    print("Carro presente. [OK]")
    print("Todos os carros estão presentes")

#Exemplo 2 
#Contar até 4 
for i in range(5):
    print(i)

#Exercício 3 
peças = ["Engrenagem", "Eixo", "Rolamento", "Parafuso"]
máquinas = ["Máquina 1", "Máquina 2"] 

for item in peças:
    print(f"Item em estoque: {item}")
    for maq in máquinas:
        print(f"Máquinas que temos {maq}")