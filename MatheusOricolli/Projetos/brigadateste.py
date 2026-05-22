import tkinter as tk
from tkinter import messagebox

total_cadastrados = 0
total_em_dia = 0

def processar_cadastro():
    global total_cadastrados, total_em_dia
    
    try:
    
        nome = campo_nome.get()
        setor = campo_setor.get().strip().lower() 
        nr10 = campo_nr10.get().strip().upper()   
        nr35 = campo_nr35.get().strip().upper()  
        
        ano_brigada = int(campo_ano_brigada.get())
        
        if setor == "elétrica" or setor == "eletrica":
            EPIs = "Luvas de Alta tensão e botas dielétricas"
        elif setor == "trabalho em altura":
            EPIs = "Cinturão de segurança e talabarte"
        else:
            EPIs = "Consultar setor de segurança"
            
        ano_atual = 2026
        if (ano_atual - ano_brigada) > 2:
            status_brigada = "Vencido"
            mensagem = "Treinamento vencido! Encaminhar para a reciclagem"
        else:
            status_brigada = "OK"
            mensagem = "Treinamento válido!"
            
        total_cadastrados += 1
        if nr10 == "OK" and nr35 == "OK" and status_brigada == "OK":
            total_em_dia += 1
            
        resultado_texto = (
            f"Funcionário: {nome}\n"
            f"Setor: {campo_setor.get()}\n"
            f"EPIs Recomendados: {EPIs}\n"
            f"Brigada: {mensagem}\n\n"
            f"--- Cadastro Realizado com Sucesso! ---"
        )
        
        messagebox.showinfo("Resultados - SESMT", resultado_texto)
      
        campo_nome.delete(0, tk.END)
        campo_setor.delete(0, tk.END)
        campo_nr10.delete(0, tk.END)
        campo_nr35.delete(0, tk.END)
        campo_ano_brigada.delete(0, tk.END)
        
        campo_nome.focus()
        
    except ValueError:
        messagebox.showerror("Erro de Digitação", "Por favor, digite um ano válido para o treinamento da Brigada!")

def encerrar_sessao():
   
    relatorio_final = (
        f"--- STATUS DOS CADASTROS REALIZADOS ---\n\n"
        f"Total de Funcionários Cadastrados: {total_cadastrados}\n"
        f"Funcionários com tudo em dia (NRs e Brigada): {total_em_dia}\n\n"
        f"Sessão finalizada com sucesso!"
    )

    messagebox.showinfo("Balanço Geral - SESMT", relatorio_final)
  
    app.destroy()


app = tk.Tk()
app.title("Sistema de Controle SESMT")
app.geometry("500x520") 


lbl_titulo = tk.Label(app, text="Controle da SESMT\nInforme os dados abaixo:", font=("Arial", 12, "bold"))
lbl_titulo.pack(pady=10)

lbl_nome = tk.Label(app, text="Nome do Funcionário:")
lbl_nome.pack(pady=2)
campo_nome = tk.Entry(app, font=("Arial", 11), width=40)
campo_nome.pack(pady=2)


lbl_setor = tk.Label(app, text="Setor (Elétrica / Trabalho em Altura):")
lbl_setor.pack(pady=2)
campo_setor = tk.Entry(app, font=("Arial", 11), width=40)
campo_setor.pack(pady=2)


lbl_nr10 = tk.Label(app, text="Status NR-10 (OK/Pendente):")
lbl_nr10.pack(pady=2)
campo_nr10 = tk.Entry(app, font=("Arial", 11), width=20)
campo_nr10.pack(pady=2)


lbl_nr35 = tk.Label(app, text="Status NR-35 (OK/Pendente):")
lbl_nr35.pack(pady=2)
campo_nr35 = tk.Entry(app, font=("Arial", 11), width=20)
campo_nr35.pack(pady=2)


lbl_ano_brigada = tk.Label(app, text="Ano do último treinamento da Brigada:")
lbl_ano_brigada.pack(pady=2)
campo_ano_brigada = tk.Entry(app, font=("Arial", 11), width=20)
campo_ano_brigada.pack(pady=2)


btn_enviar = tk.Button(app, text="Cadastrar Funcionário", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", command=processar_cadastro)
btn_enviar.pack(pady=15)


btn_sair = tk.Button(app, text="Sair", font=("Arial", 11, "bold"), bg="#F44336", fg="white", command=encerrar_sessao)
btn_sair.pack(pady=5)


app.mainloop()