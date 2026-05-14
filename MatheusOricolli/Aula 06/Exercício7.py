#Exercício 7: Sistema inteligente de Manutenção
#Crie um programa que receba 2 dados: a pressões atual (float) e as horas de uso acumuladas (int) de uma turbina
#O programa deve classificar o estado de máquina seguindo esta hierarquia: 
#Crítico (Prioridade 1): Se a pressão for maior que 100 OU as horas de uso forem maior que 10.000
#Mensagem: PARADA  IMEDIATA: Risco de falha catastrofica.
#Alerta (Prioridade 2): Se a pressão estiver entre 80 e 100 (inclusive).
#Mensagem: MANUTENÇÃO AGENDADA: Pressão acima do ideal.
#Monitoramento (Prioridade 3): Se as horas de uso forem entre 8.000 e 10.000.
#Mensagem: AVISO: Máquina aproximando - se da revisão de 10k horas.
#Normal: Para qualquer outro caso que não se encaixe nos acima.
#Mensagem: SISTEMA OPERAL: Todos os parametros dentro da normalidade.
