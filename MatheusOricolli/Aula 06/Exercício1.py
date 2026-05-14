#Lista de temperaturas lidas pelo sensor por minuto
leituras = [70, 75, 82, 98, 110, 85, 80]

for temp in leituras:
    if temp > 100:
        print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência. ")
        break  # O loop para aqui e NÃO lê os próximos valores (85 e 80)
    print(f"Temperatura está em {temp}°C. Operação normal.")

print("Sistema desligado. Aguardando manutenção.")

#-------------------------------------------------------------------------------------------------------------------------------

# materiais = ["metal", "metal", "plástico", "metal", "vidro", "metal"]
# for peça in materiais:
#     if peça != "metal":
#         print(f"Aviso: peça de {peça} detectada. Desviando para Descarte...")
#         continue # Pula o restante do código abaixo e vai para a próxima peça 

# #Esse código só roda se a peça for de metal
# print(f"Processando peça de {peça}. Furando e Polindo...")

# print("Fim do lote de produção.")