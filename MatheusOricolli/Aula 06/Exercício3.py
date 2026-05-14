#Exercício 3
#Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa.
from time import sleep
print("Sinalização do semáforo")
print("1 = Verde")
print("2 = Amarelo")
print("3 = vermelho")
c1 = int(input("Digite o número da cor escolhida: \n"))
for i in range(1, 6):
    if c1 == 1:
        print(" Cor Verde ")
    sleep(1.0)
for i in range(1,6):
    if c1 == 2:
     print(" Cor Amarela")
    sleep(1.0)
for i in range(1,6):
    if c1 == 3:
        print("Cor Vermelha")
    sleep(1.0)
