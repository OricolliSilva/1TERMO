#Exercicio 2
#Criar um algoritimo para demonstrar a sinalização de um  semáforo
print("Sinalização do semáforo")
print("1 = Verde")
print("2 = Amarelo")
print("3 = vermelho")
c1 = int(input("Digite o número da cor escolhida: \n"))
if c1 == 1:
 print(" Cor Verde")
elif c1 == 2:
 print(" Cor Amarela")
elif c1 == 3:
 print("Cor Vermelha")
else:
 print("Somente essas cores!!")