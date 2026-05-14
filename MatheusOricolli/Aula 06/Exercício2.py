#Exercício 1 
#Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5 )
n1 = 5
for número in range(1, 11):
    if número != 5:
        print(f"Número {número} detectado.")
        continue 
    print(f"Falha no sensor {n1}. Mandando para a análise.")

