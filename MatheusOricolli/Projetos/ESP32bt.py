from machine import Pin
import time

botao1 = Pin(4, Pin.IN, Pin.PULL_UP)   
buzzer1 = Pin(5, Pin.OUT)

botao2 = Pin(15, Pin.IN, Pin.PULL_UP)  
buzzer2 = Pin(2, Pin.OUT)

print("Sistema iniciado! Os dois botões estão ativos.")


bloqueado_ate = 0   
desligar_buzzer_ate = 0 
mensagem_exibida = True  

while True:
    tempo_atual = time.time() 
 
    if tempo_atual >= desligar_buzzer_ate:
        buzzer1.value(0)
        buzzer2.value(0)

    
    if tempo_atual < bloqueado_ate:
        time.sleep(0.05)
        continue  
    
    if not mensagem_exibida:
        print("-> Sistema liberado! Já pode clicar novamente.")
        mensagem_exibida = True  

    if botao1.value() == 0:
        print("DIREITO")
        buzzer1.value(1)
        
        desligar_buzzer_ate = tempo_atual + 2  
        bloqueado_ate = tempo_atual + 6       
        mensagem_exibida = False               

    elif botao2.value() == 0:
        print("ESQUERDO")
        buzzer2.value(1)
        
        desligar_buzzer_ate = tempo_atual + 2  
        bloqueado_ate = tempo_atual + 6      
        mensagem_exibida = False               

    time.sleep(0.05)
