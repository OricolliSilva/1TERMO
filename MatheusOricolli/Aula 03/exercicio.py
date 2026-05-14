#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Exercicio 1
#Cálculo de notas por semestre onde terá duas notas formativas e uma nota somativa para encerrar o semestre.
#os valores de notas são de 0 a 100

print("Notas do Matheus Oricolli do primeiro semestre: ")

n1 = int(input("Digite a primeira nota do aluno: \n"))
n2 = int(input("Digite a segunda nota do aluno: \n"))
n3 = int(input("Digite a terceira nota do aluno: \n"))
ntotal = n1 + n2 + n3 /3 
print("Valor final da nota: \n ", round(ntotal, 2)) 

print("Notas do Matheus Oricolli do segundo semestre: ")

m1 = int(input("Digite a primeira nota do aluno: \n "))
m2 = int(input("Digite a segunda nota do aluno: \n "))
m3 = int(input("Digite a terceira nota do aluno: \n"))
mtotal = m1 + m2 + m3 /3
print("A nota final do segundo semestre: \n", round(mtotal, 2))

print("As notas do primeiro e segundo semestre foram: \n primeiro semestre: \n",  round(ntotal, 2), "\n" "Segundo semestre: \n", round(mtotal, 2)) 


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
 #Arredondar casas decimais
 # s1 = n1 + n2 +n3 /3
 #round(s1),2 
 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

 #Exemplo 3 
def boas_vindas(nome, cargo,): 
    print(f"Olá, {nome}! Você é o novo {cargo}")

boas_vindas("Matheus", "Desenvolvedor")
boas_vindas("Carlos","Gerente")
boas_vindas("ana","Gerente")
boas_vindas("Gerente","ANA")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Exemplo 4
def configurar_conexao(servidor, porta= 8000):
    print(f"Conectando a {servidor} na porta {porta}...")

configurar_conexao("192.168.1.1")           #usa a porta 8000
configurar_conexao("10.0.0.1", 3000)        #usa a porta 3000
configurar_conexao("192.168.1.2")
configurar_conexao("10.0.0.2", 3001)
# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Exercicio 3
#Calculo de idsde: Deve apresentar o nome, curso, data de nascimento e apresentar a idade sua no final

nome = str(input("Digite seu nome: \n"))
curso = input("Digite seu curso \n")
data = str(input("Digite seu ano de nascimento: \n"))
print(f"Aqui estão os seus dados: \n" "Nome: \n", nome + "\n Curso: \n",  curso + "\n Data: \n",  data  ) 
print("A sua idade é: \n", 2026 - float(data)) 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

