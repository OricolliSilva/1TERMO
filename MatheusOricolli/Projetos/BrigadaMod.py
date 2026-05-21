import tkinter as tk
from tkinter import messagebox

total_cadastrados = 0
total_em_dia = 0

def cadastro_pessoal():
    global total_cadastrados, total_em_dia
    
    try:
      
        nome = nome_campo.get()
        setor = setor_campo.get()
        nr35 = nr35_campo.get()
        nr10 = nr10_campo.get()
        
        ano_brigada = int(campo_brigada.get())

        if setor == "elétrica":
            EPIs = "Luvas de Alta tensão e botas dielétricas "
        elif setor == "trabalho em altura":
            EPIs = "Cinturão de segurança e talabarte"
        else:
            EPIs = "Consultar setor de segurança"

        ano_atual = 2026
        if (ano_atual - ano_brigada) >2:
            status_brigada = "Vencido"
            mensagem = "Treinamento vencido! Encaminhar para a reciclagem"
        else:
            status_brigada = "OK"
            mensagem = "Treinamento valido!"

        total_cadastrados += 1
        if nr10 == "OK" and nr35 == "OK" and status_brigada == "OK":
            total_em_dia +=1
            


        

        print("MENSAGEM: Treinamento Vencido! Encaminhar para reciclagem.")
        return "Vencido"
        else:
            print("MENSAGEM: Treinamento Válido.")
        return "OK"

    while True:
    nome = input("\nDigite o nome do funcionário: ")
    setor = input("Digite o setor (Elétrica / Trabalho em Altura): ")
    nr10 = input("Status NR-10 (OK/Pendente): ")
    nr35 = input("Status NR-35 (OK/Pendente): ")
    ano_brigada = int(input("Ano do último treinamento da Brigada: "))

    total_cadastrados = total_cadastrados + 1

    print("\n--- RESULTADOS ---")
    verificar_epi(setor)
    status_brigada = alerta_reciclagem(ano_brigada)

    if nr10 == "OK" and nr35 == "OK" and status_brigada == "OK":
        total_em_dia = total_em_dia + 1
    continuar = input("\nDeseja realizar mais um cadastro? (Sim/Não): ").strip().lower()
    
    if continuar not in ["sim", "s"]:
        break

    print("\n" + "="*60)
    print(f"{'RELATÓRIO GERAL':^60}")
    print(f"{'-'*25:^60}")
    print(f"Total de funcionários cadastrados: {total_cadastrados:>6}")
    print(f"Funcionários com treinamentos em dia: {total_em_dia:>3}")
    print("="*60)

app = tk.Tk()
app.title("Página Oficial da brigada.")
app.geometry("500x400")