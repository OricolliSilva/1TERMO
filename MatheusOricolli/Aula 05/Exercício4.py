#Exemplo 2. Laço While (Repetições Indeterminadas) 
#Use o while quando voc~e não sabe quando vai parar. Ele depende de uma condição (Como um sensor de seguraça ou um botão de emergência).
#Exemplo: Monitor de Temperatura (Loop infinito Controlado)

#Repete enquanto a temperatura estiver segura
#Início
temperatura = 2
while temperatura < 40:
    print(f"Temperatura atual: {temperatura}°C. Sistema Operando...")
    temperatura+= 5 #Simulando o aquecimento da máquina
print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

    # Exemplo: Menu de Interação 
opcao = ""

while opcao != "sair" and "SAIR":
    opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ").upper().lower()
    if opcao != "sair" and "SAIR":
        print(f"Dado '{opcao}' registrado no banco de dados.")
print("Sistema encerrado.")  