# #Exercício 1:
# #Crie um script que mostre o caminho da pasta atual.
# import os
# print(os.getcwd())

# #Exercício 2 
# #Liste os arquivos da pasta atual.
# import os
# print(os.listdir())

# #Exercício 3
# # Crie uma pasta chamada "projetos" e depois renomeie para "meus_projetos". Por Fim. exclua a pasta.
# import os
# os.mkdir("projetos")
# os.rename("projetos", "meus_projetos")
# os.rmdir("meus_projetos")

# #Exercício 4 
# #Crie um arquivo chamado "log.txt" e escreva a mensagem "Log de atividades". Depois, leia o conteúdo do arquivo e exiba na tela.
# import os
# os.mkdir("log.txt")
# with open("log.txt", "w") as arquivo:
#     arquivo.write("Log de atividades")
# with open("log.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

#Exemplo de dicionário:
#Crie um dicionário co informações sobre uma pessoa e acesse um valor usando uma chave
# pessoa = {
#     "nome": "Alice",
#     "idade": 30,
#     "cidade": "São Pulo"
# }
# print(pessoa["nome"])

# pessoa2 = {
#     "nome": "Oricolli",
#     "idade": 16,
#     "cidade": "Limeira"
# }
# print(pessoa[""])
# print(pessoa2["nome", "idade"])

#Exercício 6: Desligar o PC ( comando para windows)
# os.system("shutdown /s /t 0")  #CUIDADO: este comando irá desligaro computador imediatamente!
# os.system("echo Desligamento simulado. Comando de desligamento para segurança")
# with open("desliga.bat", "w") as desligar:
#     desligar.write("shutdown -s -t 3600 -c \"desligamento programado para daqui a 1 hora. Salve seu trabalho!!\"")
#     # -s comando para desligar
#     # -t tempo definir
#     # -a desligamento

# with open("desliga.bat", "r") as desligar:
#     conteudo = desligar.read()
#     print(conteudo) 


#Exercício 7: Criar um arquivo de backup
#Escreva um script que crie um arquivo de backup do arquivo "notas.txt" com o nome "notas_backup.txt". O script dee ler o conteúdo
#de "notas.txt" e escrever o novo arquivo.
import os
with open("notas.txt", "r") as original:
    conteudo = original.read()
with open("notas_backup.txt", "w") as backup:
    backup.write(conteudo)
print("Backup realizado com sucesso!")

#Exemplo 2: Criar um script  de limpeza de arquivos 
#Escreva um script que liste os arquivos de uma pasta e exclua os arquivos com extensão ".tmp". O script deve exibir uma mensagem para cada arquivo excluido
pasta = os.listdir()
for arquivo in pasta:
    if arquivo.endswith(".tmp"):
        os.remove(arquivo)
        print(f"Arquivo {arquivo} excluido.")
print("Limpeza de arquivo sconcluida") 

#Tratamento de erros com python 
#Erros comuns:
# - ZeroDivisionError: sivisão por zero
# - ValueError: conversão de tipo inválida

#Exercício 8: Criar um script de monitoramento de temperatura
#Escreva um script que monitore a temperatura de um motor.
#O script deve ler a temperatura do arquivo "temperatura.txt" e exibir uma mensagem de alerta se a temperatura estiver acima de 70°
