import tkinter as tk
from tkinter import messagebox

total_cadastrados = 0
total_em_dia = 0

def processar_cadastro():
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
            
            resultado_texto = (
            f"Funcionário: {nome}\n"
            f"Setor: {setor}\n"
            f"EPIs Recomendados: {epis}\n"
            f"Brigada: {msg_brigada}\n\n"
            f"--- RELATÓRIO GERAL ATUALIZADO ---\n"
            f"Total de Cadastrados: {total_cadastrados}\n"
            f"Funcionários em Dia: {total_em_dia}"
        )

            messagebox.showinfo("Resultados - SESMT",resultado_texto)

        campo_nome.delete(0, tk.END)
        campo_setor.delete(0, tk.END)
        campo_nr10.delete(0, tk.END)
        campo_nr35.delete(0, tk.END)
        campo_ano_brigada.delete(0, tk.END)

    except ValueError:
  
        messagebox.showerror("Erro de Digitação", "Por favor, digite um ano válido para o treinamento da Brigada!")

app = tk.Tk()
app.title("Sistema de Controle SESMT")
app.geometry("500x450") 

       

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
campo_campo_nr35 = campo_nr35 = tk.Entry(app, font=("Arial", 11), width=20)
campo_nr35.pack(pady=2)


lbl_ano_brigada = tk.Label(app, text="Ano do último treinamento da Brigada:")
lbl_ano_brigada.pack(pady=2)
campo_ano_brigada = tk.Entry(app, font=("Arial", 11), width=20)
campo_ano_brigada.pack(pady=2)


btn_enviar = tk.Button(app, text="Cadastrar Funcionário", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", command=processar_cadastro)
btn_enviar.pack(pady=20)

app.mainloop()