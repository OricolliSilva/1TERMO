#Exercício 3 
#Montar uma tabuada, inicialmente pode ser usado por um valor fixo e depois usar a pergunta

for número in range(1, 11):
    print( 5* número)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

n1 = int(input("Digite o número da sua tabúada: \n"))

for número in range(1, 11):
    print(f"{n1} X {número} = ", n1 * número)       